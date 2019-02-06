import copy


class Dheap(object):
    def __init__(self, k, heap):
        self.heap = copy.deepcopy(heap)
        self.k = k
        if self.heap:
            self.heapify()

    def elements(self):
        """
        Method to return elements of D-ary Heap
        """
        return self.heap

    def length(self):
        """
        Method to return length of D-ary Heap
        """
        return len(self.heap)

    def _get_parent_index(self, child_index):
        """
        Method to find parent node index from child node index
        """
        return (child_index - 1) // self.k

    def heapify(self):
        """
        Method to convert Array into D-ary Heap
        """
        size = self.length()
        for index in reversed(range(
            self._get_parent_index(child_index=(size - 1)) + 1
        )):
            self._heapify(index=index, size=size)

    def get_children(self, parent_index):
        """
        Method to get all the children index from parent index
        """
        children = []
        size = self.length()
        for i in range(self.k):
            child_index = (parent_index * self.k) + (i + 1)
            if child_index < size:
                children.append(self.heap[child_index])
            else:
                break
        return children

    def swim_up(self, index):
        self._swim_up(index=index)

    def get_root_value(self):
        """
        Return root value of the heap
        """
        return self.heap[0]

    def add_element(self, element):
        """
        Brief:
            Method to add element / elements to D-heap
        Args:
            element: Could be a single number of array of numbers
        """
        if isinstance(element, list):
            for _element in element:
                self.heap.append(_element)
                self.swim_up(self.length() - 1)
        else:
            self.heap.append(element)
            self.swim_up(self.length() - 1)

    def extract_root(self):
        """
        Remove root element from the heap and return it
        """
        self._swap(0, self.length() - 1)
        result = self.heap.pop()
        self._heapify(index=0, size=self.length())
        return result

    def search_value(self, value):
        """
        Brief:
            Searches the value in heap and returns index
        Args:
            value: The value to be searched in the heap
        Return:
             Returns the index if the value is found otherwise -1
             Note: if same element is present multiple times,
                   first occurring index is returned
        """
        length = self.length()
        for index in range(length):
            if self.heap[index] == value:
                return index

        return -1

    def _swap(self, index1, index2):
        """
        Brief:
            Swap two elements in the given heap
        Args:
            index1: Index of the 1st element to be swapped
            index2: Index of the 2nd element to be swapped
        """
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
