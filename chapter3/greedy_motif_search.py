from chapter3.base_map import base_map
from chapter3.profile_most_probable import profile_most_probable


def main():
    first = input()
    first_split = list(map(int, first.split(' ')))
    k = first_split[0]
    t = first_split[1]
    dna = []

    for i in range(t):
        dna.append(input())

    motif = greedy_motif_search(dna, k, t)

    for m in motif:
        print(m)


def greedy_motif_search(dna: list[str], k: int, t: int) -> list:
    best_motifs = [text[:k] for text in dna]

    first = dna[0]

    for i in range(len(first) - k + 1):
        sub = first[i:i + k]
        motifs = [sub]

        for j in range(1, t):
            profile = motifs_to_profile(motifs)
            motif = profile_most_probable(dna[j], k, profile)
            motifs.append(motif)

        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    return best_motifs


def motifs_to_profile(motifs: list[str]) -> list:
    m_len = len(motifs)
    k = len(motifs[0])

    profile = [[1.0 for _ in range(k)] for _ in range(4)]

    for i in range(k):
        for j in range(m_len):
            base = motifs[j][i]
            profile[base_map[base]][i] += 1

        c_sum = 0

        for b in range(4):
            c_sum += profile[b][i]

        for b in range(4):
            profile[b][i] /= c_sum

    return profile


def score(motifs: list[str]) -> int:
    t = len(motifs)
    k = len(motifs[0])

    d_sum = 0

    for i in range(k):
        count = [0, 0, 0, 0]

        for j in range(t):
            base = motifs[j][i]
            idx = base_map[base]

            count[idx] += 1

        max_count = max(count)
        d_sum += t - max_count

    return d_sum


if __name__ == '__main__':
    main()
