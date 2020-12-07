import re
def main():
    with open('../inputs/day06', 'r') as f:
        src = [line.strip() for line in f.read().split('\n')]
    print(part1(src))
    print(part2(src))

def part1(src):
    total = 0
    # groups are read in like passports from day 4, except they're sets
    group = []
    for line in src:
        if line != "": # we're not done with this group yet
            group.extend(list(line)) # convert `line` to individual characters and append them to the end
        else: # parse the group and reset it after
            group = set(group) # remove duplicates
            total += len(group) # add the amount of questions to `total`
            group = [] # reset the group once we're done with it
    return total

def part2(src):
    total = 0
    # groups are read in like passports from day 4, except they're sets
    group = []
    for line in src:
        if line != "": # we're not done with this group yet
            group.append(set(list(line))) # convert `line` to individual characters and append them as a `set` to the end
        else: # parse the group and reset it after
            # instead of converting to a `set` like in part 1,
            # we have to get the characters all of the sets have in common
            for s in group[1:]: # looping over all of the sets (except the first since we're starting with it)
                # get every set, AKA questions each person answered, and
                # get its intersection against the first person's answers
                # since we're done with `group` after this, we are able to manipulate `group[0]`
                group[0] &= s
            total += len(group[0]) # add the amount of questions everyone answered 'yes' to into `total`
            group = [] # reset the group once we're done with it
    return total

main()
