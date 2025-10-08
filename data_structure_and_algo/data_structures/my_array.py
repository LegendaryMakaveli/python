class Array:
    def __init__(self, data_type, size):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be a positive integer")

        valid_types = (int, float, bool, str)
        if data_type not in valid_types:
            raise TypeError(f"Invalid data type. Must be one of {valid_types}")

        self.data_type = data_type
        self.array = [None] * size

        if not hasattr(self.array, "__setitem__"):
            raise TypeError("Object provided does not support assignment")

    def _validate_index(self, index):
        # print("DEBUG: validating index =", index, "type:", type(index))
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0 or index >= len(self.array):
            raise IndexError("Array index out of range")

    def _validate_value(self, value):
        if value is not None and not isinstance(value, self.data_type):
            raise TypeError("The value must be of type accepted dataType")

    def set_array(self, index, value):
        self._validate_index(index)
        if not hasattr(self.array, "__setitem__"):
            raise TypeError("Object provided does not support assignment")
        self.array[index] = value

    def get_array(self, index):
        self._validate_index(index)
        return self.array[index]

    def set_int_array(self, index, value):
        if self.data_type is not int:
            raise TypeError("This array was not created as an int array")
        self._validate_index(index)
        self._validate_value(value)
        self.array[index] = value

    def get_int_array(self, index):
        self._validate_index(index)
        return int(self.array[index])

    def set_float_array(self, index, value):
        if self.data_type is not float:
            raise TypeError("This array was not created as a float array")
        self._validate_index(index)
        self._validate_value(value)
        self.array[index] = value

    def get_float_array(self, index):
        self._validate_index(index)
        return float(self.array[index])

    def set_bool_array(self, index, value):
        if self.data_type is not bool:
            raise TypeError("This array was not created as a bool array")
        self._validate_index(index)
        self._validate_value(value)
        self.array[index] = value

    def get_bool_array(self, index):
        self._validate_index(index)
        return bool(self.array[index])

    def set_string_array(self, index, value):
        if self.data_type is not str:
            raise TypeError("This array was not created as a string array")
        self._validate_index(index)
        self._validate_value(value)
        self.array[index] = value

    def get_string_array(self, index):
        self._validate_index(index)
        return str(self.array[index])


    def __setitem__(self, index, value):
        self._validate_index(index)
        self._validate_value(value)
        self.array[index] = value

    def __getitem__(self, index):
        self._validate_index(index)
        return self.array[index]




    def get_length(self):
        return len(self.array)

    def __len__(self):
        return len(self.array)

    def __repr__(self):
       return str(self.array)

    def __eq__(self, array):
        if isinstance(array, Array):
            return self.array == array.array
        elif isinstance(array, list):
            return self.array == array
        else :
            return False
