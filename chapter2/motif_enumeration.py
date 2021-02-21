from chapter1.frequent_words_with_mismatches import neighbor
from chapter1.hamming_distance import hamming_distance


def main():
    first_line = input()
    first_line_split = list(map(int, first_line.split(' ')))
    k = first_line_split[0]
    d = first_line_split[1]

    dna = []

    while True:
        try:
            line = input()
            dna.append(line)
        except EOFError:
            break

    print(' '.join(sorted(motif_enumeration(dna, k, d))))


def motif_enumeration(dna: list[str], k: int, d: int) -> list[str]:
    patterns = set()

    first = dna[0]

    for i in range(len(first) - k + 1):
        pattern = first[i:i + k]

        neighborhood = neighbor(pattern, d)

        for n in neighborhood:
            add_to_pattern = True

            for j in range(1, len(dna)):
                text = dna[j]

                found = False

                for l in range(len(text) - k + 1):
                    sub = text[l:l + k]
                    if hamming_distance(n, sub) <= d:
                        found = True
                        break

                if not found:
                    add_to_pattern = False
                    break

            if add_to_pattern:
                patterns.add(n)

    return list(patterns)


if __name__ == '__main__':
    main()
