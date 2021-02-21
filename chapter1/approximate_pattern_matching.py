from .hamming_distance import hamming_distance


def main():
    pattern = input()
    text = input()
    d = int(input())

    print(' '.join(
        map(str, approximate_pattern_matching(pattern, text, d)))
    )


def approximate_pattern_matching(pattern: str, text: str, d: int) -> list[int]:
    p_len = len(pattern)
    t_len = len(text)

    result = []

    for i in range(t_len - p_len + 1):
        sub = text[i:i + p_len]
        if hamming_distance(sub, pattern) <= d:
            result.append(i)

    return result


if __name__ == '__main__':
    main()
