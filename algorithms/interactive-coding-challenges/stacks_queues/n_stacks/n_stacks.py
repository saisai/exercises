
class Stacks:

    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.stack_pointers = [-1] * self.num_stacks
        self.stack_array = [None] * self.num_stacks * self.stack_size

    def abs_index(self, stack_index):
        return stack_index * self.stack_size + self.stack_pointers[stack_index]

    def push(self, stack_index, data):
        if self.stack_pointers[stack_index] == self.stack_size - 1:
            raise Exception('Stack is full')
        self.stack_pointers[stack_index] += 1
        array_index = self.abs_index(stack_index)
        self.stack_array[array_index] = data

    def pop(self, stack_index):
        if self.stack_pointers[stack_index] == -1:
            raise Exception('Stack is empty')
        array_index = self.abs_index(stack_index)
        data = self.stack_array[array_index]
        self.stack_array[array_index] = None
        self.stack_pointers[stack_index] -= 1
        return data


import unittest


class TestStacks(unittest.TestCase):

    def test_pop_on_empty(self, num_stacks, stack_size):
        print('Test: Pop on empty stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.pop(0)

    def test_push_on_full(self, num_stacks, stack_size):
        print('Test: Push to full stack')
        stacks = Stacks(num_stacks, stack_size)
        for i in range(0, stack_size):
            stacks.push(2, i)
        stacks.push(2, stack_size)

    def test_stacks(self, num_stacks, stack_size):
        print('Test: Push to non-full stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.push(0, 1)
        stacks.push(0, 2)
        stacks.push(1, 3)
        stacks.push(2, 4)

        print('Test: Pop on non-empty stack')
        self.assertEqual(stacks.pop(0), 2)
        self.assertEqual(stacks.pop(0), 1)
        self.assertEqual(stacks.pop(1), 3)
        self.assertEqual(stacks.pop(2), 4)

        print('Success: test_stacks\n')


def main():
    num_stacks = 3
    stack_size = 100
    test = TestStacks()
    test.assertRaises(Exception, test.test_pop_on_empty, num_stacks,
                      stack_size)
    test.assertRaises(Exception, test.test_push_on_full, num_stacks,
                      stack_size)
    test.test_stacks(num_stacks, stack_size)


if __name__ == '__main__':
    main()

