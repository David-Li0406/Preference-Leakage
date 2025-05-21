for MODEL in qwen2.5_7b qwen2.5_3b qwen3_1.7b qwen3_4b qwen3_8b qwen3_14b
    do
        llamafactory-cli train config/additional/full_sft_gemini_all_${MODEL}.yaml
        llamafactory-cli train config/additional/full_sft_gpt4_all_${MODEL}.yaml
    done