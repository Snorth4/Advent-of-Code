def main():
    print("Input:")

    input_data = str(input())
    address_table: list[list[bool]] = [[False for _ in range(10000)] for _ in range(10000)]
    address_table[0][0] = True
    
    santa_i, santa_j = 0, 0
    robot_i, robot_j = 0, 0
    houses_visited = 1
    switch = False
    for c in input_data:

        i, j = 0, 0
        if not switch:
            i, j = santa_i, santa_j
        elif switch:
            i, j = robot_i, robot_j

        match c:
            case ">":
                i += 1
            case "<":
                i -= 1
            case "^":
                j += 1
            case "v":
                j -= 1
                
        if not switch:
            santa_i, santa_j = i, j
        elif switch:
            robot_i, robot_j = i, j

        if not address_table[i][j]:
            address_table[i][j] = True
            houses_visited += 1
        switch = not switch

    print(f"Number of houses visited = {houses_visited}")

if __name__ == "__main__":
    main()
