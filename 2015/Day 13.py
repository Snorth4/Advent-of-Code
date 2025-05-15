import math
from itertools import permutations
from collections import defaultdict

def main():
    print("Input:")
    
    words: list[list[str]] = [[]]
    while True:
        try:
            word = input()
            if word.strip() == "":
                break
            
            words.append(word.split(" "))
        except EOFError:
            break
    
    words = [x for x in words if x] 
    guest_list: list[str] = []
    happiness_values = defaultdict(dict[str, int])
    
    for i in range(len(words)):
        guest_list.append(words[i][0])
        happiness_values[words[i][0]][words[i][10][:-1]] = int(words[i][3]) * (-1 if words[i][2] == "lose" else 1)
    del words
    
    guest_list = list(set(guest_list))
    guest_list.sort()
    n = len(guest_list)
    
    while True:
        print("Are you seating yourself? (y/n)")
        x = input().lower()
        if x == "y" or x == "yes":
            for guest in guest_list:
                happiness_values["You"][guest] = 0
                happiness_values[guest]["You"] = 0
            guest_list.append("You")
            break
        elif x == "n" or x == "no":
            break
        del x
    
    max_happiness = -float("inf")
    for perm in permutations(guest_list[1:]):
        perm = list(perm)
        perm.insert(0, guest_list[0])
        
        happiness = 0
        for i in range(n):
            happiness += happiness_values[perm[i-1]][perm[i]]
            happiness += happiness_values[perm[i]][perm[i-1]]
        if happiness > max_happiness:
            max_happiness = happiness
    
    print(f"Maximum happiness: {max_happiness}")
        
if __name__ == "__main__":
    main()
