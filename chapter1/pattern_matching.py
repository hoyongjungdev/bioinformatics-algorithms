def main():
    pattern = input()
    genome = input()

    print(to_string(pattern_matching(pattern, genome)))


def pattern_matching(pattern: str, genome: str) -> list[int]:
    pattern_size = len(pattern)
    genome_size = len(genome)

    result = []

    for i in range(genome_size - pattern_size + 1):
        if genome[i:i + pattern_size] == pattern:
            result.append(i)

    return result


def to_string(indices: list[int]) -> str:
    sorted_indices = sorted(indices)
    return ' '.join(map(str, sorted_indices))


def test():
    assert to_string(pattern_matching('ATAT', 'GATATATGCATATACTT')) == '1 3 9'


if __name__ == '__main__':
    main()
