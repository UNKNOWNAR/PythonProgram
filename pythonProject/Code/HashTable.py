class HashTable:#Uses LinearProbing to To use HashTable
    def __init__(self):
        self.max = 15
        self.arr = [[] for _ in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        while self.arr[h] is None:
            h+=1
            if(h==len(self.arr)-1):
                h=0
        self.arr[h] = val

    def __contains__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return True
        return False

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = []

    def load_file(self, file_path):
        with open(file_path, "r") as f:
            for line in f:
                tokens = line.split(",")
                day = tokens[0]
                price = float(tokens[1])
             # Populate the hash map with the extracted data
                self[day] = price

    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

    def display(self):
        for i in self.arr:
            print(i)

if __name__ == "__main__":
    hash = HashTable()
    # Load data from CSV file into the hash map
    hash.load_file("E:\\Python Folders\\pythonProject\\files\\stock_prices.csv")
    # Delete an item and display the hash map again
    print(hash.arr)
    hash["Mar-17"] = 362
    print(hash.arr[7][1])
    print("\n", hash["Mar-06"], "\n")
    del hash["Mar-07"]