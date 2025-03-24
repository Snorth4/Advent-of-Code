def get_coords() -> tuple[int, int]:
    return 

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

    lights: list[list[bool]] = [[False for _ in range(1000)] for _ in range(1000)]
    num_lit_lights = 0

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
                    lights[i][j] = not lights[i][j]
                    num_lit_lights += (-1) + (2 * lights[i][j])

                elif operation == "on" and lights[i][j] == False:
                    lights[i][j] = True
                    num_lit_lights += 1

                elif operation == "off" and lights[i][j] == True:
                    lights[i][j] = False
                    num_lit_lights -= 1

    print(f"Number of lit lights: {num_lit_lights}")

if __name__ == "__main__":
    main()
