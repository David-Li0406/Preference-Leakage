# For w/ same instruction
for MODEL in gpt4 gemini
    do
        CONFIG="config/inherit/full_sft_${MODEL}_inherit.yaml"
        llamafactory-cli train $CONFIG
    done

# For w/ different instruction
for MODEL in gpt4 gemini
    do
        CONFIG="config/inherit/full_sft_${MODEL}_inherit_new.yaml"
        llamafactory-cli train $CONFIG
    done