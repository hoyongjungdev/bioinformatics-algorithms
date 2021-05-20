def dna_to_rna(dna: str):
    rna = map(
        lambda base: 'U' if base == 'T' else base,
        list(dna)
    )

    return ''.join(rna)


def test():
    assert dna_to_rna('ATGGCC') == 'AUGGCC'


if __name__ == '__main__':
    test()
