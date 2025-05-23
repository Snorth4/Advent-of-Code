def main():
    print("Input:")

    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        except EOFError:
            break

    total_area = 0
    for line in lines:
        edge1, edge2, edge3 = line.split("x")
        edge1, edge2, edge3 = int(edge1), int(edge2), int(edge3)
        side1 = edge1 * edge2
        side2 = edge1 * edge3
        side3 = edge2 * edge3
        smallest_side = min(side1, side2, side3)
        total_area += 2 * (side1 + side2 + side3) + smallest_side
    
    print(f"Total area of wrapping paper to get: {total_area}")

if __name__ == "__main__":
    main()
