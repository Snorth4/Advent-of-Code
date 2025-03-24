def main():
    print("Input:")
    
    instructions = []
    while True:
        try:
            instruction = input()
            if instruction.strip() == "":
                break
            
            instructions.append(instruction)
        except EOFError:
            break

    lights: list[list[bool]] = [[0 for _ in range(1000)] for _ in range(1000)]
    total_brightness = 0

    for instruction in instructions:
        if instruction[0:4] == "turn":
            _, operation, coord_one, _, coord_two = instruction.split(" ")
        else:
            operation, coord_one, _, coord_two = instruction.split(" ")
        
        bottom, left = coord_one.split(",")
        top, right = coord_two.split(",")
        top, bottom, left, right = int(top), int(bottom), int(left), int(right)

        for i in range(bottom, top+1):
            for j in range(left, right+1):

                if operation == "toggle":
                    lights[i][j] += 2
                    total_brightness += 2

                elif operation == "on":
                    lights[i][j] += 1
                    total_brightness += 1

                elif operation == "off" and lights[i][j] > 0:
                    lights[i][j] -= 1
                    total_brightness -= 1

    print(f"Total brightness: {total_brightness}")

if __name__ == "__main__":
    main()
