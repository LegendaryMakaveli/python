from data_structures.my_array import Array

class SetBehaviour:
    def __init__(self):
        self.isEmpty = True
        self.elements = Array(int, 4)
        self.size = 0

    def is_empty(self):
        return self.isEmpty

    def add_element(self, element):
        if not isinstance(element, int):
            raise TypeError("Only integers are allowed in this SetBehaviour")

        for count in range(self.size):
            if self.elements[count] == element:
                return

        self._adjust_capacity()
        self.elements[self.size] = element
        self.size += 1
        self.isEmpty = False

    def add_many_elements(self, new_set):
        if not isinstance(new_set, (list, tuple, Array)):
            raise TypeError("add_many_elements expects a list, tuple, or Array")

        self._adjust_capacity()
        for element in new_set:
            self.add_element(element)

    def clear_element(self):
        self.elements = Array(int, 4)
        self.size = 0
        self.isEmpty = True

    def search_element(self, element):
        for count in range(self.size):
            if self.elements[count] == element:
                return True
        return False

    def search_all(self, new_set):
        if not isinstance(new_set, (list, tuple, Array)):
            raise TypeError("search_all expects a list, tuple, or Array")

        for element in new_set:
            if not self.search_element(element):
                return False
        return True

    def remove_element_by_value(self, element):
        for count in range(self.size):
            if self.elements[count] == element:
                for counter in range(count, self.size - 1):
                    self.elements[counter] = self.elements[counter + 1]
                self.size -= 1
                if self.size == 0:
                    self.isEmpty = True
                return

    def _adjust_capacity(self):
        if self.size >= len(self.elements):
            new_array = Array(int, len(self.elements) * 2)
            for count in range(len(self.elements)):
                new_array[count] = self.elements[count]
            self.elements = new_array
