def main():
    with open('../inputs/day09', 'r') as f:
        # cast each line to an int for quicker parsing later
        src = [int(line.strip()) for line in f.read().split('\n') if line]
    print(part1(src))
    print(part2(src))

def part1(src):
    for i in range(len(src) - 25):
        # read the last 25 numbers
        last = src[i:i+25]
        # and the number after this grouping
        next_num = src[i+25]
        
        # if we find a sum of two numbers that equals the next number, that's
        # not what we're looking for, so `found` is a sort of sentinel value
        found = False
        # do a double loop similar to that in day 1
        for a in range(len(last)):
            for b in range(a+1, len(last)):
                if last[a] + last[b] == next_num:
                    # these two numbers add up to the next number, so we
                    #   trip the sentinel and bail out of this grouping
                    found = True
                    break
            # looking back, for/else would have been more
            #   Pythonic, but if it works, it works, right?
            if found:
                break
        # if we don't find two numbers in the last group that add
        #   up to the next number, we can return it as the answer
        if not found:
            return next_num
    
    # just in case, keep the fallback as always
    return -1

def part2(src):
    # the first for loop is exactly the same as in part 1
    invalid_num = -1
    for i in range(len(src) - 25):
        last = src[i:i+25]
        next_num = src[i+25]
        
        found = False
        for a in range(len(last)):
            for b in range(a+1, len(last)):
                if last[a] + last[b] == next_num:
                    found = True
                    break
            if found:
                break
        if not found:
            # except here! we capture the next_num in a variable instead of
            #   returning it, since we still have to use it further
            invalid_num = next_num
            break
    # now we need to do another double for loop, but instead of them being the indices
    #   of two numbers in the range, they become the start and end of the range instead
    for i in range(len(src)):
        for j in range(i+1,len(src)+1):
            # take the range specified by i and j
            contiguous = src[i:j]
            # and sum it up, seeing if it equals to invalid_num
            if sum(contiguous) == invalid_num:
                # if so, return the sum of the min and max values
                return min(contiguous) + max(contiguous)
            # added by Tom from The Coding Den: if the sum is greater than the invalid_num,
            #   we can forget about the starting index because the sum will only grow bigger
            elif sum(contiguous) > invalid_num:
                break
            
    return -1

main()
