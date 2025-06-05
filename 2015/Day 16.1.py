import numpy as np

class AuntSue:
    def __init__(self, 
                 children:    int | None = None, 
                 cats:        int | None = None, 
                 samoyeds:    int | None = None, 
                 pomeranians: int | None = None, 
                 akitas:      int | None = None, 
                 vizslas:     int | None = None, 
                 goldfish:    int | None = None, 
                 trees:       int | None = None, 
                 cars:        int | None = None, 
                 perfumes:    int | None = None):
        
        self.children    = children
        self.cats        = cats
        self.samoyeds    = samoyeds
        self.pomeranians = pomeranians
        self.akitas      = akitas
        self.vizslas     = vizslas
        self.goldfish    = goldfish
        self.trees       = trees
        self.cars        = cars
        self.perfumes    = perfumes

n_aunt_sues: int = 500

def main():
    print("Input:")
    
    lines: list[list[str]] = [[]]
    while True:
        try:
            tokens = input()
            if tokens.strip() == "":
                break
            
            lines.append(tokens.split(" "))
        except EOFError:
            break

    lines = [x for x in lines if x]
    
    aunt_sues = np.array([AuntSue() for _ in range(n_aunt_sues)], dtype=AuntSue)
    
    for tokens in lines:
        index = int(tokens[1][:-1]) - 1
        n_items = (len(tokens) - 2) // 2
        
        for i in range(n_items):
            
            name = str(tokens[i*2+2][:-1])
            
            value = None
            if i+1 < n_items:
                value = int(tokens[i*2+3][:-1])
            elif i+1 == n_items:
                value = int(tokens[i*2+3])
            
            match name:
                case "children":    aunt_sues[index].children    = value
                case "cats":        aunt_sues[index].cats        = value
                case "samoyeds":    aunt_sues[index].samoyeds    = value
                case "pomeranians": aunt_sues[index].pomeranians = value
                case "akitas":      aunt_sues[index].akitas      = value
                case "vizslas":     aunt_sues[index].vizslas     = value
                case "goldfish":    aunt_sues[index].goldfish    = value
                case "trees":       aunt_sues[index].trees       = value
                case "cars":        aunt_sues[index].cars        = value
                case "perfumes":    aunt_sues[index].perfumes    = value
    del lines
    
    target_aunt_sue = AuntSue(children = 3, 
                              cats = 7, 
                              samoyeds = 2, 
                              pomeranians = 3, 
                              akitas = 0, 
                              vizslas = 0, 
                              goldfish = 5, 
                              trees = 3, 
                              cars = 2, 
                              perfumes = 1)
    
    gift_giver_index: int = -1
    for i in range(n_aunt_sues):
        aunt_sue = aunt_sues[i]
        if ((aunt_sue.children    is None or aunt_sue.children    == target_aunt_sue.children)    and 
            (aunt_sue.cats        is None or aunt_sue.cats        == target_aunt_sue.cats)        and 
            (aunt_sue.samoyeds    is None or aunt_sue.samoyeds    == target_aunt_sue.samoyeds)    and 
            (aunt_sue.pomeranians is None or aunt_sue.pomeranians == target_aunt_sue.pomeranians) and 
            (aunt_sue.akitas      is None or aunt_sue.akitas      == target_aunt_sue.akitas)      and 
            (aunt_sue.vizslas     is None or aunt_sue.vizslas     == target_aunt_sue.vizslas)     and 
            (aunt_sue.goldfish    is None or aunt_sue.goldfish    == target_aunt_sue.goldfish)    and 
            (aunt_sue.trees       is None or aunt_sue.trees       == target_aunt_sue.trees)       and 
            (aunt_sue.cars        is None or aunt_sue.cars        == target_aunt_sue.cars)        and 
            (aunt_sue.perfumes    is None or aunt_sue.perfumes    == target_aunt_sue.perfumes)):
        
            gift_giver_index = i
    
    print(f"Sue {gift_giver_index+1} gave the gift.\n")
    
if __name__ == "__main__":
    main()
