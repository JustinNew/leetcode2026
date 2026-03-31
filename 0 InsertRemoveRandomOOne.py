# Insert, Remove, Random O(1)

# Example:
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // return true
# randomizedSet.remove(2); // return false
# randomizedSet.insert(2); // return true
# randomizedSet.getRandom(); // return 2
# randomizedSet.remove(1); // return true
# randomizedSet.insert(2); // return false
# randomizedSet.getRandom(); // return 2

# Use a list to store the values and a dictionary to store the index of the values.
# Insert: add the value to the list and the dictionary
# Remove: swap the value with the last value in the list and remove the last value
# GetRandom: return a random value from the list
class RandomizedSet:

    def __init__(self):
        self.values = []
        self.valuesIdx = {} # value: index

    def insert(self, val: int) -> bool:
        if val in self.valuesIdx:
            return False
        
        self.valuesIdx[val] = len(self.values)
        self.values.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.valuesIdx:
            return False
        
        index = self.valuesIdx[val]
        self.valuesIdx[self.values[-1]] = index
        del self.valuesIdx[val]
        self.values[index] = self.values[-1]
        self.values.pop()

        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.values) - 1)
        return self.values[index]