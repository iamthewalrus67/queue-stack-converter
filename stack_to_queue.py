'''
Stack to queue converter.

https://github.com/iamthewalrus67/queue-stack-converter.git
'''

from copy import deepcopy
from arrayqueue import ArrayQueue


def stack_to_queue(stack):
    '''
    Conver stack to queue.
    '''
    stack_copy = deepcopy(stack)
    queue = ArrayQueue()
    while stack_copy:
        queue.add(stack_copy.pop())
    return queue
