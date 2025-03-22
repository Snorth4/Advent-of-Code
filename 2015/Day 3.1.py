def main():
    print("Input:")

    input_data = str(input())
    address_table: list[list[bool]] = [[False for _ in range(10000)] for _ in range(10000)]
    address_table[0][0] = True
    
    i, j = 0, 0
    houses_visited = 1
    for c in input_data:
        match c:
            case ">":
                i += 1
            case "<":
                i -= 1
            case "^":
                j += 1
            case "v":
                j -= 1
        if not address_table[i][j]:
            address_table[i][j] = True
            houses_visited += 1

    print(f"Number of houses visited = {houses_visited}")

if __name__ == "__main__":
    main()
