#!/bin/bash

if [ "$1" == "--sft" ]; then
    for MODEL in gemini gpt4 llama
        do
            CONFIG="config/sft/judge_config_${MODEL}.yaml" 
            python gen_judgment.py --setting-file $CONFIG1
        done
elif [ "$1" == "--inherit" ]; then
    for MODEL in gemini gpt4
        do
            CONFIG1="config/inherit/judge_config_${MODEL}.yaml"
            CONFIG2="config/inherit/judge_config_${MODEL}_new.yaml"      
            python gen_judgment.py --setting-file $CONFIG1
            python gen_judgment.py --setting-file $CONFIG1
        done
elif [ "$1" == "--dpo" ]; then
    for MODEL in gemini gpt4
        do
            CONFIG1="config/dpo/judge_config_${MODEL}.yaml"      
            python gen_judgment.py --setting-file $CONFIG1
        done
elif [ "$1" == "--icl" ]; then
    python gen_judgment.py --setting-file config/icl/judge_config_gemini.yaml
    python gen_judgment.py --setting-file config/icl/judge_config_gpt4.yaml
elif [ "$1" == "--mix" ]; then
    for RATIO in 0.1 0.3 0.5 0.7
        do
            for MODEL in gemini gpt4
                do
                    CONFIG="config/mix_synthetic/judge_config_${MODEL}_${RATIO}.yaml"
                    python gen_judgment.py --setting-file $CONFIG
                done
        done
    
    for RATIO in 0.1 0.3 0.5 0.7
        do
            for MODEL in gemini
                do
                    CONFIG="config/mix/judge_config_${MODEL}_${RATIO}.yaml"
                    python gen_judgment.py --setting-file $CONFIG
                done
        done
elif [ "$1" == "--same_family" ]; then
    python gen_judgment.py --setting-file config/family/judge_config_gemini_1.0.yaml
    python gen_judgment.py --setting-file config/family/judge_config_chatgpt.yaml

    python gen_judgment.py --setting-file config/family/judge_config_gemini_1.5_pro.yaml
    python gen_judgment.py --setting-file config/family/judge_config_gpt4-turbo.yaml
elif [ "$1" == "--additional" ]; then
    for MODEL in qwen-2.5-3b qwen-2.5-7b qwen-3-1.7b qwen-3-4b qwen-3-8b qwen-3-14b
        do
            CONFIG1="config/additional/judge_config_${MODEL}-gemini.yaml"
            CONFIG2="config/additional/judge_config_${MODEL}-gpt4.yaml"
            
            python gen_judgment.py --setting-file $CONFIG1
            python gen_judgment.py --setting-file $CONFIG2
        done
fi