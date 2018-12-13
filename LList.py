"""
单链表类
"""


# 单链表节点类
class LNode(object):
    def __init__(self, item, next = None):
        self.item = item
        self.next = next


# 自定义异常类
class LinkedListUnderFlow(ValueError):
    pass


# 单链表类
class LList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # 头部添加节点
    def prepend(self, item):
        self.head = LNode(item, self.head)

    # 尾部添加节点
    def append(self, item):
        new_node = LNode(item)
        if self.head is None:
            self.head = new_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node

    # 插入元素到给定位置,重点理解
    def insert(self, item, i):
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

    # pop 头元素
    def pop(self):
        if self.is_empty():
            raise LinkedListUnderFlow('in pop')
        e = self.head.item
        self.head = self.head.next
        return e

    # pop 尾节点元素
    def pop_last(self):
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

    # 删除给定位置元素
    def remove_index(self, index):
        if index < 0 or index >= self.length():
            raise LinkedListUnderFlow(index)
        if index == 0:
            self.pop()
        else:
            p = self.head
            while index > 1:
                p = p.next
                index -= 1
            p.next = p.next.next

    # 删除第一个给定元素
    def remove(self, item):
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

    # 删除全部给定元素
    def remove_all(self, item):
        while self.head and self.head.item == item:
            self.head = self.head.next
        if self.head is not None:
            pre = self.head
            p = self.head.next
            while p is not None:
                while p is not None and p.item == item:
                    p = p.next
                pre.next = p
                if p is not None:
                    pre = p
                    p = p.next

    # 返回链表长度
    def length(self):
        n = 0
        p = self.head
        while p is not None:
            p = p.next
            n += 1
        return n

    # 找到满足一定条件的（第一个）元素
    def find(self, pred):
        p = self.head
        while p is not None:
            if pred(p.item):
                return p.item
            p = p.next
        return -1

    # 打印全部元素
    def print_all(self):
        p = self.head
        while p is not None:
            if p.next is not None:
                print(p.item,end=' ')
            else:
                print(p.item)
            p = p.next

    # 表的遍历-->对全部元素执行操作
    def proc_all(self, proc):
        p = self.head
        while p is not None:
            p.item = proc(p.item)
            p = p.next

    # 表的遍历 -->生成器
    def elements(self):
        p = self.head
        while p is not None:
            yield p.item
            p = p.next

    # 表的遍历 -->筛选器
    def filter(self, proc):
        p = self.head
        while p is not None:
            if proc(p.item):
                yield p.item
            p = p.next

    # 反转链表
    def reverse(self):
        q = None
        while self.head is not None:
            p = self.head
            self.head = self.head.next
            p.next = q
            q = p
        self.head = q

    # 单链表插入排序，继承到其他类需要修改
    def _sort1(self):
        if self.head is None:
            return
        cur = self.head.next
        while cur is not None:
            p = self.head
            x = cur.item
            while p is not cur and p.item < x:
                p = p.next
            while p is not cur:
                y = p.item
                p.item = x
                x = y
                p = p.next
            # 在循环开始前x里保存的是cur.item的值，循环结束后x是cur.item应该有的值，但是需要将这个值赋给cur.item
            cur.item = x
            cur = cur.next

    # 返回某个元素在表中第一次出现的位置，如果没有，则返回-1
    def index(self, element):
        p = self.head
        index = 0
        while p is not None:
            if p.item == element:
                return index
            else:
                index += 1
                p = p.next
        return -1

    # 5. 一个顺序表转换成一个单链表; 将一个单链表转换成一个顺序表函数见类下面
    @staticmethod
    def list_to_llist(alist):
        new_llist = LList()
        for i in alist:
            new_llist.append(i)
        return new_llist

    # 6. 反向遍历，将proc作用到每个元素
    # 使用self.reverse() 将链表反转，用self.proc_all()处理，然后再反转回原顺序
    def reverse_proc(self, proc):
        self.reverse()
        self.proc_all(proc)
        self.print_all()
        self.reverse()

    # 7.a)删除链表中的最小元素，如果有多个，则全部删除
    def del_minimal(self):
        p = self.head
        min_item = p.item
        while p is not None:
            if p.item < min_item:
                min_item = p.item
            p = p.next
        self.remove_all(min_item)

    # 7.b)删除链表中所有满足谓词条件（pred）的元素
    def del_if(self, pred):
        while self.head and pred(self.head.item):
            self.head = self.head.next
        if self.head is not None:
            pre = self.head
            p = self.head.next
            while p is not None:
                while p is not None and pred(p.item):
                    p = p.next
                pre.next = p
                if p is not None:
                    pre = p
                    p = p.next

    # 7.c)删除表中重复元素。表中任何元素第一次出现保留不动，后续与之相等的元素都删除
    """
    http://blog.csdn.net/jmh1996/article/details/78481365
    查找效率：set>dict>list
    单次查询中：看来list 就是O(n)的；
    而set做了去重，本质应该一颗红黑树（猜测，STL就是红黑树），复杂度O(logn)；
    dict类似对key进行了hash,然后再对hash生成一个红黑树进行查找，其查找复杂其实是O(logn),
    并不是所谓的O(1)。O(1)只是理想的实现，实际上很多hash的实现是进行了离散化的。
    dict比set多了一步hash的过程，so 它比set慢，不过差别不大。
    """
    """del_duplicate1() 该算法复杂度为n^3？效率极差！"""
    # def del_duplicate1(self):
    #     p = self.head
    #     index = 0
    #     while p is not None:
    #         if index != self.index(p.item):
    #             p = p.next
    #             self.remove_index(index)
    #         else:
    #             p = p.next
    #             index += 1
    """del_duplicate2() 用列表存储元素来判断是否重复"""
    # def del_duplicate2(self):
    #     cur = self.head
    #     pre = None
    #     item_list = []
    #     while cur is not None:
    #         if cur.item not in item_list:
    #             item_list.append(cur.item)
    #             pre = cur
    #             cur = cur.next
    #         else:
    #             cur = cur.next
    #             pre.next = cur
    """del_duplicate3() 用集合存储元素来判断是否重复"""
    def del_duplicate3(self):
        cur = self.head
        pre = None
        item_set = set()
        while cur is not None:
            if cur.item not in item_set:
                item_set.add(cur.item)
                pre = cur
                cur = cur.next
            else:
                cur = cur.next
                pre.next = cur

    # 8. 把另一个单链表中的元素一一交错的加入本单链表，
    # 如果某个表更长，剩余元素应该位于修改后的单链表的最后
    def inter_leaving(self, another):
        if not isinstance(another, LList):
            raise LinkedListUnderFlow("in inter_leaving")
        if self.is_empty():
            self.head = another.head
            return self.head
        elif another.is_empty():
            return self.head
        else:
            p1 = self.head
            p1_next = p1.next
            p2 = another.head
            p2_next = p2.next
            while p1_next and p2_next:
                p1.next = p2
                p2.next = p1_next
                p1 = p1_next
                p1_next = p1_next.next
                p2 = p2_next
                p2_next = p2_next.next
            p1.next = p2
            if p1_next is not None:
                p2.next = p1_next
        return self.head


# 5. 将一个单链表转换成一个顺序表
def llist_to_list(llist):
    p = llist.head
    new_list = []
    while p is not None:
        new_list.append(p.item)
        p = p.next
    return new_list


# 9.单链表插入排序函数
def llist_insert_sort(llist):
    if llist.length() < 2:
        return llist

    sorted_list = LList()
    p = llist.head
    sorted_list.append(p.item)
    if p.next.item > p.item:
        sorted_list.append(p.next.item)
    else:
        sorted_list.prepend(p.next.item)
    p = p.next.next
    while p:
        sorted_pre = None
        sorted_p = sorted_list.head
        while sorted_p and p.item > sorted_p.item:
            sorted_pre = sorted_p
            sorted_p = sorted_p.next
        if sorted_pre is None:
            sorted_list.prepend(p.item)
        else:
            new_node = LNode(p.item)
            sorted_pre.next = new_node
        p = p.next
    return sorted_list


# 10.单链表剖分函数，返回一对单链表，其中第一个包含原链表里所有满足谓词函数的节点，
# 另一个包含所有其他节点，且节点顺序与原节点相同
def partition(lst, pred):
    p = lst.head
    temp = LList()
    while p:
        if pred(p.item):
            temp.append(p.item)
        p = p.next
    lst.del_if(pred)
    return temp, lst


# 操作函数
def proc(x):
    return x*2


if __name__ == '__main__':
    # alist = LList()
    # for i in range(10):
    #     alist.prepend(i)
    # for i in range(10, 20):
    #     alist.append(i)
    # b_list = LList()
    # for i in range(0, 21):
    #     if i % 2 == 0:
    #         b_list.append(i)
    # alist.print_all()
    # b_list.print_all()
    # a = 'a'
    # alist.insert(a, 0)
    # alist.insert(a, 0)
    # alist.insert(a, 5)
    # alist.insert(a, 5)
    # alist.insert(a, 5)
    # alist.insert(a, 20)
    # alist.insert(a, 20)
    # alist.insert(a, 20)
    # alist.print_all()
    # print('length:',alist.length())
    # for i in range(10):
    #     ret = alist.pop_last()
    #     print(ret)

    # alist.remove('a')
    # alist.remove_all('a')
    # alist.reverse()
    # alist._sort1()
    # alist.print_all()
    # print('length:', alist.length())
    #
    # alist.remove_index(10)
    # alist.print_all()

    # for i in alist.elements():
    #     print(i*2)

    # ret = alist.filter(lambda x:x%3 == 0)
    # for i in ret:
    #     print(i)

    # ret = alist.find(lambda x: x>3 and x % 2 == 0)
    # print(ret)

    # alist.reverse_proc(proc)

    # 测试interleaving(self, another)
    # blist = LList()
    # alist.inter_leaving(blist)
    # alist.print_all()
    # blist.inter_leaving(alist)
    # blist.print_all()
    # for i in "abcdefgh":
    #     blist.append(i)
    # blist.print_all()
    # alist.inter_leaving(blist)
    # alist.print_all()
    # blist.inter_leaving(alist)
    # blist.print_all()

    # 测试llist_insert_sort(llist)
    # ret = llist_insert_sort(alist)
    # ret.print_all()

    # 测试def_if(self, pred)
    # alist.del_if(lambda x: x % 2 == 0)
    # alist.print_all()
    # b_list.del_if(lambda x: x % 2 == 0)
    # b_list.print_all()

    # 测试partition(lst, pred)
    # ret, lst = partition(alist, lambda x: x % 2 == 0)
    # ret.print_all()
    # lst.print_all()
    # ret2, lst2 = partition(b_list, lambda x: x % 2 == 0)
    # ret2.print_all()
    # lst2.print_all()

    # 测试del_duplicate1()
    # 测试del_duplicate2()
    alist = LList()
    for i in range(10):
        alist.prepend(i)
    for i in range(10, 20):
        alist.append(i)
    for i in range(10):
        alist.prepend(i)
    for i in range(10):
        alist.append(i)
    for i in range(5):
        alist.append(9)
    alist.print_all()
    # alist.del_duplicate1()
    # alist.del_duplicate2()
    alist.del_duplicate3()
    alist.print_all()
    blist = LList()
    for i in range(10):
        blist.append(1)
    blist.print_all()
    # blist.del_duplicate1()
    # blist.del_duplicate2()
    blist.del_duplicate3()
    blist.print_all()
