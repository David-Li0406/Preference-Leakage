
for MODEL in gpt4 gemini llama
    do
        llamafactory-cli train config/sft/full_sft_${MODEL}_all.yaml
    done