class Node :
    def __init__(self, key=None, left=None, right=None) :
        self.key = key
        self.left = left
        self.right = right

class BinaryTree :
    def __init__(self) :
        # self.last = Node(key=0, left=0, right=0) 
        # self.last.left = self.last
        # self.last.right = self.last
        # self.head = Node(key=0, left=0, right = self.last) # head의 right은 last를 가리키도록 초기화
        self.head = Node(key=0)

    def binary_tree_search(self, search_key) :
        # navigator = self.head.right # head의 right부터 시작한다
        navigator = self.head
        # while navigator != self.last :           
        while navigator != None :
            if navigator.key == search_key :
                return navigator.key
            if navigator.key > search_key :
                navigator = navigator.left  # 현재 노드의 key가 탐색 key보다 크면 현재 노드의 왼쪽으로 탐색
            else :
                navigator = navigator.right
        
        return -1

    def insert(self, value) :
        navigator = previous = self.head
        
        # while navigator != self.last :
        while navigator != None :
            previous = navigator
            if navigator.key== value :  # already exists then no insert? no dups allowed?
                return 
            if navigator.key > value :
                navigator = navigator.left
            else :
                navigator = navigator.right
        
        # navigator = Node(key=value, left=self.last, right=self.last)
        navigator = Node(key=value)
        if previous.key > value :
            previous.left = navigator
        else :
            previous.right = navigator    

def inorder_traverse(tree) :
    if tree==None :
        return
    inorder_traverse(tree.left)
    print(tree.key)
    inorder_traverse(tree.right)

import random, time

N = 100
keys = list(range(1, N+1))
search_keys = list(range(1, N+1))
random.shuffle(keys)

tree = BinaryTree()

for i in range(N) :
    tree.insert(keys[i])

# inorder_traverse(tree.head)

start_time = time.time()

for i in range(N) :
    result = tree.binary_tree_search(search_keys[i])
    if result == -1 or result != search_keys[i] :
        print('탐색오류')

end_time = time.time() - start_time
print('탐색의 실행시간(N=%d) : %0.3f'%(N, end_time))
print('탐색완료')