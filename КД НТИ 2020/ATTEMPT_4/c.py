def conn_gears(gear):
    gear_connwith = []
    for conn in connections:
        if gear in conn:
            gear_connwith.append(conn[-(conn.index(gear)-1)])
    return gear_connwith

def move(drive_gear):
    for gear in conn_gears(drive_gear):
        if gears_state[gear] == -1:
            gears_state[gear] = not(gears_state[drive_gear])
        elif gears_state[gear] == gears_state[drive_gear] and gears_state[gear] != -1:
            print("bad")
            quit()

n = int(input())
gears_state = [-1  for i in range(n)]
gears_state[0] = True

m = int(input())
connections = []
for i in range(m):
    inp = [int(i) - 1 for i in input().split()]
    connections.append(inp)

def main():
    follower_gears = []
    passed_gears = []
    motor_gear = 0

    move(motor_gear)
    passed_gears.append(motor_gear)
    for i in range(1, n):
        if gears_state[i] != -1 and i not in passed_gears:
            follower_gears.append(i)
    counter = 0
    while follower_gears != []:
        counter += 1
        gear = follower_gears[0]
        move(gear)
        passed_gears.append(gear)
        follower_gears.remove(i)
        for i in range(1, n):
            if gears_state[i] != -1 and i not in passed_gears:
                follower_gears.append(i)
                print("[DEBUG]", follower_gears)
                print("[DEBUG]pas", passed_gears)
        if counter == 3:
            quit()

    print("good")

if __name__ == '__main__':
    main()




            


