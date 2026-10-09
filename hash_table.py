
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def hash_function(self, key):
        total = 0

        for char in key:
            total += ord(char)

        return (total * 31) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])
        self.count += 1

    def get(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                self.count -= 1
                return True

        return False


class DynamicHashTable(HashTable):
    def __init__(self, size):
        super().__init__(size)
        self.count = 0
        self.load_factor_threshold = 0.7

    def calculate_load_factor(self):
        return self.count / self.size

    def insert(self, key, value):
        super().insert(key, value)

        if self.calculate_load_factor() > self.load_factor_threshold:
            self.resize()

    def remove(self, key):
        return super().remove(key)

    def resize(self):
        old_table = self.table

        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for key, value in bucket:
                HashTable.insert(self, key, value)


if __name__ == "__main__":
    ht = DynamicHashTable(10)

    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)

    print(ht.get("apple"))
    print(ht.calculate_load_factor())

    ht.remove("apple")
    print(ht.get("apple"))
