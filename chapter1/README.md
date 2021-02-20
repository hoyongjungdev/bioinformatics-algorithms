## Reference
- Bioinformatics Algorithms: An Active Learning Approach, Chapter 1
- https://www.bioinformaticsalgorithms.org/bioinformatics-chapter-1

## The Skew Diagram of E. coli
![skew](./e_coli_skew.png)

- Plot script: `python3 -m chapter1.skew_visualize < chapter1/E_coli.txt`
- The minimum skew algorithm reveals that minimum indices are 3923620, 3923621, 3923622, 3923623.
- Minimum skew script: `python3 -m chapter1.minimum_skew < chapter1/E_coli.txt `