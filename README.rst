D-ary Heap
##########
Python functions for working with D-ary Heap (Heap with more than 2 child nodes). For more info about this Data Structure Please gothrough: https://en.wikipedia.org/wiki/D-ary_heap

This library provides the below Heap specific functions.

*heapify*
	Convert list of elements to Heap data structure (MinHeap/MaxHeap)

*add_element*
	Add single/list of elements to Heap

*get_root_value*
	Returns root value of the Heap without removing the element
	Minimum value for Min Heap, Maximum value for Max Heap

*extract_root*
	Extract root element from Heap and reform the Heap

*search_value*
	Searches the value in heap and returns index.
	if same element is present multiple times, first occurring index is returned

*delete_element_at_index*
	Remove the element at the specified index and reform the Heap


For example function invocations, plesae see the tutorial.

.. contents::


Installation
============

install from pypi using pip::

	$ pip install d_heap

or install from source using::

	$ git clone https://github.com/rameshrvr/d-ary_heap.git
	$ cd d-ary_heap
	$ pip install .


Tutorial
========

1. Min Heap (Heap where the data in parent node is lesser than the data in child node)

.. code-block:: python
	
	Rameshs-MacBook-Pro:d-ary_heap rameshrv$ python3
	Python 3.7.2 (default, Dec 27 2018, 07:35:06) 
	[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>>
	>>> from d_heap import MinHeap, MaxHeap
	>>> 
	>>> array = [4, 3, 6, 8, 11, 1, 5, 14, 10, 7, 2, 12, 9, 13, 15]
	>>> 
	>>> min_heap_4_children = MinHeap(4, array)  # Convert array to 4 children Heap
	>>> 
	>>> min_heap_4_children.elements()
	[1, 3, 2, 8, 11, 4, 5, 14, 10, 7, 6, 12, 9, 13, 15]
	>>> 
	>>> min_heap_5_children = MinHeap(5, array)  # Convert array to 5 children Heap
	>>> 
	>>> min_heap_5_children.elements()
	[1, 2, 6, 8, 11, 4, 5, 14, 10, 7, 3, 12, 9, 13, 15]
	>>> 
	>>> min_heap_4_children.add_element(0)  # Add single element to Heap
	>>> 
	>>> min_heap_4_children.elements()
	[0, 3, 2, 1, 11, 4, 5, 14, 10, 7, 6, 12, 9, 13, 15, 8]
	>>> 
	>>> min_heap_5_children.add_element([0, 24, 17, 55])  # Add list of elements to heap
	>>> 
	>>> min_heap_5_children.elements()
	[0, 2, 1, 8, 11, 4, 5, 14, 10, 7, 3, 12, 9, 13, 15, 6, 24, 17, 55]
	>>> 
	>>> min_heap_4_children.extract_root()  # Extract root element from Heap and retrun it. In this case its the minimum element
	0
	>>> 
	>>> min_heap_4_children.elements()
	[1, 3, 2, 8, 11, 4, 5, 14, 10, 7, 6, 12, 9, 13, 15]
	>>> 
	>>> min_heap_4_children.get_root_value()  # Returns the root value (minimum value) without removing it from Heap
	1
	>>> 
	>>> min_heap_4_children.search_value(5)  # Returns index of the searched value. -1 if there is no such value in Heap
	6
	>>> min_heap_4_children.search_value(7)
	9
	>>> min_heap_4_children.search_value(21)
	-1
	>>> 
	>>> min_heap_4_children.delete_element_at_index(4)  # Remove the element at the specified index
	>>> 
	>>> min_heap_4_children.elements()
	[1, 3, 2, 8, 15, 4, 5, 14, 10, 7, 6, 12, 9, 13]
	>>> 




2. Max Heap (Heap where the data in parent node is greater than the data in child node)

.. code-block:: python

	Rameshs-MacBook-Pro:d-ary_heap rameshrv$ python3
	Python 3.7.2 (default, Dec 27 2018, 07:35:06) 
	[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>>
	>>> from d_heap import MinHeap, MaxHeap
	>>>
	>>> array = [4, 3, 6, 8, 11, 1, 5, 14, 10, 7, 2, 12, 9, 13, 15]
	>>>
	>>> max_heap_4_children = MaxHeap(4, array)  # Convert array to 4 children Heap
	>>> 
	>>> max_heap_4_children.elements()
	[15, 14, 12, 13, 11, 1, 5, 3, 10, 7, 2, 6, 9, 4, 8]
	>>> 
	>>> max_heap_5_children = MaxHeap(5, array)  # Convert array to 5 children Heap
	>>> 
	>>> max_heap_5_children.elements()
	[15, 14, 13, 8, 11, 1, 5, 3, 10, 7, 2, 12, 9, 4, 6]
	>>> 
	>>> max_heap_4_children.add_element(21)  # Add single element to Heap
	>>> 
	>>> max_heap_4_children.elements()
	[21, 14, 12, 15, 11, 1, 5, 3, 10, 7, 2, 6, 9, 4, 8, 13]
	>>> 
	>>> 
	>>> max_heap_5_children.add_element([21, 14, 27, 35])  # Add list of elements to heap
	>>> 
	>>> max_heap_5_children.elements()
	[35, 14, 15, 27, 11, 1, 5, 3, 10, 7, 2, 12, 9, 4, 6, 13, 8, 14, 21]
	>>> 
	>>> max_heap_4_children.extract_root()  # Extract root element from Heap and retrun it. In this case its the maximum element
	21
	>>> 
	>>> max_heap_4_children.elements()
	[15, 14, 12, 13, 11, 1, 5, 3, 10, 7, 2, 6, 9, 4, 8]
	>>> 
	>>> max_heap_4_children.get_root_value()  # Returns the root value (maximum value) without removing it from Heap
	15
	>>> 
	>>> max_heap_4_children.search_value(5)  # Returns index of the searched value. -1 if there is no such value in Heap
	6
	>>> max_heap_4_children.search_value(11)
	4
	>>> max_heap_4_children.search_value(21)
	-1
	>>> 
	>>> max_heap_4_children.delete_element_at_index(2)  # Remove the element at the specified index
	>>> 
	>>> max_heap_4_children.elements()
	[15, 14, 9, 13, 11, 1, 5, 3, 10, 7, 2, 6, 8, 4]
	>>> 



Development
===========

After checking out the repo, `cd` to the repository. Then, run `pip install .` to install the package locally. You can also run `python (or) python3` for an interactive prompt that will allow you to experiment.

To install this package onto your local machine, `cd` to the repository then run `pip install .`. To release a new version, update the version number in `setup.py`, and then run `python setup.py register`, which will create a git tag for the version, push git commits and tags, and push the package file to [PyPI](https://pypi.org).


Contributing
============

Bug reports and pull requests are welcome on GitHub at https://github.com/rameshrvr/d-ary_heap. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant]<http://contributor-covenant.org> code of conduct.


License
========

The package is available as open source under the terms of the [MIT License]<https://opensource.org/licenses/MIT>.


Code of Conduct
===============

Everyone interacting in the Binary Heap project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/rameshrvr/d-ary_heap/blob/master/CODE_OF_CONDUCT.md).


misc
========

:license:
  * MIT License

:authors:
  * Ramesh RV
  * Adithya KS
