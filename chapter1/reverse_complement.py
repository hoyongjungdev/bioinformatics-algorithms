def main():
    pattern = input()

    print(reverse_complement(pattern))


def reverse_complement(pattern: str) -> str:
    result = []

    base_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }

    for p in pattern:
        result.append(base_map[p])

    return ''.join(reversed(result))


def test():
    assert reverse_complement('AGTCGCATAGT') == 'ACTATGCGACT'


if __name__ == '__main__':
    main()
