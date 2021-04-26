'''
Queue to stack converter.

https://github.com/iamthewalrus67/queue-stack-converter.git
'''

from copy import copy
from arraystack import ArrayStack


def queue_to_stack(queue):
    '''
    Conver queue to stack.
    '''
    queue_copy = copy(queue)
    stack = ArrayStack()
    while queue_copy:
        stack.push(queue_copy.pop())

    result = ArrayStack()
    while stack:
        result.push(stack.pop())
    return result
