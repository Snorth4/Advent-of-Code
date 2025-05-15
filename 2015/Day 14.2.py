from collections import defaultdict

def main():
    print("Input:")
    
    words: list[list[str]] = [[]]
    while True:
        try:
            word = input()
            if word.strip() == "":
                break
            
            words.append(word.split(" "))
        except EOFError:
            break

    words = [x for x in words if x] 
    reindeer_values: defaultdict[str, list[int]] = defaultdict(lambda: [0, 0, 0, 0])
    n = len(words)
    
    for i in range(n):
        reindeer_values[words[i][0]][0] = int(words[i][3])
        reindeer_values[words[i][0]][1] = int(words[i][6])
        reindeer_values[words[i][0]][2] = int(words[i][13])
    del words
    
    print("Input the time limit:")
    time = int(input())
    
    for i in range(1, time + 1):
        max_value = 0
        max_value_names = []
        for name in reindeer_values.keys():
            distance_per_period = reindeer_values[name][0]
            moving_time = reindeer_values[name][1]
            rest_time = reindeer_values[name][2]
            period = moving_time + rest_time

            distance = distance_per_period * moving_time * (i // period)

            if i % period >= moving_time:
                distance += distance_per_period * moving_time
            elif i % period < moving_time:
                distance += distance_per_period * (i % period)

            if distance > max_value:
                max_value = distance
                max_value_names = [name]
            elif distance == max_value:
                max_value_names.append(name)

        # Increment the highest score(s) here.
        for name in max_value_names:
            reindeer_values[name][3] += 1
        
    # Pull the highest score.
    max_score = 0
    for name in reindeer_values.keys():
        if reindeer_values[name][3] > max_score:
            max_score = reindeer_values[name][3]
    
    print(f"Maximum score: {max_score}")

if __name__ == "__main__":
    main()
