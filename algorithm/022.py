###___масиви (array)
#import numpy as np
#arr = np.array([1, 2, 3, 4, 5])
#print(arr)# Output: array([1, 2, 3, 4, 5])

#import numpy as np

#arr = np.array([1, 2, 3, 4, 5])
#print(arr + 2)# Output: array([3, 4, 5, 6, 7])

#import numpy as np

#arr1 = np.array([1, 2, 3])
#arr2 = np.array([4, 5, 6])
#print(arr1 + arr2)# Output: array([5, 7, 9])

#import numpy as np

#arr = np.array([1, 2, 3, 4, 5])
#print(np.sum(arr))# Output: 15
#print(np.mean(arr))# Output: 3.0

#import numpy as np

#arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print(arr)


###___Списки (Lists) 
#my_list = [1, 2, 3, 4, 5]
#print(my_list)# Output: [1, 2, 3, 4, 5]

#my_list = [1, 2, 3, 4, 5]
#my_list.append(6)
#print(my_list)# Output: [1, 2, 3, 4, 5, 6]

#my_list = [1, 2, 3, 5]
#my_list.insert(3, 4)# Insert number 4 at position 3
#print(my_list)# Output: [1, 2, 3, 4, 5]

#my_list = [1, 2, 3, 4, 5]
#my_list.remove(3)# Removes number 3 from the list
#print(my_list)# Output: [1, 2, 4, 5]

#my_list = [3, 1, 4, 1, 5, 9, 2]
#my_list.sort()
#print(my_list)# Output: [1, 1, 2, 3, 4, 5, 9]

###___Словники (Dictionaries)
#my_dict = {'name': 'John', 'age': 25}
#print(my_dict)# Output: {'name': 'John', 'age': 25}

#my_dict = {'name': 'John', 'age': 25}
#print(my_dict['name'])# Output: John

#my_dict = {'name': 'John', 'age': 25}
#my_dict['age'] = 26
#print(my_dict)# Output: {'name': 'John', 'age': 26}

#my_dict = {'name': 'John', 'age': 25}
#my_dict['city'] = 'New York'
#print(my_dict)# Output: {'name': 'John', 'age': 25, 'city': 'New York'}

###___Множини (Sets)
#my_set = set([1, 2, 3, 4, 5])
#print(my_set)# Output: {1, 2, 3, 4, 5}

#my_set = {1, 2, 3, 4, 5}
#my_set.add(6)
#print(my_set)# Output: {1, 2, 3, 4, 5, 6}

#my_set = {1, 2, 3, 4, 5}
#my_set.remove(1)
#print(my_set)# Output: {2, 3, 4, 5}

#set1 = {1, 2, 3, 4, 5}
#set2 = {4, 5, 6, 7, 8}
#print(set1.union(set2))# Output: {1, 2, 3, 4, 5, 6, 7, 8}
#print(set1.intersection(set2))# Output: {4, 5}
#print(set1.difference(set2))# Output: {1, 2, 3}
#print(set1.symmetric_difference(set2))# Output: {1, 2, 3, 6, 7, 8}


###___Стек
#stack = []

#stack.append('a')
#stack.append('b')
#stack.append('c')

#print(stack)# Output: ['a', 'b', 'c']

#print(stack.pop())# Output: 'c'
#print(stack)# Output: ['a', 'b']

#def peek(stack):
#    return stack[-1]

#print(peek(stack))# Output: 'b'

#def is_empty(stack):
#    return len(stack) == 0

#print(is_empty(stack))# Output: False

#class Stack:
#    def __init__(self):
#        self.stack = []

# Додавання елемента до стеку
#    def push(self, item):
#        self.stack.append(item)

# Видалення елемента зі стеку
#    def pop(self):
#        if len(self.stack) < 1:
#            return None
#        return self.stack.pop()

# Перевірка, чи стек порожній
#    def is_empty(self):
#        return len(self.stack) == 0

# Перегляд верхнього елемента стеку без його видалення
#    def peek(self):
#        if not self.is_empty():
#            return self.stack[-1]
#s = Stack()
#s.push('a')
#s.push('b')
#s.push('c')
#print(s.peek()) # Output: 'c'
#print(s.pop())  # Output: 'c'
#print(s.peek()) # Output: 'b'
#print(s.is_empty()) # Output: False


###___Черги
#from queue import Queue

# Створюємо чергу
#q = Queue()

# Додаємо елементи
#q.put('a')
#q.put('b')
#q.put('c')

#print(q.queue)# Output: deque(['a', 'b', 'c'])

# Видаляємо елемент
#q.get()
#print(q.queue)# Output: deque(['b', 'c'])

#from queue import Queue

# Створюємо чергу
#q = Queue(maxsize = 3)

# Перевіряємо, чи черга порожня
#print(q.empty())# Output: True

# Додаємо елементи
#q.put('a')
#q.put('b')
#q.put('c')

# Перевіряємо, чи черга повна
#print(q.full())# Output: True

# Перевіряємо розмір черги
#print(q.qsize())# Output: 3

# Видаляємо елементи
#print(q.get())# Output: 'a'
#print(q.get())# Output: 'b'

#from queue import Queue
#import random

#class Client:
#    def __init__(self, name):
#        self.name = name
#        self.operations = random.randint(1, 5)# Випадкова кількість операцій

#class Bank:
#    def __init__(self):
#        self.clients = Queue()

#    def new_client(self, client):
#        self.clients.put(client)

#    def serve_clients(self):
#        while not self.clients.empty():
#            current_client = self.clients.get()
#            print(f"Обслуговуємо клієнта {current_client.name} з {current_client.operations} операцій")
# Тут можна додати час обслуговування та іншу логіку

# Створюємо банк
#bank = Bank()

# Додаємо клієнтів
#for i in range(5):
#    bank.new_client(Client(f"Client-{i}"))

# Обслуговуємо клієнтів
#bank.serve_clients()

###___Двостороння черга
#from collections import deque

#d = deque()
#print(d)  # deque([])

#d.append('right')
#d.appendleft('left')
#print(d)  # deque(['left', 'right'])

#d.pop()
#d.popleft()
#print(d)  # deque([])
#d.extend(['a', 'b', 'c'])
#d.extendleft(['x', 'y', 'z'])
#print(d)  # deque(['z', 'y', 'x', 'a', 'b', 'c'])

#d.rotate(2)
#print(d)  # deque(['b', 'c', 'z', 'y', 'x', 'a'])

#d.rotate(-2)
#print(d)  # deque(['z', 'y', 'x', 'a', 'b', 'c'])

#d = deque(maxlen=3)
#d.extend([1, 2, 3])
#print(d)  # deque([1, 2, 3])

#d.append(4)
#print(d)  # deque([2, 3, 4])

#d = deque([1, 2, 3, 4, 2, 5])
#print(d.count(2))  # 2


###___Зв'язані списки
class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
  print(element.data)
