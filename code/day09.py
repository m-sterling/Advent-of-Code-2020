def main():
    with open('../inputs/day09', 'r') as f:
        src = [int(line.strip()) for line in f.read().split('\n') if line]
    print(part1(src))
    print(part2(src))

def part1(src):
    for i in range(len(src) - 25):
        last = list(map(int, src[i:i+25]))
        next_num = int(src[i+25])
        
        found = False
        for a in range(len(last)):
            for b in range(a+1, len(last)):
                if last[a] + last[b] == next_num:
                    found = True
                    break
            if found:
                break
        if not found:
            return next_num

    return -1

def part2(src):
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
            invalid_num = next_num
            break
    for i in range(len(src)):
       for j in range(i+1,len(src)+1):
            contiguous = src[i:j]
            if sum(contiguous) == invalid_num:
                return min(contiguous) + max(contiguous)
            
    return -1

main()
