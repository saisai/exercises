import enum

class entry_not_found(Exception):
    """Raised when an entry is not found in a collection"""
    pass

class entry_already_exists(Exception):
    """Raised when an entry already exists in a collection"""
    pass

class state(enum.Enum):
    header = 0
    left_high = 1
    right_high = 2
    balanced = 3

class direction(enum.Enum):
    from_left = 0
    from_right = 1

from abc import ABC, abstractmethod

class comparer(ABC):
    @abstractmethod
    def compare(self, t):
        pass

class node(comparer):

    def __init__(self):
        self.parent = None
        self.left = self
        self.right = self
        self.balnace = state.header

    def compare(self, t):
        if self.key < t:
            return -1
        elif t < self.key:
            return 1
        else:
            return 0

    def is_header(self):
        return self.balance == state.header

    def length(self):
        if self != None:
            if self.left != None:
                left = self.left.length()
            else:
                left = 0
            if self.right != None:
                right = self.right.length()
            else:
                right = 0

            return left + right + 1
        else:
            return 0

    def rotate_left(self):
        _parent = self.parent
        x = self.right
        self.parent = x
        x.parent = _parent
        if x.parent is not None:
            x.left.parent = self
        self.right = x.left
        x.left = self
        return x

    def rotate_right(self):
        _parent = self.parent
        x = self.left
        self.parnt = x
        x.parent = _parent
        if x.right is not None:
            x.right.parent = self
        self.left = x.right
        x.right = self
        return x

    def balance_left(self):
        _left = self.left

        if _left is None:
            return None

        if _left.balance == state.left.high:
            self.balance = state.balanced
            _left.balance = state.balanced
            self = self.rotate_right()
        elif _left.balance == state.right_high:
            subright = _left.right
            if subright.balance == state.balanced:
                self.balance = state.balanced
                _left.balance = state.balanced
            elif subright.balance == state.right_high:
                self.balance = state.balanced
                _left.balance = state.left_high
            elif subright.balance == left_high:
                root.balance = state.right_high
                _left.balance = state.balanced
            subright.balance = state.balanced
            _left = _left.rotate_left()
            self.left = _left
            self = self.rotate_right
        elif _left.balance == state.balanced:
            self.balance = state.left_high
            _left.balance = state.right_high
            self = self.rotate_right()
        return self

