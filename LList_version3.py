"""
循环单链表
"""


class LNode(object):
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedListUnderFlow(ValueError):
    pass


class LCNode(object):
    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear is None

    def prepend(self, item):
        p = LNode(item)
        if self.is_empty():
            self.rear = p
            p.next = p
        else:
            p.next = self.rear.next
            self.rear.next = p

    def append(self, item):
        self.prepend(item)
        self.rear = self.rear.next

    def pop(self):
        if self.is_empty():
            raise LinkedListUnderFlow('in pop')
        p = self.rear.next
        if self.rear == p:
            self.rear = None
        else:
            self.rear.next = p.next
        return p.item

    def pop_last(self):
        if self.is_empty():
            raise LinkedListUnderFlow("in pop_last")
        ret = self.rear.item
        p = self.rear
        if p.next == self.rear:
            self.rear = None
        else:
            while p.next != self.rear:
                p = p.next
            p.next = self.rear.next
            self.rear = p
        return ret

    def pop_index(self, index):
        p = self.rear
        while index > 0:
            p = p.next
            index -= 1
        if p.next == self.rear:
            self.pop_last()
        elif p == self.rear:
            self.pop()
        else:
            ret = p.next.item
            p.next = p.next.next
            return ret

    def length(self):
        p = self.rear
        if p is None:
            return 0
        count = 1
        while p.next is not self.rear:
            p = p.next
            count += 1
        return count

    def printall(self):
        if self.is_empty():
            print('列表为空')
            return
        p = self.rear.next
        while True:
            if p is not self.rear:
                print(p.item, end=", ")
            else:
                print(p.item)
                break
            p = p.next


if __name__ == '__main__':
    lclist = LCNode()
    print(lclist.is_empty())
    print(lclist.length())
    #
    # for i in range(10):
    #     lclist.append(i)
    # lclist.printall()
    #
    # for i in range(11,15):
    #     lclist.prepend(i)
    # lclist.printall()
    #
    # print(lclist.is_empty())
    # print(lclist.length())
    #
    # print("-"*30)
    # print(lclist.pop())
    # print(lclist.pop_last())
    # lclist.printall()
    # print(lclist.length())
