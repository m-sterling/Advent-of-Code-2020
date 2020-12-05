# thank you to Maia on the TCD Discord server for helping me
# understand a much better (and actually working) ID parsing system!!
def main():
    with open('../inputs/day05', 'r') as f:
        src = [line.strip() for line in f.readlines()]
    print(part1(src))
    print(part2(src))

def part1(src):
    ids = []
    for line in src:
        # each line in the input contains seven occurrences of 
        #   "F" and "B" followed by three occurrences of "L" and "R" 
        # the former letters correspond to 0 in binary, while the latter correspond to 1
        # replacing these letters with the bit values they symbolise yields
        #   a binary number, which we then convert from base 2 to 10
        _id = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
        ids.append(int(_id, 2))
    # then return the highest ID
    return max(ids)

def part2(src):
    ids = []
    for line in src:
        # parsing is the same as in part 1 - nothing to comment about here
        _id = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
        ids.append(int(_id,2))
    
    # our seat is missing in the list, but the seat IDs before and after it are present
    for i in range(min(ids), max(ids)+1):
        # therefore, we can just loop over all IDs and find the one that isn't present but 
        #   the ones before and after it are - very straightforward
        if i not in ids and i-1 in ids and i+1 in ids:
            return i
    return -1

main()
