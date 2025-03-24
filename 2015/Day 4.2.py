import hashlib

char = "0"
num_char = 6

def main():
    print("Input:")
    string = str(input())

    number = 0
    valid = False
    while not valid:
        
        number += 1
        string_i = f"{string}{number}"
        string_encoding = string_i.encode()
        hash = hashlib.md5(string_encoding)
        hash_str = hash.hexdigest()

        if hash_str[0:num_char] == char * num_char:
            valid = True

    print(f"Number = {number}")

if __name__ == "__main__":
    main()
