from .frequent_words import max_map
from .reverse_complement import reverse_complement


def main():
    text = input()
    next_line = input()
    nums = list(map(int, next_line.split(' ')))

    k = nums[0]
    d = nums[1]

    print(to_string(frequent_words_rc(text, k, d)))


def frequent_words_with_mismatches(text: str, k: int, d: int) -> list[str]:
    patterns = []
    freq_map = {}
    n = len(text)

    for i in range(n - k + 1):
        pattern = text[i:i + k]
        neighborhood = neighbor(pattern, d)

        for n in neighborhood:
            freq_map[n] = freq_map.get(n, 0) + 1

    m = max_map(freq_map)

    for pattern in freq_map:
        if freq_map[pattern] == m:
            patterns.append(pattern)

    return patterns


def frequent_words_rc(text: str, k: int, d: int) -> list[str]:
    patterns = []
    freq_map = {}
    n = len(text)

    for i in range(n - k + 1):
        pattern = text[i:i + k]
        neighborhood = neighbor(pattern, d)

        for n in neighborhood:
            freq_map[n] = freq_map.get(n, 0) + 1

        pattern_rc = reverse_complement(pattern)
        neighborhood_rc = neighbor(pattern_rc, d)

        for n in neighborhood_rc:
            freq_map[n] = freq_map.get(n, 0) + 1

    m = max_map(freq_map)

    for pattern in freq_map:
        if freq_map[pattern] == m:
            patterns.append(pattern)

    return patterns


def neighbor(pattern: str, maximum_distance: int) -> list[str]:
    result = []

    for d in range(maximum_distance + 1):
        result.extend(neighbor_exact(pattern, d))

    return result


def neighbor_exact(pattern: str, distance: int) -> list[str]:
    bases = 'CGAT'

    if distance == 0:
        return [pattern]

    n1 = [first + latter
          for first in bases
          for latter in neighbor_exact(pattern[1:], distance - 1)
          if first != pattern[0]]

    if distance < len(pattern):
        n2 = [pattern[0] + latter for latter in neighbor_exact(pattern[1:], distance)]

        return n1 + n2

    return n1


def to_string(arr: list[str]):
    return ' '.join(sorted(arr))


def test():
    assert to_string(frequent_words_with_mismatches('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1)) == 'ATGC ATGT GATG'


if __name__ == '__main__':
    main()
