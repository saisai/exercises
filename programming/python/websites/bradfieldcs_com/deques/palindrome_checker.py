from collections import deque

def is_palindrome(characters):

    character_deque = deque(characters)

    print(character_deque)

    while len(character_deque) > 1:
        first = character_deque.popleft()
        last = character_deque.pop()
        print('first: ', first, 'last : ', last)
        if first != last:
            return False

    return True


is_palindrome('lsdkjfskf')
is_palindrome('radar')
