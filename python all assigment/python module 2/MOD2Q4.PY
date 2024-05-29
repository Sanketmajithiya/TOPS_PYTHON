""" Q.4 How memory is managed in Python? 

1.Automatic Memory Management: Python utilizes automatic memory management, often referred to as garbage collection, to reclaim memory occupied by objects that are no longer in use. The Python memory manager takes care of this automatically, freeing programmers from manually allocating and deallocating memory.

2.Reference Counting: Python uses reference counting as a fundamental mechanism for memory management. Every object in Python has a reference count, which keeps track of the number of references pointing to that object. When an object's reference count drops to zero, meaning there are no more references to it, Python's garbage collector frees the memory associated with that object.

3.Garbage Collection: In addition to reference counting, Python also employs a garbage collection mechanism to deal with circular references or situations where reference counting alone may not be sufficient. Python's garbage collector is responsible for detecting and collecting cyclic references, ensuring that memory occupied by unreachable objects is properly reclaimed.

4.Memory Pool: Python maintains a private heap for storing objects. It manages this heap using a system called memory pool, which preallocates a certain amount of memory for specific types of objects. This helps reduce the overhead of memory allocation and deallocation by reusing memory blocks when possible.

5.Memory Optimizations: Python also implements various memory optimization techniques, such as interning small integers and certain string literals, which helps reduce memory usage by reusing immutable objects rather than creating new ones.

Overall, Python's memory management is designed to provide a balance between performance, simplicity, and reliability, allowing programmers to focus on writing code without having to worry extensively about memory allocation and deallocation. However, understanding these underlying mechanisms can be beneficial for optimizing memory usage in performance-critical applications."""


