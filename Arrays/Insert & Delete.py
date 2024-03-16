class Array:
    def __init__(self, max_size):
        self.max_size = max_size  # Maximum size of the array
        self.n = 0  # Current number of elements in the array
        self.arr = [0] * max_size  # Initialize array with zeros of size max_size

    def insert_beg(self, item):
        if self.n != self.max_size:  # Check if array is not full
            i = self.n - 1 # Start from the last element 
            while i >= 0:# Loop through the array
                self.arr[i + 1] = self.arr[i]  # Shift elements to the right
                i -= 1 # Decrement i by 1
            self.arr[0] = item  # Insert item at the beginning
            self.n += 1  # Increment number of elements
        else:
            print('Overflow')  # Print overflow message if array is full

    def insert_after(self, val, item):
        if self.n != self.max_size:  # Check if array is not full
            i = self.n - 1 # Start from the last element
            while self.arr[i] != val and i >= 0: # Loop through the array
                self.arr[i + 1] = self.arr[i]  # Shift elements to the right
                i -= 1
            self.arr[i + 1] = item  # Insert item after the specified value
            self.n += 1  # Increment number of elements
        else:
            print('Overflow')  # Print overflow message if array is full

    def insert_end(self, item):
        if self.n != self.max_size:  # Check if array is not full
            self.arr[self.n] = item  # Insert item at the end
            self.n += 1  # Increment number of elements
        else:
            print('Overflow')  # Print overflow message if array is full

    def del_beg(self):
        if self.n != 0:  # Check if array is not empty
            i = 1 # Start from the second element
            while i <= self.n - 1:
                self.arr[i - 1] = self.arr[i]  # Shift elements to the left
                i += 1
            self.n -= 1  # Decrement number of elements
        else:
            print('Underflow')  # Print underflow message if array is empty

    def del_after(self, val):
        if val in self.arr:  # Check if the value exists in the array
            i = self.n - 1# Start from the last element
            while self.arr[i] != val and i >= 0:# Loop through the array
                i -= 1 # Decrement i by 1
            i += 1
            while i < self.n - 1:
                self.arr[i] = self.arr[i + 1]  # Shift elements to the left
                i += 1
            self.n -= 1  # Decrement number of elements
        else:
            print('Not Found')  # Print message if value is not found in the array

    def del_end(self):
        if self.n != 0:  # Check if array is not empty
            self.n -= 1  # Decrement number of elements
        else:
            print('Underflow')  # Print underflow message if array is empty

    def display(self):
        print('Array:', self.arr[:self.n])  # Display elements of the array up to n

# Example usage:
arr = Array(10)
arr.insert_beg(1)
arr.insert_beg(2)
arr.insert_end(3)
arr.display()  # Output: Array: [2, 1, 3]
