from d_heap import Dheap


class MinHeap(Dheap):
    def __init__(self, k, heap=[]):
        super(self.__class__, self).__init__(
            k=k, heap=heap
        )

    def _heapify(self, index, size):
        """
        Brief:
            Private method to shiftup the smallest number
        Args:
            heap: Unprocessed Array
            index: Index to start
            size: Size of the array
        """
        children = self.get_children(index)
        if children == []:
            return
        min_child_index = children.index(min(children))
        # get actual index of min child
        min_child_index = (self.k * index) + (min_child_index + 1)
        if self.heap[min_child_index] < self.heap[index]:
            self._swap(index, min_child_index)
            if min_child_index <= size // self.k:
                self._heapify(min_child_index, size)

    def _swim_up(self, index):
        """
        Method to swim up if the children are smaller the root
        Args:
            index: Index of the children
        Example: (4 children heap)
                            1
              2        3         4        5
          6 7 8 9  10 11 12 13  14 15 16 17  18 19 20 21
            In the above heap root will be self.heap[0]
            elements 10, 11 are in respective index 9,10 the parrent node
            will be (children_idex - 1) // self.d = (9 - 1) // 4 => 2
        """
        if index == 0:
            return
        parent = (index - 1) // self.k
        if self.heap[parent] < self.heap[index]:
            return
        self._swap(parent, index)
        self._swim_up(index=parent)

    def delete_element_at_index(self, index):
        """
        Removes the element at the specified index

        """
        if index >= self.length():
            return

        self.heap[index] = float("-inf")
        self.swim_up(index)
        self.extract_root()
