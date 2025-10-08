from my_array import Array

class ArrayList:
    def __init__(self, data_type, size):
        self.arrayList = Array(int, size)
        self.isEmpty = True
        self.count = 0
        self.data_type = data_type


    @property
    def get_isEmpty(self):
        return self.isEmpty

    def add_element(self, element):
        self.get_adjust_capacity()
        self.arrayList[self.count] = element
        self.count += 1
        self.isEmpty = False

    def get_element(self):
         return self.arrayList

    def remove_element(self):
        for element in range(self.count):
            self.arrayList[element] = self.data_type()
        self.isEmpty = True


    def add_element_by_index(self, index, value):
        self.get_adjust_capacity()
        if index < 0 or index > self.count:
            raise IndexError("Index out of range")
        for element in range(self.count, index, -1):
            self.arrayList[element] = self.arrayList[element - 1]

        self.arrayList[index] = value
        self.count += 1

        self.isEmpty = False


    def remove_element_by_index(self, index, value):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        for element in range(index, self.count - 1):
            self.arrayList[element] = self.arrayList[element + 1]

        self.arrayList[self.count - 1] = value
        self.count -= 1
        self.isEmpty = False

    def get_element_by_index(self, index):
        if index <= 0 or index < self.count:
            return self.arrayList[index]
        return None

    def search_element(self, element):
            for index in range(self.count):
                if self.arrayList[index] == element:
                    return True
            return False

    def search_all_element(self, new_array):
            if not isinstance(new_array, ArrayList):
                raise ValueError("Only ArrayList can be searched at once")

            for index in range(new_array.count):
                element = new_array.arrayList[index]
                if not self.search_element(element):
                    return False
            return True

    def get_index(self, element):
        if element is None or element == 0:
            return -1
        for index in range(self.count):
            if self.arrayList[index] == element:
                return index
        return -1

    def get_size(self): return self.count

    def sort_my_list(self):
        for count in range(self.count - 1):
            for counter in range(count + 1, self.count):
                if self.arrayList[count] > self.arrayList[counter]:
                    temp = self.arrayList[count]
                    self.arrayList[count] = self.arrayList[counter]
                    self.arrayList[counter] = temp

    def _adjust_capacity(self):
            new_array = Array(self.data_type, len(self.arrayList) * 2)
            for index in range(self.count):
                new_array[index] = self.arrayList[index]
            self.arrayList = new_array

    def get_adjust_capacity(self):
        if self.count >= len(self.arrayList):
            self._adjust_capacity()





