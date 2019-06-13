class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        deleted = self.storage[0]
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        self.storage.pop()
        self._sift_down(0)
        return deleted

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while (index - 1) // 2 >= 0:
            parent_index = (index - 1) // 2
            if self.storage[parent_index] < self.storage[index]:
                self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            index = parent_index

    def _sift_down(self, index):
        while index * 2 + 1 <= len(self.storage) - 1:
            left_child_index = index * 2 + 1
            right_child_index = index * 2 + 2

            if right_child_index > len(self.storage) - 1:
                largest_index = left_child_index
            else:
                largest_index = index * 2 + \
                    1 if self.storage[left_child_index] > self.storage[right_child_index] else right_child_index

            if self.storage[index] < self.storage[largest_index]:
                self.storage[index], self.storage[largest_index] = self.storage[largest_index], self.storage[index]
            index = largest_index
