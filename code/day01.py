def main():
    with open('../inputs/day01', 'r') as f:
        src = f.readlines()
    print(part1(src))
    print(part2(src))

def part1(src):
    src = list(map(int, src))
    for i in range(len(src)):
        for j in range(i+1, len(src)):
            a, b = src[i], src[j]
            if a + b == 2020:
                return a*b
    return -1

def part2(src):
    src = list(map(int, src))
    for i in range(len(src)):
        for j in range(i+1, len(src)):
            for k in range(i+2, len(src)):
                a, b, c = src[i], src[j], src[k]
                if a + b + c == 2020:
                    return a*b*c
    return -1

main()
