class CircularQueue:
    DEFAULT_CAPACITY=10

    def __init__(self):

        self._data=[None]*CircularQueue.DEFAULT_CAPACITY

        self._size = 0

        self._front = 0


    def __len__(self):

        return self._size


    def is_Empty(self):

        return self._size == 0


    def first(self):
        if self.is_Empty():
            raise Empty('Queue is empty.') #The method is exited, nothing is executed from here

        return self._data[self._front]




    def dequeue(self):
        if self.is_Empty():
            raise Empty('Queue is empty for da dequeue operation.')

        front = (self._front + 1) % len(self._data)

        dequeued_element = self._data[self._front]

        self._data[self._front] = None # Le process of garbage collection, to ensure no space is waste

        self._size -= 1

        return dequeued_element




    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        tail = (self._front + self._size) % len(self._data)

        self._data[tail]=element

        self._size += 1


    def _resize(self, new_capacity):
        ...

class Empty(Exception):
    pass

if __name__=="__main__":
    obj_queue=CircularQueue()

    # obj_queue.enqueue(11)
    # obj_queue.enqueue(22)
    # obj_queue.enqueue(33)
    # obj_queue.enqueue(44)
    # obj_queue.enqueue(55)

    insert_elements=[11,22,33,44,55]
    for element in insert_elements:
        obj_queue.enqueue(element)

        print(f"Added Element: {element}")
        print(f"The new size of the Queues: {obj_queue._size}")

    print("\n Current Queue representation:")




