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
        prev_char: str = None
        num_vowels: int = 0
        naughty: bool = False
        contains_double_chars: bool = False
        for curr_char in string:
            substring = f"{prev_char}{curr_char}"

            if substring == "ab" or substring == "cd" or substring == "pq" or substring == "xy":
                num_naughty += 1
                naughty = True
                break

            if curr_char == "a" or curr_char == "e" or curr_char == "i" or curr_char == "o" or curr_char == "u":
                num_vowels += 1

            if curr_char == prev_char:
                contains_double_chars = True

            prev_char = curr_char

        if num_vowels >= 3 and contains_double_chars and not naughty:
            num_nice += 1
        else:
            num_naughty += 1
        
    print(f"Number of nice strings: {num_nice}")

if __name__ == "__main__":
    main()
