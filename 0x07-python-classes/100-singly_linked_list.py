#!/usr/bin/python3
"""
This is a Node class.

This Node class creates a Node object.
"""


class Node:
    """
    Initialize Node object.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
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

"""
This is a SinglyLinkedList class.

This SinglyLinkedList class creates a linkedlist of Node objects in a soretd
order and prints it.
"""


class SinglyLinkedList:
    """
    Initialize SinglyLinkedList object
    """
    def __init__(self):
        self.__head = None

    """
    Insert Node object in sorted order
    """
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

    """
    Print list.
    """
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
