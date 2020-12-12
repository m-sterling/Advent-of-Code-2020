def main():
    with open('../inputs/day12', 'r') as f:
        src = [line.strip() for line in f.read().split('\n') if line]
    print(part1(src))
    print(part2(src))

def part1(src):
    # ship x, ship y: east/south = positive, west/north = negative 
    # ship direction: N = 0, E = 1, S = 2, W = 3
    x, y, d = 0, 0, 1
    for line in src:
        # separate the instruction from the value
        letter = line[0]
        number = int(line[1:])
        
        # N/S/E/W are direct coordinate translations
        if letter == 'N':
            y -= number
        elif letter == 'S':
            y += number
        elif letter == 'E':
            x += number
        elif letter == 'W':
            x -= number
        # L/R rotate the ship; 90deg clockwise = one direction increase
        #   also, Python always makes negative numbers positive when used as the dividend
        elif letter == 'L':
            d -= int(number / 90) % 4
        elif letter == 'R':
            d += int(number / 90) % 4
        # use the direction to move that way
        elif letter == 'F':
            if d%4 == 0:
                y -= number
            elif d%4 == 1:
                x += number
            elif d%4 == 2:
                y += number
            elif d%4 == 3:
                x -= number
    # Manhattan distance = absolute value of x plus absolute value of y
    return abs(x) + abs(y)

def part2(src):
    # ship x and y - signs are the same as in part 1 
    sx, sy = 0, 0
    # waypoint x and y - again, signs are same
    wx, wy = 10, -1
    for line in src:
        letter = line[0]
        number = int(line[1:])
        
        # these four remain unchanged, though they affect the waypoint instead
        if letter == 'N':
            wy -= number
        elif letter == 'S':
            wy += number
        elif letter == 'E':
            wx += number
        elif letter == 'W':
            wx -= number
        # L/R rotates the waypoint around the ship; rotating clockwise = swapping x/y and swapping sign of the new y
        elif letter == 'L':
            for i in range(int(number / 90) % 4):
                wx, wy = wy, -wx
        elif letter == 'R':
            for i in range(int(number / 90) % 4):
                wx, wy = -wy, wx
        # F teleports the ship to the waypoint's position `number` times
        elif letter == 'F':
            sx += wx*number
            sy += wy*number
    # again, get Manhattan distance
    return abs(sx) + abs(sy)

main()
