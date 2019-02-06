import copy
from unittest import TestCase
from d_heap import MinHeap, MaxHeap


class TestMinHeap(TestCase):
    def setUp(self):
        self.array = [
            4, 3, 6, 8, 11, 1, 5, 14, 10, 7, 2, 12, 9, 13, 15
        ]

    def test_min_heap_property(self):
        min_heap = MinHeap(4, self.array)
        length = min_heap.length()
        elements = min_heap.elements()
        for i in range(0, length):
            current_value = elements[i]
            children = min_heap.get_children(i)
            for child in children:
                self.assertLessEqual(current_value, child)

    def test_min_heap_count_and_elements(self):
        min_heap = MinHeap(4, self.array)
        self.assertEqual(15, min_heap.length())
        self.assertEqual(
            [1, 3, 2, 8, 11, 4, 5, 14, 10, 7, 6, 12, 9, 13, 15],
            min_heap.elements()
        )
        min_heap = MinHeap(5, self.array)
        self.assertEqual(
            [1, 2, 6, 8, 11, 4, 5, 14, 10, 7, 3, 12, 9, 13, 15],
            min_heap.elements()
        )

    def test_add_element_to_minheap(self):
        min_heap = MinHeap(4, self.array)
        min_heap.add_element(0)
        self.assertEqual(16, min_heap.length())
        self.assertEqual(
            [0, 3, 2, 1, 11, 4, 5, 14, 10, 7, 6, 12, 9, 13, 15, 8],
            min_heap.elements()
        )
        self.assertEqual(0, min_heap.get_root_value())

    def test_add_array_of_elements_to_minheap(self):
        min_heap = MinHeap(4, self.array)
        min_heap.add_element([0, 24, 17, 55])
        self.assertEqual(19, min_heap.length())
        self.assertEqual(
            [0, 3, 2, 1, 11, 4, 5, 14, 10, 7, 6, 12,
             9, 13, 15, 8, 24, 17, 55], min_heap.elements()
        )
        self.assertEqual(0, min_heap.get_root_value())

    def test_delete_element_at_index_minheap(self):
        min_heap = MinHeap(4, self.array)
        min_heap.delete_element_at_index(1)
        self.assertEqual(14, min_heap.length())
        self.assertEqual([1, 4, 2, 8, 11, 15, 5, 14, 10, 7, 6, 12, 9, 13], min_heap.elements())
        min_heap.delete_element_at_index(3)
        self.assertEqual([1, 4, 2, 13, 11, 15, 5, 14, 10, 7, 6, 12, 9], min_heap.elements())
        self.assertEqual(13, min_heap.length())
        min_heap.delete_element_at_index(13)
        self.assertEqual(13, min_heap.length())


    def test_search_value_minheap(self):
        min_heap = MinHeap(3, self.array)
        retindex = min_heap.search_value(5)
        self.assertEqual(6, retindex)
        retindex = min_heap.search_value(20)
        self.assertEqual(retindex, -1)

    def test_extract_root_value_minheap(self):
        min_heap = MinHeap(4, self.array)
        self.assertEqual(1, min_heap.extract_root())
        self.assertEqual(
            [2, 3, 6, 8, 11, 4, 5, 14, 10, 7, 15, 12, 9, 13],
            min_heap.elements()
        )

    def test_multiple_operations_minheap(self):
        min_heap = MinHeap(4, self.array)
        min_heap.add_element(5)
        self.assertEqual(
            [1, 3, 2, 5, 11, 4, 5, 14, 10, 7, 6, 12, 9, 13, 15, 8],
            min_heap.elements()
        )
        self.assertEqual(1, min_heap.extract_root())
        self.assertEqual(
            [2, 3, 6, 5, 11, 4, 5, 14, 10, 7, 8, 12, 9, 13, 15],
            min_heap.elements()
        )
        min_heap.add_element([1, 3, 5, 6])
        self.assertEqual(
            [1, 3, 6, 2, 5, 4, 5, 14, 10, 7, 8, 12, 9, 13, 15, 5, 3, 11, 6],
            min_heap.elements()
        )
        self.assertEqual(1, min_heap.extract_root())
        self.assertEqual(2, min_heap.extract_root())
        self.assertEqual(
            [3, 4, 6, 3, 5, 11, 5, 14, 10, 7, 8, 12, 9, 13, 15, 5, 6],
            min_heap.elements()
        )
        self.assertEqual(
            [3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            sorted(min_heap.elements())
        )


class TestMaxHeap(TestCase):
    def setUp(self):
        self.array = [
            4, 3, 6, 8, 11, 1, 5, 14, 10, 7, 2, 12, 9, 13, 15
        ]

    def test_min_heap_property(self):
        max_heap = MaxHeap(4, self.array)
        length = max_heap.length()
        elements = max_heap.elements()
        for i in range(0, length):
            current_value = elements[i]
            children = max_heap.get_children(i)
            for child in children:
                self.assertGreaterEqual(current_value, child)

    def test_max_heap_count_and_elements(self):
        max_heap = MaxHeap(4, self.array)
        self.assertEqual(15, max_heap.length())
        self.assertEqual(
            [15, 14, 12, 13, 11, 1, 5, 3, 10, 7, 2, 6, 9, 4, 8],
            max_heap.elements()
        )
        max_heap = MaxHeap(5, self.array)
        self.assertEqual(
            [15, 14, 13, 8, 11, 1, 5, 3, 10, 7, 2, 12, 9, 4, 6],
            max_heap.elements()
        )

    def test_add_element_to_maxheap(self):
        max_heap = MaxHeap(4, self.array)
        max_heap.add_element(23)
        self.assertEqual(16, max_heap.length())
        self.assertEqual(
            [23, 14, 12, 15, 11, 1, 5, 3, 10, 7, 2, 6, 9, 4, 8, 13],
            max_heap.elements()
        )
        self.assertEqual(23, max_heap.get_root_value())
        self.assertEqual(
            [23, 14, 12, 15, 11, 1, 5, 3, 10, 7, 2, 6, 9, 4, 8, 13],
            max_heap.elements()
        )

    def test_add_array_of_elements_to_maxheap(self):
        max_heap = MaxHeap(4, self.array)
        max_heap.add_element([21, 14, 27, 35])
        self.assertEqual(19, max_heap.length())
        self.assertEqual(
            [35, 14, 12, 15, 27, 1, 5, 3, 10, 7, 2,
             6, 9, 4, 8, 13, 14, 11, 21], max_heap.elements()
        )
        self.assertEqual(35, max_heap.get_root_value())

    def test_delete_element_at_index_maxheap(self):
        max_heap = MaxHeap(3, self.array)
        max_heap.delete_element_at_index(1)
        self.assertEqual(14, max_heap.length())
        self.assertEqual([15, 11, 14, 12, 4, 1, 5, 6, 10, 7, 2, 8, 9, 3], max_heap.elements())
        max_heap.delete_element_at_index(3)
        self.assertEqual([15, 11, 14, 9, 4, 1, 5, 6, 10, 7, 2, 8, 3], max_heap.elements())
        self.assertEqual(13, max_heap.length())
        max_heap.delete_element_at_index(13)
        self.assertEqual(13, max_heap.length())


    def test_search_value_maxheap(self):
        max_heap = MaxHeap(5, self.array)
        retindex = max_heap.search_value(10)
        self.assertEqual(8, retindex)
        retindex = max_heap.search_value(29)
        self.assertEqual(retindex, -1)

    def test_extract_root_value_maxheap(self):
        max_heap = MaxHeap(4, self.array)
        self.assertEqual(15, max_heap.extract_root())
        self.assertEqual(
            [14, 10, 12, 13, 11, 1, 5, 3, 8, 7, 2, 6, 9, 4],
            max_heap.elements()
        )

    def test_multiple_operations_maxheap(self):
        max_heap = MaxHeap(4, self.array)
        max_heap.add_element(23)
        self.assertEqual(
            [23, 14, 12, 15, 11, 1, 5, 3, 10, 7, 2, 6, 9, 4, 8, 13],
            max_heap.elements()
        )
        self.assertEqual(23, max_heap.extract_root())
        self.assertEqual(
            [15, 14, 12, 13, 11, 1, 5, 3, 10, 7, 2, 6, 9, 4, 8],
            max_heap.elements()
        )
        max_heap.add_element([21, 14, 27, 35])
        self.assertEqual(
            [35, 14, 12, 15, 27, 1, 5, 3, 10, 7, 2, 6, 9,
             4, 8, 13, 14, 11, 21], max_heap.elements()
        )
        self.assertEqual(35, max_heap.extract_root())
        self.assertEqual(27, max_heap.extract_root())
        self.assertEqual(
            [21, 14, 12, 15, 11, 1, 5, 3, 10, 7, 2, 6, 9, 4, 8, 13, 14],
            max_heap.elements()
        )
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 15, 21],
            sorted(max_heap.elements())
        )
