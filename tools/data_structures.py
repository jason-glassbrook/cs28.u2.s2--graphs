############################################################
#   DATA STRUCTURES
############################################################

from collections import defaultdict, deque

############################################################
#   DefaultDict
############################################################

DefaultDict = defaultdict

############################################################
#   Queue
############################################################


class Queue:

    def __init__(self):

        self.__container = deque()
        return

    def __len__(self):

        return len(self.__container)

    def push(self, value):

        self.__container.append(value)
        return

    def pop(self):

        if len(self) > 0:
            return self.__container.popleft()

        else:
            return None


############################################################
#   Stack
############################################################


class Stack:

    def __init__(self):

        self.__container = deque()
        return

    def __len__(self):

        return len(self.__container)

    def push(self, value):

        self.__container.appendleft(value)
        return

    def pop(self):

        if len(self) > 0:
            return self.__container.popleft()

        else:
            return None
