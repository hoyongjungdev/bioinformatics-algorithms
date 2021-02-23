import sys
from random import randrange

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from chapter3.greedy_motif_search import motifs_to_profile, score
from chapter3.profile_most_probable import profile_most_probable


def main():
    first = input()
    first_split = list(map(int, first.split(' ')))
    k = first_split[0]
    t = first_split[1]
    dna = []

    for i in range(t):
        dna.append(input())

    motif, score_history = repeat(dna, k, t, 200)

    for m in motif:
        print(m)

    series = pd.Series(score_history, index=np.arange(len(score_history)))

    series.plot()
    plt.xlabel('# of Iterations')
    plt.ylabel('Score')
    plt.show()


def repeat(dna: list[str], k: int, t: int, n: int) -> (list[str], list[int]):
    min_score = sys.maxsize
    best_motifs = []
    score_history = []

    for i in range(n):
        motifs = randomized_motif_search(dna, k, t)
        s = score(motifs)

        if min_score > s:
            best_motifs = motifs
            min_score = s

        score_history.append(min_score)

    return best_motifs, score_history


def randomized_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    motifs = []

    for i in range(t):
        text = dna[i]
        t_len = len(text)
        start = randrange(0, t_len - k + 1)
        motifs.append(text[start:start + k])

    best_motifs = motifs

    while True:
        profile = motifs_to_profile(motifs)
        motifs = []

        for i in range(t):
            motif = profile_most_probable(dna[i], k, profile)
            motifs.append(motif)

        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs


if __name__ == '__main__':
    main()
