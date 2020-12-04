import re
def main():
    with open('../inputs/day04', 'r') as f:
        src = [line.strip() for line in f.read().split('\n')]
    print(part1(src))
    print(part2(src))

def part1(src):
    total = 0
    passport = {}
    for line in src:
        if line != "":
            for x in line.split():
                a,b = x.split(":")
                passport[a] = b
        else:
            good = True
            for x in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
                if x not in passport.keys():
                    good = False
            if good:
                total += 1
            passport = {}
    return total

def part2(src):
    total = 0
    passport = {}
    for line in src:
        if line != "":
            for x in line.split():
                a,b = x.split(":")
                passport[a] = b
        else:
            for x in ['byr','iyr','eyr']:
                if x not in passport.keys():
                    passport[x] = -1
            for x in ['hgt','hcl','ecl','pid']:
                if x not in passport.keys():
                    passport[x] = ''
            if 1920 <= int(passport['byr']) <= 2002 and\
                    2010 <= int(passport['iyr']) <= 2020 and\
                    2020 <= int(passport['eyr']) <= 2030 and\
                    (\
                        (passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193) or \
                        (passport['hgt'][-2:] == 'in' and 59  <= int(passport['hgt'][:-2]) <= 76)\
                    ) and\
                    re.match('^\\#[0-9a-f]{6}$', passport['hcl']) and\
                    passport['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'] and\
                    re.match('^[0-9]{9}$', passport['pid']):
                total += 1
            passport = {}
    return total

main()
