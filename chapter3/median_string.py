import sys

from chapter1.hamming_distance import hamming_distance


def main():
    k = int(input())
    dna = []

    while True:
        try:
            dna.append(input())
        except EOFError:
            break

    print(median_string(k, dna))


def median_string(k: int, dna: list[str]) -> str:
    d = sys.maxsize
    median = ""

    for m in kmer(k):
        d_m = distance(m, dna)
        if d > d_m:
            d = d_m
            median = m

    return median


def distance(pattern: str, dna: list[str]) -> int:
    total_distance = 0
    p_len = len(pattern)

    for text in dna:
        d = sys.maxsize

        for i in range(len(text) - p_len + 1):
            sub = text[i:i + p_len]
            d_i = hamming_distance(sub, pattern)

            if d > d_i:
                d = d_i

        total_distance += d

    return total_distance


def kmer(k: int) -> list[str]:
    bases = 'ATCG'

    if k == 1:
        return list(bases)

    result = [head + tail
              for head in bases
              for tail in kmer(k - 1)]

    return result


def to_string(arr: list[str]):
    return ' '.join(sorted(arr))


def test():
    assert to_string(kmer(2)) == 'AA AC AG AT CA CC CG CT GA GC GG GT TA TC TG TT'


if __name__ == '__main__':
    main()
