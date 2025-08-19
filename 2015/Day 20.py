import math, time

# 10000  - 360
# Runtime: 0:00:00.00s
# 
# 100000 - 3120
# Runtime: 0:00:00.11s
# 
# 1000000 - 27720
# Runtime: 0:00:09.80s
# 
# 29000000 - 665280
# Runtime: 1:54:00.49s

def main():

    ### Process the input...

    print("Integer Input:")

    threshold: int = int(input())
    
    
    print(f"Are there an infinite number of houses?")
    valid = False
    is_infinite = False
    while not valid:
        line = input()
        if line.lower() == "y":
            valid = True
            is_infinite = True
        elif line.lower() == "n" or line == "":
            valid = True
            is_infinite = False
        else:
            print(f"Please only enter y or n.")
    del valid
    
    
    i: int = 0
    house_value: int = 0
    
    start_time = time.time()
    
    if is_infinite:
        reduced_threshold: int = math.ceil(float(threshold) / 10.0)
        while house_value < reduced_threshold:
            i += 1
            house_value = 0
            for j in range(1, i+1):
                if i % j == 0:
                    house_value += j
        
    elif not is_infinite:
        reduced_threshold: int = math.ceil(float(threshold) / 11.0)
        while house_value < reduced_threshold:
            i += 1
            house_value = 0
            for j in range(1, i+1 if i <= 50 else 50):
                if i % j == 0:
                    house_value += j
    
    print(f"Lowest number house with at least as many presents as the house number: {i}")
    print(f"Runtime: {(((time.time() - start_time)*1000) // 10) / 100:.2f}s")
    print()

if __name__ == "__main__":
    main()
