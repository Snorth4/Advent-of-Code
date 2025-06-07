import numpy as np

def num_combinations(containers: np.ndarray, size: int) -> int:
    n_comb = 0
    if size == 0:
        return 1
    elif size > 0:
        if containers.size <= 0:
            return 0
        elif containers.size > 0:
            for i in range(containers.size):
                n_comb += num_combinations(containers[i+1:], size - containers[i])
                
    return n_comb

TOTAL_EGGNOG: int = 150

def main():
    print("Input:")
    
    lines: list[int] = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            
            lines.append(int(line))
        except EOFError:
            break

    lines = [x for x in lines if x]
    
    # Flatten the list of lists and convert each string to int.
    containers = np.array(lines, dtype=int)
    
    # Sort the array in decreasing order.
    containers = np.flip(np.sort(containers))
    
    print(f"There are {num_combinations(containers, TOTAL_EGGNOG)} combinations of the containers.")
    
if __name__ == "__main__":
    main()
