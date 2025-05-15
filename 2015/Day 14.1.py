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
    reindeer_values: defaultdict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
    n = len(words)
    
    for i in range(n):
        reindeer_values[words[i][0]][0] = int(words[i][3])
        reindeer_values[words[i][0]][1] = int(words[i][6])
        reindeer_values[words[i][0]][2] = int(words[i][13])
    del words
    
    time = 2503
    
    max_distance = 0
    for name in reindeer_values.keys():
        distance_per_period = reindeer_values[name][0]
        moving_time = reindeer_values[name][1]
        rest_time = reindeer_values[name][2]
        period = moving_time + rest_time
        
        distance = distance_per_period * moving_time * (time // period)
        
        if time % period >= moving_time:
            distance += distance_per_period * moving_time
        elif time % period < moving_time:
            distance += distance_per_period * (time % period)
        
        if distance > max_distance:
            max_distance = distance
    
    print(f"Maximum distance: {max_distance}")

if __name__ == "__main__":
    main()
