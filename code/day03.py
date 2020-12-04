def main():
    with open('../inputs/day03', 'r') as f:
        src = [line.strip() for line in f.readlines()]
    print(part1(src))
    print(part2(src))

def part1(src):
    total = 0
    # could have done a `for` loop, not sure why a `while` was used, oh well
    # `x` = the position in the line to check for a tree - increases by `3` every iteration
    # `y` = the line to use for above - increases by `1` every iteration
    x, y = 0, 0
    while y < len(src):
        # get the current `line`
        line = src[y]
        # if the current position is a tree, increase total
        if line[x % len(line)] == '#':
            total += 1
        # slide over 3 horiz and 1 vert
        x += 3
        y += 1

    return total

def part2(src):
    # initialising `total` to 0 would mean nothing would be added, since 0 * anything == 0
    total = 1
    # need to multiply the count of five different slopes together
    for i, j in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        _total = 0
        # almost exactly like above
        x, y = 0, 0
        while y < len(src):
            line = src[y]
            if line[x % len(line)] == '#':
                # `_total` contains this iteration's tree count; could have used a `list`
                #   and `functools.reduce()` or `math.prod()` but this is a bit more verbose
                _total += 1
            # slide over `i` horiz and `j` vert, since this time they differ
            x += i
            y += j
        # multiply the result into the grand `total`
        total *= _total

    return total

main()
