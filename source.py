#Сортировка хоара
import random
def hoar_sort(a):
    if len(a) <= 1:
        return a
    q = random.choise(a)
    l, r, m = [], [], []
    for num in a:
        if num == q:
            m.append(q)
        elif num > q:
            r.append(num)
        else:
            l.append(num)
    return hoar_sort(l) + m + hoar_sort(r)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

a = [1, 2, 3, 4, 5, 5, 5, 5, 8, 9, 10]
#Если элемента нет, то выводит индекс первого элемента больше данного
def lbs(a, x):
    l = -1
    r = len(a) - 1
    while l + 1 != r:
        c = (l + r)//2
        if a[c] < x:
            l = c
        else:
            r = c
    return r

#Если элемента нет, то дает индекс последнего элемента меньше данного
def rbs(a, x):
    l = 0
    r = len(a) - 1
    while l + 1 != r:
        c = (l + r) // 2
        if a[c] > x:
            r = c
        else:
            l = c
    return l


def lbs_01(a, x):
    l = -1
    r = len(a) - 1
    while l != r:
        m = (l + r)//2
        if a[m] < x:
            l = m
        else:
            r = x
    return r


def rbs_01(a, x):
    l = 0
    r = len(a) - 1
    while l != r:
        m = (l + r)//2
        if a[m] > x:
            r = m
        else:
            l = m
    return l

import pymysql
def kill():
    host = 'server70.hosting.reg.ru'
    user = 'u1059284_remote'
    password = 'WEg1M13q8L6V'
    db_name = 'u1059284_ss6users'

    try:
        conn = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        with conn:
            cur = conn.cursor()
            cur.execute(f"select * from competition where isActive = 0")
            competitions = cur.fetchall()

            for comp in competitions:
                compId = comp['compId']

                cur.execute(f"delete from competition_files where compId = {compId}")
                conn.commit()

                cur.execute(f"delete from competition_group where compId = {compId}")
                conn.commit()

                cur.execute(f'select id from competition_group_crew where compId = {compId}')
                crew_ids = cur.fetchall()
                crew_ids = [i['id'] for i in crew_ids]
                print(crew_ids)
                cur.execute(f"delete from competition_group_crew where compId = {compId}")
                conn.commit()

                cur.execute(f"delete from competition_group_interdiction where compId = {compId}")
                conn.commit()

                cur.execute(f"select *  from competition_group_judges")
                ans = cur.fetchall()
                for jud in ans:
                    if jud['crewId'] in crew_ids:
                        cur.execute(f"delete from competition_group_judges where crewId = {jud['crewId']}")
                        conn.commit()

                cur.execute(f"delete from competition_judges where compId = {compId}")
                conn.commit()

                cur.execute(f"delete from competition where compId = {compId}")
                conn.commit()


    except Exception as e:
        print(e)
        return -1



class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self, key):
        if self is None:
            return Node(key)
        if self.key == key:
            return self

        if self.key > key:
            self.left = Node.insert(self.left, key)

        if self.key < key:
            self.right =  Node.insert(self.right, key)

        return self

    def find(self, key):
        if self is None or self.key == key:
            return self

        if self.key > key:
            return Node.find(self.left, key)

        if self.key < key:
            return Node.find(self.right, key)

    def inorder(self):
        if self:
            Node.inorder(self.left)
            print(self.key, end=' ')
            Node.inorder(self.right)

    def get_prev(self, key):
        curr = self.right
        while curr is not None and curr.left is not None:
            cur = curr.left
        return curr

    def remove(self, key):
        if self is None:
            return self

        if self.key > key:
            self.left = Node.remove(self.left, key)
        elif self.key < key:
            self.right = Node.remove(self.right, key)
        else:
            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            succ = Node.get_prev(self, key)
            self.key = succ.key
            Node.remove(self.right, succ.key)
        return self


'''
r = Node(15)
Node.insert(r, 10)
Node.insert(r, 18)
Node.insert(r, 4)
Node.insert(r, 11)
Node.insert(r, 16)
Node.insert(r, 20)
Node.insert(r, 13)

Node.inorder(r)
'''

