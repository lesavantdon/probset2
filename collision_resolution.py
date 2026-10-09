
import time
import random
import string


class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key):
        index = self._hash(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return


class LinearProbingHashTable:
    DELETED = object()

    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        first_deleted = None

        for _ in range(self.size):
            current = self.keys[index]

            if current is None:
                if first_deleted is not None:
                    index = first_deleted

                self.keys[index] = key
                self.values[index] = value
                return

            if current is self.DELETED:
                if first_deleted is None:
                    first_deleted = index

            elif current == key:
                self.values[index] = value
                return

            index = (index + 1) % self.size

        if first_deleted is not None:
            self.keys[first_deleted] = key
            self.values[first_deleted] = value
            return

        raise RuntimeError("Hash table is full")

    def get(self, key):
        index = self._hash(key)

        for _ in range(self.size):
            current = self.keys[index]

            if current is None:
                return None

            if current is not self.DELETED and current == key:
                return self.values[index]

            index = (index + 1) % self.size

        return None

    def remove(self, key):
        index = self._hash(key)

        for _ in range(self.size):
            current = self.keys[index]

            if current is None:
                return

            if current is not self.DELETED and current == key:
                self.keys[index] = self.DELETED
                self.values[index] = None
                return

            index = (index + 1) % self.size


def generate_random_string(length):
    return ''.join(
        random.choices(string.ascii_lowercase, k=length)
    )


def compare_performance():
    random.seed(42)

    separate_chaining = SeparateChainingHashTable(10000)
    linear_probing = LinearProbingHashTable(10000)

    test_data = [
        (generate_random_string(10), i)
        for i in range(10000)
    ]

    lookup_data = random.choices(test_data, k=1000)
    remove_data = random.sample(test_data, k=1000)

    # Insert performance
    sc_insert_start = time.perf_counter()

    for key, value in test_data:
        separate_chaining.insert(key, value)

    sc_insert_end = time.perf_counter()

    lp_insert_start = time.perf_counter()

    for key, value in test_data:
        linear_probing.insert(key, value)

    lp_insert_end = time.perf_counter()

    print(
        f"Separate Chaining insert time: "
        f"{sc_insert_end - sc_insert_start}"
    )

    print(
        f"Linear Probing insert time: "
        f"{lp_insert_end - lp_insert_start}"
    )

    # Lookup performance
    sc_lookup_start = time.perf_counter()

    for key, _ in lookup_data:
        separate_chaining.get(key)

    sc_lookup_end = time.perf_counter()

    lp_lookup_start = time.perf_counter()

    for key, _ in lookup_data:
        linear_probing.get(key)

    lp_lookup_end = time.perf_counter()

    print(
        f"Separate Chaining lookup time: "
        f"{sc_lookup_end - sc_lookup_start}"
    )

    print(
        f"Linear Probing lookup time: "
        f"{lp_lookup_end - lp_lookup_start}"
    )

    # Remove performance
    sc_remove_start = time.perf_counter()

    for key, _ in remove_data:
        separate_chaining.remove(key)

    sc_remove_end = time.perf_counter()

    lp_remove_start = time.perf_counter()

    for key, _ in remove_data:
        linear_probing.remove(key)

    lp_remove_end = time.perf_counter()

    print(
        f"Separate Chaining remove time: "
        f"{sc_remove_end - sc_remove_start}"
    )

    print(
        f"Linear Probing remove time: "
        f"{lp_remove_end - lp_remove_start}"
    )


if __name__ == "__main__":
    compare_performance()
