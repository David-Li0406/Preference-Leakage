#!/usr/bin/env bash
#SBATCH -t 0-06:00:00
#SBATCH --mem=32G
#SBATCH -c 4

for JUDGE_MODEL in gpt4 gemini llama
    do
        python self_recognition_pairwise.py --judge_model $JUDGE_MODEL
    done