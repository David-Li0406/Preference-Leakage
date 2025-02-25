#!/bin/bash

if [ "$1" == "--sft" ]; then
    export OPENAI_API_KEY=
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft.json" \
        --annotators_config 'alpaca_eval_gpt4o-2024-11-20' \
        --output_path "output/sft/gpt-4o-judge-gpt-4o-as-reference-gemini-as-output"

    export OPENAI_API_KEY=
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft.json" \
        --annotators_config 'gemini-1.5-flash' \
        --output_path "output/sft/gemini-judge-gpt-4o-as-reference-gemini-as-output"
elif [ "$1" == "--inherit" ]; then
    export OPENAI_API_KEY=
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft_inherit.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft_inherit.json" \
        --annotators_config 'alpaca_eval_gpt4o-2024-11-20' \
        --output_path "output/inherit/gpt-4o-judge-gpt-4o-as-reference-gemini-as-output-inherit"

    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft_inherit_new.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft_inherit_new.json" \
        --annotators_config 'alpaca_eval_gpt4o-2024-11-20' \
        --output_path "output/inherit/gpt-4o-judge-gpt-4o-as-reference-gemini-as-output-inherit-new"

    export OPENAI_API_KEY=
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft_inherit.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft_inherit.json" \
        --annotators_config 'gemini-1.5-flash' \
        --output_path "output/inherit/gemini-judge-gpt-4o-as-reference-gemini-as-output-inherit"
    
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft_inherit_new.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft_inherit_new.json" \
        --annotators_config 'gemini-1.5-flash' \
        --output_path "output/inherit/gemini-judge-gpt-4o-as-reference-gemini-as-output-inherit-new"
elif [ "$1" == "--dpo" ]; then
    export OPENAI_API_KEY=
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_dpo_moss_oasst_lima.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_dpo_moss_oasst_lima.json" \
        --annotators_config 'alpaca_eval_gpt4o-2024-11-20' \
        --output_path "output/dpo/gpt-4o-judge-gpt-4o-as-reference-gemini-as-output-dpo"

    export OPENAI_API_KEY=
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_dpo_moss_oasst_lima.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_dpo_moss_oasst_lima.json" \
        --annotators_config 'gemini-1.5-flash' \
        --output_path "output/dpo/gemini-judge-gpt-4o-as-reference-gemini-as-output-dpo"
elif [ "$1" == "--icl" ]; then
    export OPENAI_API_KEY=
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_moss_oasst_lima_sft_icl.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_moss_oasst_lima_sft_icl.json" \
        --annotators_config 'alpaca_eval_gpt4o-2024-11-20' \
        --output_path "output/icl/gpt-4o-judge-gpt-4o-as-reference-gemini-as-output-icl"

    export OPENAI_API_KEY=
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_moss_oasst_lima_sft_icl.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_moss_oasst_lima_sft_icl.json" \
        --annotators_config 'gemini-1.5-flash' \
        --output_path "output/icl/gemini-judge-gpt-4o-as-reference-gemini-as-output-icl"
elif [ "$1" == "--mix" ]; then
    for RATIO in 0.1 0.3 0.5 0.7
    do
    export OPENAI_API_KEY=
    # # gpt-4o as a judge
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft_mix_synthetic_$RATIO.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft_mix_synthetic_$RATIO.json" \
        --annotators_config 'alpaca_eval_gpt4o-2024-11-20' \
        --output_path "output/mix_synthetic/gpt-4o-judge-gpt-4o-as-reference-gemini-as-output-mix-synthetic-$RATIO"

    export OPENAI_API_KEY=
    # gemini as a judge
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft_mix_synthetic_$RATIO.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft_mix_synthetic_$RATIO.json" \
        --annotators_config 'gemini-1.5-flash' \
        --output_path "output/mix_synthetic/gemini-judge-gpt-4o-as-reference-gemini-as-output-mix-synthetic-$RATIO"

    done

    for RATIO in 0.1 0.3 0.5 0.7
    do
    export OPENAI_API_KEY=
    # # gpt-4o as a judge
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft_mix_$RATIO.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft_mix_$RATIO.json" \
        --annotators_config 'alpaca_eval_gpt4o-2024-11-20' \
        --output_path "output/mix/gpt-4o-judge-gpt-4o-as-reference-gemini-as-output-mix-synthetic-$RATIO"

    export OPENAI_API_KEY=
    # gemini as a judge
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft_mix_$RATIO.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft_mix_$RATIO.json" \
        --annotators_config 'gemini-1.5-flash' \
        --output_path "output/mix/gemini-judge-gpt-4o-as-reference-gemini-as-output-mix-synthetic-$RATIO"

    done
elif [ "$1" == "--same_family" ]; then
    # chatgpt & gemini-1.0
    export OPENAI_API_KEY=
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft.json" \
        --annotators_config 'alpaca_eval_gpt_3.5_turbo_0125' \
        --output_path "output/family/chatgpt-judge-gpt-4o-as-reference-gemini-as-output"

    export OPENAI_API_KEY=
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft.json" \
        --annotators_config 'gemini-1.0-pro' \
        --output_path "output/family/gemini-1.0-judge-gpt-4o-as-reference-gemini-as-output"


    # gpt-4-turbo & gemini-1.5-flash
    export OPENAI_API_KEY=
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft.json" \
        --annotators_config 'alpaca_eval_gpt-4-turbo-2024-04-09' \
        --output_path "output/family/gpt-4-turbo-judge-gpt-4o-as-reference-gemini-as-output"

    export OPENAI_API_KEY=
    alpaca_eval --model_outputs "example/output_Mistral-7B-v0.1_gemini_sft.json" \
        --reference_outputs "example/output_Mistral-7B-v0.1_gpt4_sft.json" \
        --annotators_config 'gemini-1.5-pro' \
        --output_path "output/family/gemini-1.5-pro-judge-gpt-4o-as-reference-gemini-as-output"
fi