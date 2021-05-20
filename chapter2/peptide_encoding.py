from chapter1.reverse_complement import reverse_complement
from chapter2.protein_translation import protein_translation
from chapter2.dna_to_rna import dna_to_rna

def peptide_encoding(text: str, peptide: str) -> list[str]:
    size = 3 * len(peptide)

    text_rc = reverse_complement(text)
    result = set()

    for i in range(0, len(text) - size + 1, 3):
        sub = text[i:i+size]
        sub_rc = text_rc[i:i+size]
        if len(sub) < size:
            break

        if protein_translation(dna_to_rna(sub)) == peptide:
            result.add(sub)

        if protein_translation(dna_to_rna(sub_rc)) == peptide:
            result.add(sub_rc)

    return list(result)
