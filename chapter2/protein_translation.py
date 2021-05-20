def main():
    pattern = input()
    print(protein_translation(pattern))


def protein_translation(pattern: str):
    code = {
        'CUG': 'L',
        'CUA': 'L',
        'CUC': 'L',
        'CUU': 'L',
        'CGG': 'R',
        'CGA': 'R',
        'CGC': 'R',
        'CGU': 'R',
        'CCG': 'P',
        'CCA': 'P',
        'CCC': 'P',
        'CCU': 'P',
        'CAG': 'Q',
        'CAA': 'Q',
        'CAC': 'H',
        'CAU': 'H',
        'AUG': 'M',
        'AUA': 'I',
        'AUC': 'I',
        'AUU': 'I',
        'AGG': 'R',
        'AGA': 'R',
        'AGC': 'S',
        'AGU': 'S',
        'ACG': 'T',
        'ACA': 'T',
        'ACC': 'T',
        'ACU': 'T',
        'AAG': 'K',
        'AAA': 'K',
        'AAC': 'N',
        'AAU': 'N',
        'UUG': 'L',
        'UUA': 'L',
        'UUC': 'F',
        'UUU': 'F',
        'UGG': 'W',
        'UGA': '*',
        'UGC': 'C',
        'UGU': 'C',
        'UCG': 'S',
        'UCA': 'S',
        'UCC': 'S',
        'UCU': 'S',
        'UAG': '*',
        'UAA': '*',
        'UAC': 'Y',
        'UAU': 'Y',
        'GUG': 'V',
        'GUA': 'V',
        'GUC': 'V',
        'GUU': 'V',
        'GGG': 'G',
        'GGA': 'G',
        'GGC': 'G',
        'GGU': 'G',
        'GCG': 'A',
        'GCA': 'A',
        'GCC': 'A',
        'GCU': 'A',
        'GAG': 'E',
        'GAA': 'E',
        'GAC': 'D',
        'GAU': 'D',
    }

    result = []

    for i in range(len(pattern) // 3):
        codon = pattern[3 * i:3 * i + 3]
        p = code.get(codon, '')

        if p == '*':
            break

        result.append(p)

    return ''.join(result)


def test():
    assert protein_translation('UAUACGAAA') == 'YTK'
    assert protein_translation('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA') == 'MAMAPRTEINSTRING'


if __name__ == '__main__':
    main()
