def look_and_say_sequence(string: str) -> str:

    prev, curr, next = "", "", ""
    symbol_counter: int = 0
    sequence: str = ""
    n = len(string)

    for i in range(n):
        prev = string[i-1:i]
        curr = string[i:i+1]
        next = string[i+1:i+2]

        if i == 0:
            prev == ""
        if i == n - 1:
            next == ""
        
        if   prev == curr == next:
            symbol_counter += 1

        elif prev == curr != next:
            symbol_counter += 1
            sequence = f"{sequence}{symbol_counter}{curr}"
            
        elif prev != curr == next:
            symbol_counter = 1

        elif prev != curr != next:
            symbol_counter = 1
            sequence = f"{sequence}{symbol_counter}{curr}"

    return sequence
        

def main():
    print("Input:")

    number = str(input())
    num_iterations = 40

    for _ in range(num_iterations):
        number = look_and_say_sequence(number)

    print(f"Length of {num_iterations} iterations: {len(number)}")

if __name__ == "__main__":
    main()
