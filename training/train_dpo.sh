for MODEL in gpt4 gemini
    do
        llamafactory-cli train config/dpo/dpo_mistral_${MODEL}_moss_oasst_lima.yaml
    done