import math

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
        dim1, dim2, dim3 = line.split("x")
        dim1, dim2, dim3 = int(dim1), int(dim2), int(dim3)
        side1 = dim1 * dim2
        side2 = dim1 * dim3
        side3 = dim2 * dim3
        smallest_side = min(side1, side2, side3)
        total_area += 2 * (side1 + side2 + side3) + smallest_side
    
    print(f"Total area of wrapping paper to get: {total_area}")

if __name__ == "__main__":
    main()
