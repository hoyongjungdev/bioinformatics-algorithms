def main():
    p = input()
    q = input()
    print(hamming_distance(p, q))


def hamming_distance(p: str, q: str) -> int:
    size = len(p)
    distance = 0

    for i in range(size):
        if p[i] != q[i]:
            distance += 1

    return distance


if __name__ == '__main__':
    main()
