def increment(string: list[chr]) -> list[chr]:

    remainder = False
    for i in range(1, len(string)+1):
        if string[-i] != 'z':
            string[-i] = chr(ord(string[-i]) + 1)
            remainder = False
        elif string[-i] == 'z':
            string[-i] = 'a'
            remainder = True

        if remainder == False:
            break
        elif remainder == True and i == len(string):
            string.insert(0, 'a')
    
    return string

def main():
    print("Input:")

    password: list[chr] = list(input())

    valid_password = False
    while not valid_password:
        password: list[chr] = increment(password)

        contains_illegal_character = False
        contains_sequential_staircase = False
        contains_one_pair_twins = False
        contains_two_pair_twins = False

        prev_prev_char: chr = None
        prev_char: chr = None
        
        for curr_char in password:

            if curr_char == 'i' or curr_char == 'o' or curr_char == 'l':
                contains_illegal_character = True
                break

            if (not contains_sequential_staircase 
                    and prev_prev_char is not None 
                    and prev_char is not None 
                    and curr_char is not None 
                    and ord(prev_prev_char) == ord(prev_char) - 1 == ord(curr_char) - 2):
                contains_sequential_staircase = True

            if (contains_one_pair_twins
                    and prev_char is not None
                    and curr_char is not None
                    and prev_char == curr_char):
                contains_two_pair_twins = True
                
            if (not contains_one_pair_twins 
                    and prev_prev_char is not None 
                    and prev_char is not None 
                    and prev_prev_char == prev_char):
                contains_one_pair_twins = True

            prev_prev_char = prev_char
            prev_char = curr_char
            
            # For debugging purposes
            # print(f"password: {''.join(password)}, staircase: {contains_sequential_staircase}, twins: {contains_two_pair_twins}, illegal: {contains_illegal_character}")
        
        if not contains_illegal_character and contains_sequential_staircase and contains_two_pair_twins:
            valid_password = True

    print(f"Next legal password: {''.join(password)}")

if __name__ == "__main__":
    main()
