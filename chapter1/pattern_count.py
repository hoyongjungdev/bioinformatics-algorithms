def main():
    text = input()
    pattern = input()

    print(pattern_count(text, pattern))


def pattern_count(text: str, pattern: str):
    count = 0

    text_len = len(text)
    pattern_len = len(pattern)

    for i in range(text_len - pattern_len + 1):
        if text[i:i+pattern_len] == pattern:
            count += 1

    return count


def test():
    assert pattern_count('GCGCG', 'GCG') == 2
    assert pattern_count('ACAACTATGCATACTATCGGGAACTATCCT', 'ACTAT') == 3


if __name__ == '__main__':
    main()
