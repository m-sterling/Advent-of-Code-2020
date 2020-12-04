import re
def main():
    with open('../inputs/day04', 'r') as f:
        src = [line.strip() for line in f.read().split('\n')]
    print(part1(src))
    print(part2(src))

def part1(src):
    total = 0
    # passports are just glorified key/value objects
    passport = {}
    for line in src:
        if line != "": # we're not done with this passport yet
            for x in line.split(): # get every key/value pair in this line
                a,b = x.split(":")
                passport[a] = b
        else: # parse the passport and reset it after
            good = True
            for x in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
                if x not in passport.keys():
                    # passport needs all of the above seven keys; `cid` is optional so not checked
                    good = False # looking back, a for/else would make a bit more sense
            if good:
                total += 1
            passport = {} # reset the passport once we're done with it
    return total

def part2(src):
    total = 0
    # same as above, passports are key/value objects
    passport = {}
    for line in src:
        if line != "": # passports are read in the same
            for x in line.split():
                a,b = x.split(":")
                passport[a] = b
        else: # but we parse them differently
            for x in ['byr','iyr','eyr']:
                # birth year, issue year, and expiration year are `int`s
                #   if not present, set to `-1` for nullish value
                if x not in passport.keys():
                    passport[x] = -1
            for x in ['hgt','hcl','ecl','pid']:
                # height, hair colour, eye colour, and passport id are strings
                #   if not present, set to empty string for nullish value
                if x not in passport.keys():
                    passport[x] = ''
            # this could have been done a LOT better.
            # if birth year in range `[1920, 2002]`,
            #   issue year in range `[2010, 2020]`,
            #   expiry year in range `[2020, 2030]`,
            #   height is either
            #     in centimetres and in range `[150, 193]` or
            #     in inches and in range `[59, 76]`,
            #   hair colour is a valid hex code,
            #   eye colour is one of `amb`/`blu`/`brn`/`gry`/`grn`/`hzl`/`oth`, and
            #   passport id is nine digits, including padded zeroes
            #
            # looking back at the code now, the birth/issue/expiry years could have
            # been left as strings and compared to other strings; `'1920' <= '1985' <= '2002'` is `True`
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
