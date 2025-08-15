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
    
    curr_list: list[list[int]] = [molecule_tok]
    curr_list_n_steps: list[int] = [0]
    
    while curr_list:
        
        print(len(curr_list))
        
        next_list: list[list[int]] = []
        next_list_n_steps: list[int] = []

        ### Iterate through each molecule in this iteration of the list...
        for i in range(len(curr_list)):
            curr_molecule: list[int] = curr_list[i]
        
            ### Iterate through each element in this instance of the molecule... 
            for j in range(len(curr_molecule)):

                ### Iterate through each element...
                for element in replacements:

                    ### Iterate through each elemental replacement for the ith element...
                    for replacement in replacements[element]:
                        n = len(replacement)
                        
                        ### If this is a valid replacement, try the replacement...
                        if curr_molecule[j:j+n] == replacement:
                            temp_molecule = molecule_tok.copy()

                            ### Remove all elements that can be removed relating to the current replacement...
                            for _ in range(n):
                                temp_molecule.pop(j)

                            ### If the molecule still has elements in it, create the next iteration of the list...
                            if len(temp_molecule) > 0:
                                temp_molecule.insert(j, element)
                                next_list.append(temp_molecule)
                                next_list_n_steps.append(curr_list_n_steps[i] + 1)
        
        curr_list = next_list
        curr_list_n_steps = next_list_n_steps

    print(f"Total molecules from molecule: {len(molecules_str)}")
    print(f"Unique molecules from molecule: {len(set(molecules_str))}")
    print(f"Molecule was attained in {min(curr_list_n_steps)} steps.")

if __name__ == "__main__":
    main()
