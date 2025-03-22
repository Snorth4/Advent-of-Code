def main():
    print("Input:")

    input_data = str(input())
    counter = 0
    index = 1
    for c in input_data:
        if c == "(":
            counter += 1
        elif c == ")":
            counter -= 1
        index += 1
        if counter <= 0:
            break
    print(f"Index = {index}")

if __name__ == "__main__":
    main()
