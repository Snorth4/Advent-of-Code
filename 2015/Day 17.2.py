import numpy as np

def num_combinations(containers: np.ndarray, size: int, curr_num: int = 0):
    global num_min_combs, min_num
    
    if size == 0:
        if curr_num == min_num:
            num_min_combs += 1
        elif curr_num < min_num:
            min_num = curr_num
            num_min_combs = 1
            
    elif size > 0:
        if containers.size > 0:
            for i in range(containers.size):
                num_combinations(containers[i+1:], size - containers[i], curr_num + 1)

min_num: int = 999999
num_min_combs: int = 0

TOTAL_EGGNOG: int = 150

def main():
    global num_min_combs, min_num
    
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
    
    num_combinations(containers, TOTAL_EGGNOG)
    
    print(f"There are {num_min_combs} combinations for the minimum number ({min_num}) of containers.")
    
if __name__ == "__main__":
    main()
