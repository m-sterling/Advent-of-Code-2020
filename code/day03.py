def main():
    with open('../inputs/day03', 'r') as f:
        src = [line.strip() for line in f.readlines()]
    print(part1(src))
    print(part2(src))

def part1(src):
    total = 0
    x, y = 0, 0
    while y < len(src):
        line = src[y]
        if line[x % len(line)] == '#':
            total += 1
        x += 3
        y += 1

    return total

def part2(src):
    total = 1
    for i, j in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        _total = 0
        x, y = 0, 0
        while y < len(src):
            line = src[y]
            if line[x % len(line)] == '#':
                _total += 1
            x += i
            y += j
        total *= _total

    return total

main()
