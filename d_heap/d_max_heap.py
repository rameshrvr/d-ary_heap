from d_heap import Dheap


class MaxHeap(Dheap):
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
        max_child_index = children.index(max(children))
        # get actual index of max child
        max_child_index = (self.k * index) + (max_child_index + 1)
        if self.heap[max_child_index] > self.heap[index]:
            self._swap(index, max_child_index)
            if max_child_index <= size // self.k:
                self._heapify(max_child_index, size)

    def _swim_up(self, index):
        """
        Method to swim up if the children are greater the root
        Args:
            index: Index of the children
        Example: (4 children heap)
                            16
              15       14        13       12
          11 10 9 8  7 6 5 4   3 2 1 0   0 0 0 0
            In the above heap root will be self.heap[0]
            elements 3, 2 are in respective index 13, 14 the parrent node
            will be (children_idex - 1) // self.d = (13 - 1) // 4 => 3
        """
        if index == 0:
            return
        parent = (index - 1) // self.k
        if self.heap[parent] > self.heap[index]:
            return
        self._swap(parent, index)
        self._swim_up(index=parent)

    def delete_element_at_index(self, index):
        """
        Removes the element at the specified index

        """
        if index >= self.length():
            return

        self.heap[index] = float("inf")
        self.swim_up(index)
        self.extract_root()
