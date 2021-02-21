import sys
from random import randrange

from chapter2.greedy_motif_search import motifs_to_profile, score
from chapter2.profile_most_probable import profile_most_probable


def main():
    first = input()
    first_split = list(map(int, first.split(' ')))
    k = first_split[0]
    t = first_split[1]
    dna = []

    for i in range(t):
        dna.append(input())

    motif = repeat(dna, k, t, 1000)

    for m in motif:
        print(m)


def repeat(dna: list[str], k: int, t: int, n: int) -> list[str]:
    min_score = sys.maxsize
    best_motifs = []

    for i in range(n):
        motifs = randomized_motif_search(dna, k, t)
        s = score(motifs)

        if min_score > s:
            best_motifs = motifs
            min_score = s

    return best_motifs


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
