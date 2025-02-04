# for multisource synthetic data mixing
for RATIO in 0.1 0.3 0.5 0.7
    do
        for MODEL in gpt4 gemini
            do
                CONFIG=config/mix_synthetic/full_sft_${MODEL}_${RATIO}.yaml
                llamafactory-cli train $CONFIG
            done
    done
    

# for manually-written data mixing
for RATIO in 0.1 0.3 0.5 0.7
    do
        for MODEL in gpt4 gemini
            do
                CONFIG=config/mix/full_sft_${MODEL}_${RATIO}.yaml
                llamafactory-cli train $CONFIG
            done
    done