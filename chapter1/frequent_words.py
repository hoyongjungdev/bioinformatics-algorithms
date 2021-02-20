import sys


def main():
    text = input()
    k = int(input())

    print(to_string(frequent_words(text, k)))


def frequent_words(text: str, k: int) -> list:
    frequent_patterns = []

    freq_map = frequency_table(text, k)
    max_val = max_map(freq_map)

    for k in freq_map:
        if freq_map[k] == max_val:
            frequent_patterns.append(k)

    return frequent_patterns


def frequency_table(text: str, k: int):
    freq_map = {}
    n = len(text)

    for i in range(n - k + 1):
        pattern = text[i:i + k]
        freq_map[pattern] = freq_map.get(pattern, 0) + 1

    return freq_map


def max_map(freq_map: dict) -> int:
    max_val = -sys.maxsize
    for (k, v) in freq_map.items():
        if max_val < v:
            max_val = v

    return max_val


def to_string(words: list) -> str:
    sorted_words = sorted(words)
    return ' '.join(sorted_words)


def test():
    assert to_string(frequent_words('ACAACTATGCATCACTATCGGGAACTATCCT', 5)) == 'ACTAT'
    assert to_string(frequent_words('CGATATATCCATAG', 3)) == 'ATA'
    assert to_string(frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)) == 'CATG GCAT'


if __name__ == '__main__':
    main()
