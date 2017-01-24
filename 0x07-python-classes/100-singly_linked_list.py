#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

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
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None:
            self.__next_node = value
        elif isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        newNode = Node(value, None)
        if self.__head is None:
            self.__head = newNode
        elif self.__head.next_node is None:
            if self.__head.data < value:
                self.__head.next_node = newNode
            elif self.__head.data >= value:
                newNode.next_node = self.__head
                self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node:
                if tmp.data >= value:
                    newNode.next_node = tmp
                    tmp = newNode
                    self.__head = tmp
                    return
                elif tmp.data < value and tmp.next_node.data >= value:
                    newNode.next_node = tmp.next_node
                    tmp.next_node = newNode
                    return
                tmp = tmp.next_node
            tmp.next_node = newNode

    def __str__(self):
        if self.__head is not None:
            tmp = self.__head
            out = "" + str(tmp.data) + "\n"
            while tmp.next_node:
                tmp = tmp.next_node
                if tmp.next_node:
                    out += str(tmp.data) + "\n"
                else:
                    out += str(tmp.data)
            return out
