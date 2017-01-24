#!/usr/bin/python3
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if value is None:
            self.__next = value
        elif isinstance(value, Node):
            self.__next = value
        else:
            raise TypeError("next must be a Node object")

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        newNode = Node(value, None)
        if self.__head is None:
            self.__head = newNode
        elif self.__head.next is None:
            if self.__head.data < value:
                self.__head.next = newNode
            elif self.__head.data >= value:
                newNode.next = self.__head
                self.__head = new
        else:
            tmp = self.__head
            while tmp.next:
                if tmp.data >= value:
                    newNode.next = tmp
                    tmp = newNode
                    self.__head = tmp
                    return
                elif tmp.data < value and tmp.next.data >= value:
                    newNode.next = tmp.next
                    tmp.next = newNode
                    return
                tmp = tmp.next
            tmp.next = newNode

    def __str__(self):
        if not self.__head is None:
            tmp = self.__head
            out = "" + str(tmp.data) + "\n"
            while tmp.next:
                tmp = tmp.next
                if tmp.next:
                    out += str(tmp.data) + "\n"
                else:
                    out += str(tmp.data)
            return out
