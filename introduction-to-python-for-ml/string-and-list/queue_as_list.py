# Queue (FIFO) is implemented as a list in Python. The first element of the list is the front of the queue.

queue = []

## Enqueue elements into the queue
queue.append(1)
queue.append(2)
queue.append(3)

## Dequeue elements from the queue
print(queue.pop(0))  # Output: 1
print(queue.pop(0))  # Output: 2
print(queue.pop(0))  # Output: 3

## Check if the queue is empty
print(len(queue) == 0)  # Output: True

# Note: Using a list to implement a queue is not efficient for large queues because popping from the front of the list (pop(0)) has O(n) time complexity. For better performance, consider using collections.deque which provides O(1) time complexity for append and pop operations from both ends.