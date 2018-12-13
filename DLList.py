"""
双链表类
"""


# 双链表节点类
class DLNode(object):
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev


# 自定义异常类
class LinkedListUnderFlow(ValueError):
    pass


# 双链表类
class DLList(object):
    def __init__(self):
        self.head = None
        self.rear = None

    # 判断是否为空
    def is_empty(self):
        return self.head is None

    # 返回链表长度
    def length(self):
        n = 0
        p = self.head
        while p is not None:
            p = p.next
            n += 1
        return n

    # 打印双链表
    def print_all(self):
        p = self.head
        while p is not None:
            if p.next is not None:
                print(p.item, end=' ')
            else:
                print(p.item)

    # 在双链表前端插入数据
    def prepend(self, item):
        p = DLNode(item)
        if self.is_empty():
            self.head = p
            self.rear = p
        else:
            p.next = self.head
            self.head.prev = p
            self.head = p

    # 在双链表末端插入数据
    def append(self, item):
        new_node = DLNode(item)
        if self.is_empty():
            self.head = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node

    # pop头元素
    def pop(self):
        if self.is_empty():
            raise LinkedListUnderFlow('in pop')
        e = self.head.item
        p = self.head
        if self.rear is p:
            self.head, self.rear = None, None
        else:
            self.head = self.head.next
            self.head.prev = None
        return e

    # pop尾元素
    def pop_last(self):
        if self.is_empty():
            raise LinkedListUnderFlow('in pop')
        e = self.rear.item
        p = self.rear
        if self.head is p:
            self.rear, self.head = None, None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        return e

    # 查找元素是否存在，存在返回True，不存在返回False
    def search(self, item):
        p = self.head
        while p is not None:
            if p.item == item:
                return True
            p = p.next
        return False
