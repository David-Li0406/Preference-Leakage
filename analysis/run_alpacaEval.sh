#!/bin/bash

if [ "$1" == "--sft" ]; then
    for MODEL in gpt4 gemini llaam
        do
            python alpacaEval.py --judge_name $MODEL --tuning_technique sft
        done
elif [ "$1" == "--inherit" ]; then
    for MODEL in gpt4 gemini
        do
            python alpacaEval_icl.py --judge_name $MODEL --tuning_technique sft --exp inherit
            python alpacaEval_icl.py --judge_name $MODEL --tuning_technique sft --exp inherit_new
        done
elif [ "$1" == "--dpo" ]; then
    python alpacaEval.py --judge_name gpt4 --tuning_technique dpo --exp moss_oasst_lima
    python alpacaEval.py --judge_name gemini --tuning_technique dpo --exp moss_oasst_lima
elif [ "$1" == "--icl" ]; then
    for MODEL in gpt4 gemini
        do
            python alpacaEval_icl.py --judge_name $MODEL --tuning_technique sft
        done
elif [ "$1" == "--mix" ]; then
    for MODEL in gpt4 gemini
    do
        for RATIO in 0.1 0.3 0.5 0.7
            do
                python alpacaEval.py --judge_name $MODEL --tuning_technique sft --exp mix_synthetic --ratio $RATIO
            done
    done

    for MODEL in gpt4 gemini
    do
        for RATIO in 0.1 0.3 0.5 0.7
            do
                python alpacaEval.py --judge_name $MODEL --tuning_technique sft --exp mix --ratio $RATIO
            done
    done
fi