def main():
    print("Input:")

    input_data = str(input())
    counter = 0
    for c in input_data:
        if c == "(":
            counter += 1
        elif c == ")":
            counter -= 1
    print(f"Floor = {counter}")

if __name__ == "__main__":
    main()
