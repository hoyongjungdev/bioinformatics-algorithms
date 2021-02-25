import sys

from common.string import join_sorted


def main():
    text = input()
    k = int(input())

    print(join_sorted(frequent_words(text, k)))


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


if __name__ == '__main__':
    main()
