def main():
    with open('../inputs/day02', 'r') as f:
        src = [line.strip() for line in f.readlines()]
    print(part1(src))
    print(part2(src))

def part1(src):
    total = 0
    for line in src:
        words = line.split()
        l,h = map(int, words[0].split('-'))
        letter = words[1][0]
        pw = words[2]
        if l <= pw.count(letter) <= h:
            total += 1
    return total

def part2(src):
    total = 0
    for line in src:
        words = line.split()
        l,h = map(int, words[0].split('-'))
        letter = words[1][0]
        pw = words[2]
        if (pw[l-1] == letter and not (pw[h-1] == letter)) or \
                (not (pw[l-1] == letter) and pw[h-1] == letter):
            total += 1
    return total

main()
