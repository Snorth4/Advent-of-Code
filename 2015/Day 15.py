import numpy as np

def calculate_score(ingredients: np.ndarray, num_tspns: np.ndarray, calories: int | None) -> int:
    
    # Matrix multiplication
    props_scores = np.dot(num_tspns, ingredients)
    del ingredients, num_tspns
    
    # Any negatives or zeroes force-return zero
    for prop_score in props_scores[:-2]:
        if prop_score <= 0:
            return 0
    
    if calories != None and props_scores[4] != calories:
        return 0
    
    # Myltiply properties
    total_score = props_scores[0] * props_scores[1] * props_scores[2] * props_scores[3]
    
    return total_score

# Returns the next valid number of teaspoons (coefficient) for each ingredient.
# Returns True for the second value if we've covered all combinations of each ingredients' coefficients.
def next_valid_num_tspns(num_tspns: np.ndarray) -> tuple[np.ndarray, bool]:
    n = len(num_tspns)
    
###########################################

    valid: bool = False
    while not valid:
        for i in range(n):
            if num_tspns[i] < 100:
                num_tspns[i] += 1
                break
            elif num_tspns[i] == 100:
                if i+1 < n:
                    num_tspns[i] = 0
                elif i+1 >= n:
                    return num_tspns, True
        
        if np.sum(num_tspns) == 100:
            valid = True
    
###########################################
#    
#    for i in range(n):
#        if num_tspns[i] == 0:
#            ...
#        elif num_tspns[i] < 100:
#            num_tspns[i] += 1
#            num_tspns
#            break
#        elif num_tspns[i] == 100:
#            if i+1 < n:
#                num_tspns[i] = 0
#            elif i+1 >= n:
#                return num_tspns, True
#        
###########################################
    
    return num_tspns, False

def main():
    print("Input:")
    
    tokens: list[list[str]] = [[]]
    while True:
        try:
            token = input()
            if token.strip() == "":
                break
            
            tokens.append(token.split(" "))
        except EOFError:
            break

    tokens = [x for x in tokens if x]
    n = len(tokens)
    
    ingredients: np.ndarray = np.empty((n, 5), dtype=int)
    num_tspns = np.zeros(n, dtype=int)
    
    for i in range(n):
        ingredients[i] = [int(tokens[i][2][:-1]),
                          int(tokens[i][4][:-1]),
                          int(tokens[i][6][:-1]),
                          int(tokens[i][8][:-1]),
                          int(tokens[i][10])]
    del tokens
    
    print("Input an int for the target number of calories (empty for no target):")
    calories_str = input()
    calories = 0
    if calories_str.strip() == "":
        calories = None
    else:
        calories = int(calories_str.strip())
            
    # Do excess calculations...
    maximum_score = 0
    finished: bool = False
    while not finished:
        num_tspns, finished = next_valid_num_tspns(num_tspns)
        score = calculate_score(ingredients, num_tspns, calories)
        
        if score > maximum_score:
            maximum_score = score
    
    print(f"Maximum score: {maximum_score}")
    
if __name__ == "__main__":
    main()
