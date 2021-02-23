from chapter3.base_map import base_map


def main():
    text = input()
    k = int(input())

    profile = []

    for i in range(4):
        inp = input()
        row = list(map(float, inp.split(' ')))
        profile.append(row)

    print(profile_most_probable(text, k, profile))


def profile_most_probable(text: str, k: int, profile: list):
    max_prob = -1
    probable = ''

    t_len = len(text)

    for i in range(t_len - k + 1):
        sub = text[i:i + k]
        p = prob(sub, profile)

        if max_prob < p:
            max_prob = p
            probable = sub

    return probable


def prob(pattern: str, profile: list):
    p_len = len(pattern)
    p = 1.0

    for i in range(p_len):
        base = pattern[i]
        idx = base_map[base]
        p *= profile[idx][i]

    return p


if __name__ == '__main__':
    main()
