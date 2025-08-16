def tokenize_molecule(molecule_str: str) -> list[int]:
    molecule_tok: list[int] = []

    n: int = len(molecule_str)
    i: int = 0
    while i < n:
        if i < n:
            if molecule_str[i].isupper():
                element_str: str = ""

                if i+1 < n and molecule_str[i+1].islower():
                    element_str = molecule_str[i:i+2]
                    i += 2
                else: 
                    element_str = molecule_str[i:i+1]
                    i += 1
                
                if element_str not in encoding:
                    encoding[element_str] = max(encoding.values()) + 1
                    decoding[max(decoding.keys()) + 1] = element_str

                molecule_tok.append(encoding[element_str])

        else:
            break
    
    return molecule_tok

def untokenize_molecule(molecule_tok: list[int]) -> str:
    molecule_str: str = ""
    for element_int in molecule_tok:
        molecule_str = ''.join([molecule_str, decoding[element_int]])

    return molecule_str

def untokenize_molecules(molecules_tok: list[list[int]]) -> list[str]:
    molecules_str: list[str] = []

    for molecule_tok in molecules_tok:
        molecules_str.append(untokenize_molecule(molecule_tok))
    
    return molecules_str

encoding: dict[str, int] = {}
decoding: dict[int, str] = {}

def main():

    ### Process the input...

    print("Input:")

    lines: list[list[str]] = []
    molecule_str: str = ""
    is_replacement = True
    while True:
        try:
            line = input().strip()

            if is_replacement == True:
                if line == "":
                    is_replacement = False
                else:
                    lines.append(line.split())
            elif line != "" and is_replacement == False:
                molecule_str = line
                break

        except EOFError:
            break
    del is_replacement

    lines = [x for x in lines if x]

    print()

    ### Create a dict of an integer encoding and decoding of the elements...

    global encoding, decoding

    j: int = 0
    for element in sorted(set([line[0] for line in lines])):
        encoding[element] = j
        j += 1
    del j

    decoding = {value: key for key, value in encoding.items()}

    print(f"Encoding:\n{encoding}\n")
    
    print(f"Decoding:\n{decoding}\n")

    ### Create a dictionary of elements to their replacements using their element encodings...
    
    replacements: dict[int, list[list[int]]] = {}
    for line in lines:
        element = encoding[line[0]]
        replacement = tokenize_molecule(line[2])

        if element not in replacements:
            replacements[element] = []
        
        replacements[element].append(replacement)
    del lines

    print(f"Replacements (tokenized):\n{replacements}\n")

    ### Encode the input molecule...

    molecule_tok = tokenize_molecule(molecule_str)

    print(f"Molecule (tokenized):\n{molecule_tok}\n")

    ### Part 1: Process all possible combinations of the molecule given the replacements in a tokenized format...

    molecules_tok: list[list[int]] = []
    for j in range(len(molecule_tok)):

        new_molecule_by_index: list[int] = molecule_tok.copy()
        element = new_molecule_by_index.pop(j)

        if element in replacements:
            for replacement in replacements[element]:
                new_molecule = new_molecule_by_index.copy()
                for element in reversed(replacement):
                    new_molecule.insert(j, element)
                molecules_tok.append(new_molecule)

    ### Untokenize the list...

    molecules_str: list[str] = untokenize_molecules(molecules_tok)

    ### Part 2: Reverse engineer the molecule in the fewest number of steps by using a recursive function.
    
    ### Use a prebuilt tree of the elements?
    
    import copy, time
    
    start_time = time.time()
    
    class Molecule_Object:
        def __init__(self, 
                     molecule: list[int] = [], 
                     n_steps: int = 0):

            self.molecule = molecule
            self.n_steps = n_steps
        
        def increment(self):
            self.n_steps = self.n_steps + 1
    
    curr_list: list[Molecule_Object] = [Molecule_Object(molecule_tok, 0)]
    
    min_n_steps: int = 999999999999
    
    while curr_list:
        
        instance_start_time = time.time()
        
        total_len: int = 0
        for mole_obj in curr_list:
            total_len += len(mole_obj.molecule)
                
        next_list: list[Molecule_Object] = []

        ### Iterate through each molecule in this iteration of the list...
        for mole_obj in curr_list:
            
            ### Iterate through each element in this instance of the molecule...
            for j in range(len(mole_obj.molecule)):

                ### Iterate through each element...
                for element in replacements:

                    ### Iterate through each elemental replacement for the ith element...
                    for replacement in replacements[element]:
                        n = len(replacement)
                        
                        ### If this is a valid replacement, try the replacement...
                        if mole_obj.molecule[j:j+n] == replacement:
                            temp_obj = copy.deepcopy(mole_obj)

                            ### Remove all elements that can be removed relating to the current replacement...
                            for _ in range(n):
                                temp_obj.molecule.pop(j)

                            temp_obj.molecule.insert(j, element)
                            temp_obj.increment()
                            
                            if len(temp_obj.molecule) == 1 and temp_obj.molecule[0] == encoding['e'] and mole_obj.n_steps < min_n_steps:
                                min_n_steps = temp_obj.n_steps
                            
                            next_list.append(temp_obj)
                            
                        ### If this is not a valid replacement, do nothing...
                        else:
                            ...
                            
        print(f"Instance runtime: {(((time.time() - instance_start_time)*1000) // 10) / 100:.2f}s, Avg length: {total_len // len(curr_list)}, Instances in list: {len(curr_list)}, Total elements: {total_len}")
        
        curr_list = copy.deepcopy(next_list)
        
    print()
    print(f"Total molecules from molecule: {len(molecules_str)}")
    print(f"Unique molecules from molecule: {len(set(molecules_str))}")
    print()
    print(f"Molecule was attained in {min_n_steps} steps and in {(((time.time() - start_time)*1000) // 10) / 100:.2f} seconds")
    print()

if __name__ == "__main__":
    main()
