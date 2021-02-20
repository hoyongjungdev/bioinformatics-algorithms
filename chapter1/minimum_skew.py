def main():
    genome = input()
    print(to_string(minimum_skew(genome)))


def skew(genome: str) -> list[int]:
    result = [0]

    for i in range(0, len(genome)):
        g = genome[i]

        if g == 'C':
            diff = -1
        elif g == 'G':
            diff = 1
        else:
            diff = 0

        result.append(result[i] + diff)

    return result


def minimum_skew(genome: str) -> list[int]:
    result = []

    skew_val = skew(genome)
    min_val = min(skew_val)

    for i in range(len(skew_val)):
        if skew_val[i] == min_val:
            result.append(i)

    return result


def to_string(nums: list[int]) -> str:
    return ' '.join(map(str, nums))


def test():
    assert to_string(skew('CATGGGCATCGGCCATACGCC')) == '0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2'


if __name__ == '__main__':
    main()
