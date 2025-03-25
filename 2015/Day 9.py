import math, itertools

# 368 too high

class Location:
    def __init__(self, distance: dict[str : int]):
        self.distance = distance
    
    def add(self, location_B: str, distance: int):
        self.distance[location_B] = distance

    def distance_to(self, location_name: str) -> int:
        return self.distance[location_name]

class DistanceMap:
    def __init__(self, locations: dict[str : Location]):
        self.locations = locations
        self.num_locations = 0

    def add(self, location_A: str, location_B: str, distance: int):

        if location_A in self.locations:
            self.locations[location_A].add(location_B, distance)
        else:
            self.locations.update({location_A: Location({location_B: distance})})
            self.num_locations += 1
        
        if location_B in self.locations:
            self.locations[location_B].add(location_A, distance)
        else:
            self.locations.update({location_B: Location({location_A: distance})})
            self.num_locations += 1

    def get_min_dists_brute_force(self, is_max: bool = False) -> int:
        min_dist = float('inf')
        max_dist = -float('inf')
        location_names = list(self.locations.keys())

        # Iterate over permutations
        for locations_order in itertools.permutations(location_names):
            dist = 0
            for j in range(len(locations_order) - 1):
                location_A = locations_order[j]
                location_B = locations_order[j + 1]
                dist += self.locations[location_A].distance_to(location_B)
            min_dist = min(min_dist, dist)
            max_dist = max(max_dist, dist)
        
        if is_max: return max_dist
        else: return min_dist
    
    def get_max_dists_brute_force(self) -> int:
        return self.get_min_dists_brute_force(is_max=True)

def main():
    print("Input:")

    locations = DistanceMap(locations={})
    while True:
        try:
            instruction = input()
            if instruction.strip() == "":
                break
                
            location_A, _, location_B, _, distance = instruction.split(" ")
            locations.add(location_A, location_B, int(distance))

        except EOFError:
            break

    print(f"Minimum distance: {locations.get_min_dists_brute_force()}")
    print(f"Maximum distance: {locations.get_max_dists_brute_force()}")

if __name__ == "__main__":
    main()
