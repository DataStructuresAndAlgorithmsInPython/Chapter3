"""
Josephus问题：
n个人围坐在一圈，要求从第k个人开始报数，报到第m个数的人退出。
然后从下一个人开始继续报数并按同样规则退出，直至所有人退出。
要求按顺序输出各出列人的编号
"""


def count(alist, n):
    num = 0
    for i in alist:
        if i == n:
            num += 1
    return num


def josephus2(n, k, m):
    """基于list类型，表元素设置为零表示人退出"""
    alist = [1 for _ in range(n)]
    blist = []
    index = k-1
    index %= n
    out_num = 0
    while out_num < n:
        i = m - 1
        while i > 0:
            index += 1
            index %= n
            if alist[index] == 0:
                continue
            else:
                i -= 1
        alist[index] = 0
        blist.append(index)
        out_num += 1
        while out_num != n and alist[index] == 0:
            index += 1
            index %= n
    print(blist)


def josephus_daan1(n, k, m):
    """基于数组概念的解法"""
    people = list(range(1, n+1))
    i = k-1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end="")
                people[i] = 0
            i = (i + 1) % n
        if num < n - 1:
            print(", ", end="")
        else:
            print()


def josephus_daan2(n, k, m):
    people = [i for i in range(1, n+1)]
    i = k-1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end="")
                people[i] = 0
            i = (i+1) % n
        if num < n-1:
            print(", ", end="")
        else:
            print()


def josephus3(n, k, m):
    """基于顺序表的解,点到人后删除"""
    # 8, 5, 3, 2, 4, 7, 1, 6, 9, 10
    people = [i for i in range(1, n+1)]
    i = k + m-2
    while n > 0:
        i = i % n
        ret = people.pop(i)
        if n > 1:
            print(ret, end=", ")
        else:
            print(ret)
        n -= 1
        if n > 0:
            i = i + m - 1


def josephus_daan3(n, k, m):
    people = list(range(1, n+1))

    num, i = n, k-1
    for num in range(n, 0, -1):
        i = (i + m-1) % num
        print(people.pop(i), end=(", " if num > 1 else "\n"))


if __name__ == '__main__':
    # josephus2(10, 2, 7)
    # [7, 4, 2, 1, 3, 6, 0, 5, 8, 9]

    # josephus_daan1(10,2,7)
    # 8, 5, 3, 2, 4, 7, 1, 6, 9, 10

    josephus3(10, 2, 7)
    josephus_daan3(10, 2, 7)
