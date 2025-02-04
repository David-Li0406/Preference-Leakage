import os
import json
import time
import requests
import openai
import copy
import together
from together import AsyncTogether, Together
import datetime

import time
import google.generativeai as genai

from loguru import logger

safe = [
        {
            "category": "HARM_CATEGORY_DANGEROUS",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
    ]

os.environ['TOGETHER_API_KEY'] = ''
client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
async_client = AsyncTogether(api_key=os.environ.get("TOGETHER_API_KEY"))
os.environ['OPENAI_API_KEY'] = ''
os.environ['GEMINI_API_KEY'] = ''

DEBUG = int(os.environ.get("DEBUG", "0"))


def generate_together(
    model,
    messages,
    max_tokens=2048,
    temperature=0.7,
    streaming=False,
    n=1,
):

    output = None
    messages = [{"role": "user", "content": messages}]

    for sleep_time in [1, 2, 4, 8, 16, 32]:

        try:

            endpoint = "https://api.together.xyz/v1/chat/completions"

            if DEBUG:
                logger.debug(
                    f"Sending messages ({len(messages)}) (last message: `{messages[-1]['content'][:20]}...`) to `{model}`."
                )

            res = requests.post(
                endpoint,
                json={
                    "model": model,
                    "max_tokens": max_tokens,
                    "temperature": (temperature if temperature > 1e-4 else 0),
                    "messages": messages,
                    "n":n,
                },
                headers={
                    "Authorization": f"Bearer {os.environ.get('TOGETHER_API_KEY')}",
                },
            )
            if "error" in res.json():
                logger.error(res.json())
                if res.json()["error"]["type"] == "invalid_request_error":
                    logger.info("Input + output is longer than max_position_id.")
                    return None

            output = [item["message"]["content"] for item in res.json()["choices"]]
            break

        except Exception as e:
            logger.error(e)
            if DEBUG:
                logger.debug(f"Msgs: `{messages}`")

            logger.info(f"Retry in {sleep_time}s..")
            time.sleep(sleep_time)

    if output is None:

        return output

    # output = output.strip()
    output = [item.strip() for item in output]

    if DEBUG:
        logger.debug(f"Output: `{output[:20]}...`.")

    return output



def generate_openai(
    model,
    messages,
    max_tokens=2048,
    temperature=0.7,
):

    client = openai.OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    messages = [{"role": "user", "content": messages}]

    for sleep_time in [1, 2, 4, 8, 16, 32]:
        try:

            if DEBUG:
                logger.debug(
                    f"Sending messages ({len(messages)}) (last message: `{messages[-1]['content'][:20]}`) to `{model}`."
                )

            completion = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            output = completion.choices[0].message.content
            break

        except Exception as e:
            logger.error(e)
            logger.info(f"Retry in {sleep_time}s..")
            time.sleep(sleep_time)

    output = output.strip()

    return output


def generate_gemini(
    model,
    messages,
    max_tokens=2048,
    temperature=0.7
):
    try:
        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
        model = genai.GenerativeModel(model)
        response = model.generate_content(messages, safety_settings=safe)
        return response.text.strip()
    except Exception as E:
        print(E)
        return None


def generate_vllm(prompt, model, client, n=1):

    kwargs = {
        'messages':[
            {"role": "user", "content": prompt}
        ],
        "n":n
    }
    completion = client.chat.completions.create(**kwargs)
    res = [item.message.content.strip() for item in completion.choices]
    return res