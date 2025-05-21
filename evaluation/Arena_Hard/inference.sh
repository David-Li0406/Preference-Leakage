export PYTHONIOENCODING=utf-8;
HOME_DIR=`realpath ..`

GPU=0,1
PORT=8000
TP_SIZE=2

export CUDA_VISIBLE_DEVICES=${GPU}

declare -A MODEL_ZOO
# for sft exp
MODEL_ZOO["mistral-7b-v0.1_gpt4_all"]="../../saves/Mistral-7B-v0.1/gpt4_sft_30000"
MODEL_ZOO["mistral-7b-v0.1_gemini_all"]="../../saves/Mistral-7B-v0.1/gemini_sft_30000"
MODEL_ZOO["mistral-7b-v0.1_llama_all"]="../../saves/Mistral-7B-v0.1/llama_sft_30000"

# for inherit exp
MODEL_ZOO["mistral-7b-v0.1_gpt4_all_inherit"]="../../saves/Mistral-7B-v0.1/gpt4_sft_30000_inherit"
MODEL_ZOO["mistral-7b-v0.1_gemini_all_inherit"]="../../saves/Mistral-7B-v0.1/gemini_sft_30000_inherit"
MODEL_ZOO["mistral-7b-v0.1_gpt4_all_inherit_new"]="../../saves/Mistral-7B-v0.1/gpt4_sft_30000_inherit_new"
MODEL_ZOO["mistral-7b-v0.1_gemini_all_inherit_new"]="../../saves/Mistral-7B-v0.1/gemini_sft_30000_inherit_new"

# for icl exp
MODEL_ZOO["mistral-7B-v0.1_moss_oasst_lima_gpt4"]="../../saves/Mistral-7B-v0.1/moss_oasst_lima_sft_30000"
MODEL_ZOO["mistral-7B-v0.1_moss_oasst_lima_gemini"]="../../saves/Mistral-7B-v0.1/moss_oasst_lima_sft_30000"

# for dpo exp
MODEL_ZOO["mistral-7B-v0.1_dpo_moss_oasst_lima_gpt4"]="../../saves/Mistral-7B-v0.1/gpt4_dpo_30000_moss_oasst_lima"
MODEL_ZOO["mistral-7B-v0.1_dpo_moss_oasst_lima_gemini"]="../../saves/Mistral-7B-v0.1/gemini_dpo_30000_moss_oasst_lima"


# for mix exp
MODEL_ZOO["mistral-7b-v0.1_gpt4_mix_0.1"]="../../saves/Mistral-7B-v0.1/mix/gpt4_sft_0.1"
MODEL_ZOO["mistral-7b-v0.1_gpt4_mix_0.3"]="../../saves/Mistral-7B-v0.1/mix/gpt4_sft_0.3"
MODEL_ZOO["mistral-7b-v0.1_gpt4_mix_0.5"]="../../saves/Mistral-7B-v0.1/mix/gpt4_sft_0.5"
MODEL_ZOO["mistral-7b-v0.1_gpt4_mix_0.7"]="../../saves/Mistral-7B-v0.1/mix/gpt4_sft_0.7"

MODEL_ZOO["mistral-7b-v0.1_gemini_mix_0.1"]="../../saves/Mistral-7B-v0.1/mix/gemini_sft_0.1"
MODEL_ZOO["mistral-7b-v0.1_gemini_mix_0.3"]="../../saves/Mistral-7B-v0.1/mix/gemini_sft_0.3"
MODEL_ZOO["mistral-7b-v0.1_gemini_mix_0.5"]="../../saves/Mistral-7B-v0.1/mix/gemini_sft_0.5"
MODEL_ZOO["mistral-7b-v0.1_gemini_mix_0.7"]="../../saves/Mistral-7B-v0.1/mix/gemini_sft_0.7"

# for synthetic mix exp

MODEL_ZOO["mistral-7b-v0.1_gpt4_mix_synthetic_0.1"]="../../saves/Mistral-7B-v0.1/mix_synthetic/gpt4_sft_0.1"
MODEL_ZOO["mistral-7b-v0.1_gpt4_mix_synthetic_0.3"]="../../saves/Mistral-7B-v0.1/mix_synthetic/gpt4_sft_0.3"
MODEL_ZOO["mistral-7b-v0.1_gpt4_mix_synthetic_0.5"]="../../saves/Mistral-7B-v0.1/mix_synthetic/gpt4_sft_0.5"
MODEL_ZOO["mistral-7b-v0.1_gpt4_mix_synthetic_0.7"]="../../saves/Mistral-7B-v0.1/mix_synthetic/gpt4_sft_0.7"

MODEL_ZOO["mistral-7b-v0.1_gemini_mix_synthetic_0.1"]="../../saves/Mistral-7B-v0.1/mix_synthetic/gemini_sft_0.1"
MODEL_ZOO["mistral-7b-v0.1_gemini_mix_synthetic_0.3"]="../../saves/Mistral-7B-v0.1/mix_synthetic/gemini_sft_0.3"
MODEL_ZOO["mistral-7b-v0.1_gemini_mix_synthetic_0.5"]="../../saves/Mistral-7B-v0.1/mix_synthetic/gemini_sft_0.5"
MODEL_ZOO["mistral-7b-v0.1_gemini_mix_synthetic_0.7"]="../../saves/Mistral-7B-v0.1/mix_synthetic/gemini_sft_0.7"


# for additional exp
MODEL_ZOO["qwen-2.5-3b-gemini"]="../../saves/Qwen2.5-3B/gemini_sft_30000"
MODEL_ZOO["qwen-2.5-3b-gpt4"]="../../preference_leakage/saves/Qwen2.5-3B/gpt4_sft_30000"
MODEL_ZOO["qwen-2.5-7b-gemini"]="../../preference_leakage/saves/Qwen2.5-7B/gemini_sft_30000"
MODEL_ZOO["qwen-2.5-7b-gpt4"]="../../preference_leakage/saves/Qwen2.5-7B/gpt4_sft_30000"
MODEL_ZOO["qwen-3-1.7b-gemini"]="../../preference_leakage/saves/Qwen3-1.7B/gemini_sft_30000"
MODEL_ZOO["qwen-3-1.7b-gpt4"]="../../preference_leakage/saves/Qwen3-1.7B/gpt4_sft_30000"
MODEL_ZOO["qwen-3-4b-gemini"]="../../preference_leakage/saves/Qwen3-4B/gemini_sft_30000"
MODEL_ZOO["qwen-3-4b-gpt4"]="../../preference_leakage/saves/Qwen3-4B/gpt4_sft_30000"
MODEL_ZOO["qwen-3-8b-gemini"]="../../preference_leakage/saves/Qwen3-8B/gemini_sft_30000"
MODEL_ZOO["qwen-3-8b-gpt4"]="../../preference_leakage/saves/Qwen3-8B/gpt4_sft_30000"
MODEL_ZOO["qwen-3-14b-gemini"]="../../preference_leakage/saves/Qwen3-14B/gemini_sft_30000"
MODEL_ZOO["qwen-3-14b-gpt4"]="../../preference_leakage/saves/Qwen3-14B/gpt4_sft_30000"


if [ "$1" == "--sft" ]; then
    for MODEL in gpt4 gemini llama
        do
        JUDGE_MODEL="mistral-7b-v0.1_${MODEL}_all"
        model_name=${MODEL_ZOO["$JUDGE_MODEL"]}

        # run the vllm server
        python -m vllm.entrypoints.openai.api_server \
                --model ${model_name} \
                --tensor-parallel-size ${TP_SIZE} \
                --download-dir "${HOME_DIR}/model_cache/" \
                --port ${PORT} &

        PID=$!

        sleep 200
        # run inference
        CONFIG="config/sft/gen_answer_config_${MODEL}.yaml"
        python gen_answer.py --setting-file $CONFIG
        kill $PID
        done

elif [ "$1" == "--inherit" ]; then
    for MODEL in gpt4 gemini
        do
        JUDGE_MODEL="mistral-7b-v0.1_${MODEL}_all_inherit"
        model_name=${MODEL_ZOO["$JUDGE_MODEL"]}
        # run the vllm server
        python -m vllm.entrypoints.openai.api_server \
                --model ${model_name} \
                --tensor-parallel-size ${TP_SIZE} \
                --download-dir "${HOME_DIR}/model_cache/" \
                --port ${PORT} &
        PID=$!

        sleep 200
        # run inference
        CONFIG="config/inherit/gen_answer_config_${MODEL}.yaml"
        python gen_answer.py --setting-file $CONFIG
        kill $PID

        JUDGE_MODEL="mistral-7b-v0.1_${MODEL}_all_inherit_new"
        model_name=${MODEL_ZOO["$JUDGE_MODEL"]}
        # run the vllm server
        python -m vllm.entrypoints.openai.api_server \
                --model ${model_name} \
                --tensor-parallel-size ${TP_SIZE} \
                --download-dir "${HOME_DIR}/model_cache/" \
                --port ${PORT} &
        PID=$!

        sleep 200
        # run inference
        CONFIG="config/dpo/gen_answer_config_${MODEL}_new.yaml"
        python gen_answer.py --setting-file $CONFIG
        kill $PID
        done

elif [ "$1" == "--dpo" ]; then
    for MODEL in gpt4 gemini
        do
        JUDGE_MODEL="mistral-7B-v0.1_dpo_moss_oasst_lima_${MODEL}"
        model_name=${MODEL_ZOO["$JUDGE_MODEL"]}

        # run the vllm server
        python -m vllm.entrypoints.openai.api_server \
                --model ${model_name} \
                --tensor-parallel-size ${TP_SIZE} \
                --download-dir "${HOME_DIR}/model_cache/" \
                --port ${PORT} &

        PID=$!

        sleep 200
        # run inference
        CONFIG="config/dpo/gen_answer_config_${MODEL}.yaml"
        python gen_answer.py --setting-file $CONFIG
        kill $PID
        done

elif [ "$1" == "--icl" ]; then
    for MODEL in gpt4 gemini
    do

        JUDGE_MODEL="mistral-7B-v0.1_moss_oasst_lima_${MODEL}"
        model_name=${MODEL_ZOO["$JUDGE_MODEL"]}
        # run the vllm server
        python -m vllm.entrypoints.openai.api_server \
                --model ${model_name} \
                --tensor-parallel-size ${TP_SIZE} \
                --download-dir "${HOME_DIR}/model_cache/" \
                --port ${PORT} &

        PID=$!
        sleep 200
        # run inference
        CONFIG="config/icl/gen_answer_config_${MODEL}.yaml"
        python gen_answer_icl.py --demonstration_name $MODEL --setting-file $CONFIG
        kill $PID
    done
elif [ "$1" == "--mix" ]; then
    for RATIO in 0.1 0.3 0.5 0.7
    do
        for MODEL in gpt4 gemini
            do
                JUDGE_MODEL="mistral-7b-v0.1_${MODEL}_mix_${RATIO}"
                model_name=${MODEL_ZOO["$JUDGE_MODEL"]}
                echo $model_name

                # run the vllm server
                python -m vllm.entrypoints.openai.api_server \
                        --model ${model_name} \
                        --tensor-parallel-size ${TP_SIZE} \
                        --download-dir "${HOME_DIR}/model_cache/" \
                        --port ${PORT} &

                PID=$!

                sleep 200
                # run inference
                CONFIG="config/mix/gen_answer_config_${MODEL}_${RATIO}.yaml"
                python gen_answer.py --setting-file $CONFIG
                kill $PID
            done
    done

    for RATIO in 0.3 0.5 0.7
        do
                for MODEL in gpt4 gemini
                do
                        JUDGE_MODEL="mistral-7b-v0.1_${MODEL}_mix_synthetic_${RATIO}"
                        model_name=${MODEL_ZOO["$JUDGE_MODEL"]}
                        echo $model_name

                        # run the vllm server
                        python -m vllm.entrypoints.openai.api_server \
                                --model ${model_name} \
                                --tensor-parallel-size ${TP_SIZE} \
                                --download-dir "${HOME_DIR}/model_cache/" \
                                --port ${PORT} &

                        PID=$!

                        sleep 200
                        # run inference
                        CONFIG="config/mix_synthetic/gen_answer_config_${MODEL}_${RATIO}.yaml"
                        python gen_answer.py --setting-file $CONFIG
                        kill $PID
                done
        done
elif [ "$1" == "--additional" ]; then
    do
        for MODEL in qwen-2.5-3b qwen-2.5-7b qwen-3-1.7b qwen-3-4b qwen-3-8b qwen-3-14b
                JUDGE_MODEL="${MODEL}-gpt4"
                model_name=${MODEL_ZOO["$JUDGE_MODEL"]}

                # run the vllm server
                python -m vllm.entrypoints.openai.api_server \
                        --model ${model_name} \
                        --tensor-parallel-size ${TP_SIZE} \
                        --download-dir "${HOME_DIR}/model_cache/" \
                        --port ${PORT} &

                PID=$!

                sleep 200
                # run inference
                CONFIG="config/additional/gen_answer_config_${MODEL}-gpt4.yaml"
                
                python gen_answer.py --setting-file $CONFIG
                kill $PID
        done
    done
fi