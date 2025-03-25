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
        num_extra += 2
        num_literal += n
        last_signifier: int = -5

        for i in range(1, n-1):

            if last_signifier == -1:
                num_extra += 1

            elif last_signifier == -2:

                if string[i-1] == "x":
                    num_extra += 1

                else:
                    if string[i] == "\\":
                        last_signifier = 0
                    num_memory += 1

            elif last_signifier == -3:

                if string[i-2] == "x":
                    num_extra += 1

                else:
                    if string[i] == "\\":
                        last_signifier = 0
                    num_memory += 1
                    
            elif last_signifier <= -4:
                
                if string[i] == "\\":
                    last_signifier = 0
                num_memory += 1

            else:
                num_memory += 1
            
            last_signifier -= 1

    print(f"Num chars literal: {num_literal}")
    print(f"Num chars memory: {num_memory}")
    print(f"Num chars extra: {num_extra}")

if __name__ == "__main__":
    main()
