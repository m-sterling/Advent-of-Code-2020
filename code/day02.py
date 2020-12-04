def main():
    with open('../inputs/day02', 'r') as f:
        src = [line.strip() for line in f.readlines()]
    print(part1(src))
    print(part2(src))

def part1(src):
    total = 0
    for line in src:
        # format: <low-high count> <letter:> <password>
        words = line.split()
        # take first word (<low-high count>) and split it by - to get `low` as
        #   first item and `high` as second, then cast them to `int`s via `map()`
        l,h = map(int, words[0].split('-'))
        # then take the first character of the second word - second only contains the
        #   letter to check for and a colon, so it's always guaranteed to be the first char
        letter = words[1][0]
        # finally the password is the third word, nothing fancy
        pw = words[2]
        # check to see if the count of `letter` in `pw` is in the range `[l, h]`
        if l <= pw.count(letter) <= h:
            total += 1
    return total

def part2(src):
    total = 0
    for line in src:
        # same format as above for words, low/high, letter, and pw
        words = line.split()
        l,h = map(int, words[0].split('-'))
        letter = words[1][0]
        pw = words[2]
        # this time, `low` and `high` correspond to one-indexed positions in `pw` to check
        #   if either of indices contain the letter specified by `letter` - but not both
        if (pw[l-1] == letter and not (pw[h-1] == letter)) or \
                (not (pw[l-1] == letter) and pw[h-1] == letter):
            total += 1
    return total

main()
