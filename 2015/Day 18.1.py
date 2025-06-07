import numpy as np

def main():
    print("Input:")
    
    lines: list[str] = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            
            lines.append(line)
        except EOFError:
            break

    lines = [x for x in lines if x]
    length = len(lines[0])
    height = len(lines)
    
    grid = np.zeros((height, length), dtype=int)
    for i in range(height):
        for j in range(length):
            if lines[i][j] == '#':
                grid[i][j] = 1
    
    n_steps = 100
    for _ in range(n_steps):
        
        next_grid = grid.copy()
        for i in range(height):
            for j in range(length):
                
                n_neighbors_on = 0
                for ii in (i-1, i, i+1):
                    for jj in (j-1, j, j+1):
                        
                        if ((ii != i or jj != j) and 
                            ii >= 0 and 
                            jj >= 0 and 
                            ii < height and 
                            jj < length and 
                            grid[ii][jj] == 1):
                            n_neighbors_on += 1
                
                if grid[i][j] == 0 and n_neighbors_on == 3:
                    next_grid[i][j] = 1
                elif grid[i][j] == 1 and n_neighbors_on != 2 and n_neighbors_on != 3:
                    next_grid[i][j] = 0
        
        grid = next_grid
    
    print(f"\n{grid}\n")
    
    total_lights_on = grid.sum(axis=-1).sum(axis=-1)

    print(f"{total_lights_on} lights are on after {n_steps} step{'' if n_steps == 1 else 's'}.")
    
if __name__ == "__main__":
    main()
