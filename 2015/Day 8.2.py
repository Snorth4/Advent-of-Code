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

    num_literal = 0
    num_memory = 0
    num_extra = 0

    for string in strings:
        n = len(string)
        num_literal += 2
        num_extra += 2

        for c in string:
            if c is "\\" or c is "\"":
                num_literal += 2
                num_memory += 1
                num_extra += 1

            else:
                num_literal += 1
                num_memory += 1



    print(f"Num chars literal: {num_literal}")
    print(f"Num chars memory: {num_memory}")
    print(f"Num chars extra: {num_extra}")

if __name__ == "__main__":
    main()
