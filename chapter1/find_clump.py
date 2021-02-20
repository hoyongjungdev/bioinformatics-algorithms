from .frequent_words import frequency_table, to_string


def main():
    text = input()
    next_line = input()
    split = next_line.split(' ')
    k = int(split[0])
    l = int(split[1])
    t = int(split[2])

    print(to_string(find_clump(text, k, l, t)))


def find_clump(text: str, k: int, l: int, t: int) -> list[str]:
    patterns = set()
    n = len(text)

    for i in range(n - l + 1):
        window = text[i:i + l]
        freq_map = frequency_table(window, k)

        for key in freq_map:
            if freq_map[key] >= t:
                patterns.add(key)

    return list(patterns)


def test():
    assert to_string(
        find_clump(
            'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC',
            5,
            75,
            4
        )
    ) == 'AATGT CGACA GAAGA'


if __name__ == '__main__':
    main()
