import re
def main():
    with open('../inputs/day08', 'r') as f:
        src = [line.strip() for line in f.read().split('\n') if line]
    print(part1(src))
    print(part2(src))

def part1(src):
    # `acc` starts at zero and has no influence on pointer
    # `ptr` determines which instruction to execute
    # `seen` keeps track of which lines we've executed to detect an infinite loop
    acc = 0
    ptr = 0
    seen = []
    # keep looping until we find a point we were at before
    while ptr not in seen:
        # track this line for next time
        seen.append(ptr)

        # parse the line for interpretation
        words = src[ptr].split()
        inst = words[0]
        arg = int(words[1])
        
        if inst == 'nop':   # does nothing - no operation
            ptr += 1
        elif inst == 'acc': # adds to the accumulator and moves on
            acc += arg
            ptr += 1
        elif inst == 'jmp': # moves the pointer by `arg` lines
            ptr += arg
    # once the infinite loop is found, the loop is exited and we can return the value
    return acc

def part2(src):
    nops = [i for i in range(len(src)) if src[i].startswith('nop')]
    jmps = [i for i in range(len(src)) if src[i].startswith('jmp')]
    # one `nop` or `jmp` should be switched - loop through each changing
    # one each iteration to find which change fixes the infinite loop
    for nop_i in nops:
        # same as above
        acc = 0
        ptr = 0
        seen = []
        
        # adding that the loop should break when the pointer is OOB
        while ptr not in seen and ptr < len(src):
            seen.append(ptr)

            words = src[ptr].split()
            # if this line is the `nop` we're looking to change, intercept and swap it out
            inst = 'jmp' if ptr == nop_i else words[0]
            arg = int(words[1])
            
            # continue as normal
            if inst == 'nop':
                ptr += 1
            elif inst == 'acc':
                acc += arg
                ptr += 1
            elif inst == 'jmp':
                ptr += arg
        # if the loop was exited due to the pointer being OOB, the infinite loop was broken!
        if ptr >= len(src):
            return acc

    # exact same as the above loop, except nop -> jmp becomes jmp -> nop
    for jmp_i in jmps:
        acc = 0
        ptr = 0
        seen = []
        while ptr not in seen and ptr < len(src):
            seen.append(ptr)

            words = src[ptr].split()
            inst = 'nop' if ptr == jmp_i else words[0]
            arg = int(words[1])
        
            if inst == 'nop':
                ptr += 1
            elif inst == 'acc':
                acc += arg
                ptr += 1
            elif inst == 'jmp':
                ptr += arg
        if ptr >= len(src):
            return acc
    
    # failsafe - should theoretically never happen
    return -1

main()
