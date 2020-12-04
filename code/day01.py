def main():
    with open('../inputs/day01', 'r') as f:
        src = f.readlines()
    print(part1(src))
    print(part2(src))

def part1(src):
    # convert all numbers in the list to integers
    src = list(map(int, src))
    for i in range(len(src)):
        for j in range(i+1, len(src)):
            # double for loop, second loop starts at the number
            #   after src[i] to avoid duplicate checking
            a, b = src[i], src[j]
            if a + b == 2020:
                return a*b
    return -1

def part2(src):
    # same as above, convert numbers in list to ints
    src = list(map(int, src))
    for i in range(len(src)):
        for j in range(i+1, len(src)):
            for k in range(i+2, len(src)):
                # same idea, each nested loop starts one after the one enclosing it
                a, b, c = src[i], src[j], src[k]
                if a + b + c == 2020:
                    return a*b*c
    return -1

main()
