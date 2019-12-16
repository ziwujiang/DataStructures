''' 循环链表约瑟夫环'''

# 首先定义一个结点类
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


# 再定义一个循环链表类
class LCList:
    # 初始化尾结点
    def __init__(self):
        self._rear = None

    # 判断是否为空
    def is_empty(self) -> bool:
        return self._rear is None

    # 从前端插入数据
    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p
        # 从尾端插入

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

        # 从前端弹出元素

    def pop(self):
        if self._rear is None:
            raise ValuError('in pop of CLList')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

        # 输出所有表元素

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while p is not self._rear:
            print(p.elem)
            p = p.next


# 定义约瑟夫环类，继承自循环链表类
class josephus(LCList):
    # 定义一个新方法用于实现结点环的循环
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        super().__init__()
        for i in range(n):
            self.append(i + 1)
        # 从第k个人开始报数，将此元素移动到表头
        self.turn(k - 1)
        # 开始循环报数
        while not self.is_empty():
            self.turn(m - 1)  # 把报数到m人移动到表头
            p = self.pop()
            print(p, end='\n' if self.is_empty() else ', ')
