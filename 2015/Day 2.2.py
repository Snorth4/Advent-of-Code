from typing import List

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
        edges: List[int] = [edge1, edge2, edge3]
        smallest_edge = min(edges)
        edges.remove(smallest_edge)
        second_smallest_edge = min(edges)
        total_area += 2 * (smallest_edge + second_smallest_edge) + edge1 * edge2 * edge3
    
    print(f"Total area of wrapping paper to get: {total_area}")

if __name__ == "__main__":
    main()
