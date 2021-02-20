from .pattern_matching import pattern_matching, to_string
from .reverse_complement import reverse_complement


def main():
    genome = input()
    pattern = 'ATGATCAAG'

    print(to_string(pattern_matching(pattern, genome)))
    print(to_string(pattern_matching(reverse_complement(pattern), genome)))


if __name__ == '__main__':
    main()
