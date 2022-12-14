#!/usr/bin/python3
"""This function does strictly nothing."""


class Square:
    """my first class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    # getter method
    @property
    def size(self):
        return self.__size

    # property setter
    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    # 2 public instance methods
    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size > 0:
            for i in range(self.position[1]):
                print()
            for row in range(self.__size):
                print(" " * self.__position[0], end="")
                for col in range(self.__size):
                    print('#', end="")
                print()
        elif self.__size == 0:
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
