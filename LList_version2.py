"""
单链表的变形，加入尾节点引用域
"""


class LNode(object):
    # 单链表节点类
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedListUnderFlow(ValueError):
    # 自定义异常类
    pass


class LList(object):
    # 单链表类
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, item):
        """头部添加节点"""
        self.head = LNode(item, self.head)

    def pop(self):
        """pop 头元素"""
        if self.is_empty():
            raise LinkedListUnderFlow('in pop')
        e = self.head.item
        self.head = self.head.next
        return e

    def append(self, item):
        """尾部添加节点"""
        new_node = LNode(item)
        if self.head is None:
            self.head = new_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node

    def pop_last(self):
        """pop 尾节点元素"""
        if self.head is None:
            raise LinkedListUnderFlow
        p = self.head
        if p.next is None:
            while p.next:
                p = p.next
            e = p.item
            self.head = None
            return e
        else:
            while p.next.next is not None:
                p = p.next
            e = p.next.item
            p.next = None
            return e

    def length(self):
        n = 0
        p = self.head
        while p is not None:
            p = p.next
            n += 1
        return n

    def insert(self, item, i):
        """插入元素到给定位置,重点理解"""
        if i <= 0:
            self.prepend(item)
        elif i >= self.length():
            self.append(item)
        else:
            p = self.head
            new_node = LNode(item)
            while p.next is not None and i > 1:
                p = p.next
                i -= 1
            new_node.next = p.next
            p.next = new_node

    # def remove(self,item):
    #     """删除第一个给定元素"""
    #     pre = None
    #     p = self.head
    #     while p is not None:
    #         if p.item == item:
    #             if not pre:
    #                 self.head = p.next
    #             else:
    #                 pre.next = p.next
    #             break
    #         else:
    #             pre = p
    #             p = p.next
    def remove(self, item):
        """删除第一个给定元素"""
        if self.head.item == item:
            self.head = self.head.next
        else:
            pre = self.head
            p = self.head.next
            while p is not None:
                if p.item == item:
                    pre.next = p.next
                    break
                else:
                    pre = p
                    p = p.next

    def remove_all(self, item):
        """删除全部给定元素"""
        while self.head.item == item:
            self.head = self.head.next
        pre = self.head
        p = self.head.next
        while p is not None:
            while p is not None and p.item == item:
                p = p.next
            pre.next = p
            if p is not None:
                pre = p
                p = p.next

    def find(self, pred):
        """找到满足一定条件的（第一个）元素"""
        p = self.head
        while p is not None:
            if pred(p.item):
                return p.item
            p = p.next

    def printall(self):
        """打印全部元素"""
        p = self.head
        while p is not None:
            if p.next is not None:
                print(p.item,end=' ')
            else:
                print(p.item)
            p = p.next

    def proc_all(self, proc):
        """表的遍历-->对全部元素执行操作"""
        p = self.head
        while p is not None:
            proc(p.item)
            p = p.next

    def elements(self):
        """表的遍历-->生成器"""
        p = self.head
        while p is not None:
            yield p.item
            p = p.next

    def filter(self, proc):
        """表的遍历-->筛选器"""
        p = self.head
        while p is not None:
            if proc(p.item):
                yield p.item
            p = p.next

    def reverse(self):
        """反转链表"""
        q = None
        while self.head is not None:
            p = self.head
            self.head = self.head.next
            p.next = q
            q = p
        self.head = q


class LList1(LList):
    # 单链表加入尾节点引用域
    def __init__(self):
        LList.__init__(self)
        self.rear = None

    def prepend(self,item):
        if self.head is None:
            self.head = LNode(item, self.head)
            self.rear = self.head
        else:
            self.head = LNode(item, self.head)

    def append(self,item):
        if self.head is None:
            self.head = LNode(item, self.head)
            self.rear = self.head
        else:
            self.rear.next = LNode(item)
            self.rear = self.rear.next

    def pop(self):
        """pop 头元素"""
        if self.is_empty():
            raise LinkedListUnderFlow('in pop')
        e = self.head.item
        self.head = self.head.next
        if self.head is None:
            self.rear = None
        return e

    def pop_last(self):
        if self.is_empty():
            raise LinkedListUnderFlow
        if self.head.next is None:
            e = self.head.item
            self.head = None
            return e
        else:
            p = self.head
            while p.next.next is not None:
                p = p.next
            e = p.next.item
            p.next = None
            self.rear = p
            return e

    def remove(self, item):
        """删除第一个给定元素"""
        if self.head.item == item:
            self.head = self.head.next
        else:
            pre = self.head
            p = self.head.next
            while p is not None:
                if p.item == item:
                    pre.next = p.next
                    break
                else:
                    pre = p
                    p = p.next
            self.rear = pre

    def remove_all(self, item):
        """删除全部给定元素"""
        while self.head.item == item:
            self.head = self.head.next
        pre = self.head
        p = self.head.next
        while p is not None:
            while p is not None and p.item == item:
                p = p.next
            pre.next = p
            if p is not None:
                pre = p
                p = p.next
        self.rear = pre

    def reverse(self):
        """反转链表"""
        q = None
        while self.head is not None:
            p = self.head
            self.head = self.head.next
            p.next = q
            if q is None:
                self.rear = p
            q = p
        self.head = q


if __name__ == '__main__':
    alist = LList1()
    for i in range(10):
        alist.append(i)
    # for i in range(10,20):
    #     alist.append(i)
    # alist.printall()
    a = 'a'
    # alist.insert(a, 0)
    # alist.insert(a,0)
    alist.insert(a, 10)
    alist.insert(a, 11)
    alist.printall()
    print('length:', alist.length())
    # for i in range(10):
    #     ret = alist.pop_last()
    #     print(ret)
    # alist.remove('a')
    # alist.remove_all('a')
    alist.reverse()
    alist.printall()
    print('length:', alist.length())

    # for i in alist.elements():
    #     print(i*2)

    # ret = alist.filter(lambda x:x%3 == 0)
    # for i in ret:
    #     print(i)

    # ret = alist.find(lambda x: x>3 and x % 2 == 0)
    # print(ret)
