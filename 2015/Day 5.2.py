def main():
    print("Input:")
    
    strings = []
    while True:
        try:
            string = input()
            if string.strip() == "":
                break
            strings.append(string)
        except EOFError:
            break

    num_nice = 0
    num_naughty = 0

    for string in strings:

        contains_twin_pairs = False
        contains_char_sandwich = False
        n = len(string)

        for i in range(n):
            curr_char = string[i:i+1]
            next_next_char = string[i+2:i+3]
            substring = string[i:i+2]

            if not contains_twin_pairs:
                for j in range(i+2, n-1):
                    other_substring = string[j:j+2]
                    if substring == other_substring:
                        contains_twin_pairs = True
            
            if curr_char == next_next_char:
                contains_char_sandwich = True

        if contains_twin_pairs and contains_char_sandwich:
            num_nice += 1
        else:
            num_naughty += 1
        
    print(f"Number of nice strings: {num_nice}")

if __name__ == "__main__":
    main()
