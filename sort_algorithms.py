import random, time
from typing import BinaryIO

def checkSort(arr, n, asc=True) :
    isSorted = True

    if asc==True :
        for i in range(1, n) :
            if arr[i] > arr[i+1] :
                isSorted = False
                break
    else : 
        for i in range(1, n) :
            if arr[i] < arr[i+1] :
                isSorted = False
                break    
    if isSorted :
        print("정렬완료")
    else :
        print("정렬안됨") 

def selectionSort(arr, n) :               
    for i in range(1, n) :
        minIdx = i
        for j in range(i+1, n+1) :           
            if arr[minIdx] > arr[j] :
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

def selectionSortDesc(arr, n, checkSort=False) :
    for i in range(1, n) :
        maxIdx = i
        for j in range(i+1, n+1) :
            if arr[maxIdx] < arr[j] :
                maxIdx = j
        arr[i], arr[maxIdx] = arr[maxIdx], arr[i]

        if checkSort == True :
            if isSorted(arr, n) == True :
                break

def isSorted(arr, n) :
    isSorted = True
    for i in range(1, n):
        if arr[i] > arr[i+1] :
            isSorted = False
            break
    return isSorted

def bubbleSort(arr, n, checkSort=False) :
    for i in range(n, 1, -1) :
        if checkSort == True:
            if isSorted(arr, n) == True :
                break
        for j in range(1, i) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionSort(arr, n) :
    for i in range(2, n+1) :
        v, j = arr[i], i
        while j > 1 and arr[j-1] > v:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = v

def shellSort(arr, n) :
    # 최대 간격 찾기
    h = 1
    while h*3+1 < n :
        h += 1
    h = (h-1)*3+1    
    # 계산된 간격부터 간격을 h/3씩 줄여가며 삽입정렬 
    while h > 0 :
        # print('h: ' + str(h))
        cnt = 0
        for i in range(h+1, n+1) :
            #h+1원소부터 h 배수 간격 앞에 있는 원소들과 삽입정렬
            cnt += 1
            v, j = arr[i], i
            while j > h and arr[j-h] > v :
                arr[j] = arr[j-h]
                j -= h
            arr[j] = v   
        print('h가 ' + str(h)+'일 때 그룹 수: ' + str(cnt))
        h = int(h/3)

def partition(arr, left, right) :
    pivot = arr[right]
    
    i = left-1
    j = right
    
    while True :
        i += 1
        while arr[i] < pivot :
            i += 1

        j -= 1
        while j > 0 and arr[j] > pivot:
            j -= 1

        if i >= j :
           break

        arr[i], arr[j] = arr[j], arr[i]    

    arr[i], arr[right] = arr[right], arr[i]

    return i

def quickSort(arr, left, right) :
    if left >= right :
        return
    i = partition(arr, left, right)
    # print('left : ' + str(left) + ", i: " + str(i) + ', right: ' + str(right))
    quickSort(arr, left, i-1)
    quickSort(arr, i+1, right)

def insertionSort2(arr, left, right) :
    for i in range(left+1, right+1) :
        v, j = arr[i], i
        while j > 1 and arr[j-1] > v :
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = v    
            
M = 15
def quickSort2(arr, left, right) :
    if right-left <= M :
        insertionSort2(arr, left, right)
    else :
        i = partition(arr, left, right)
        quickSort2(arr, left, i-1)
        quickSort2(arr, i+1, right)


def mergeSort(arr, left, right) :
    if (left>=right) :
        return
    mid = int((left+right)/2)
    mergeSort(arr, left, mid)    
    mergeSort(arr, mid+1, right)
    for i in range(left, right+1) : #각각 정렬된 것을 복사본에 넣고
        arr_copy[i] = arr[i]

    i, j = left, mid+1
    k = 0
    for k in range(left, right+1) :  # 반틈씩 정렬된 복사본을 전체 정렬된 순서로 원본에 반영 
        if i > mid or j > right : # 반틈 두 개 중 하나는 소진했음. 
            break
        if arr_copy[i] < arr_copy[j] :
            arr[k] = arr_copy[i]
            i += 1
        else :
            arr[k] = arr_copy[j]
            j += 1
    if i > mid :   # 소진 안된 나머지를 원본에 반영 
        start = j
        end = right+1
    else :
        start = i
        end = mid+1
    for i in range(start, end) :
        arr[k] = arr_copy[i]
        k += 1                

def heapify(arr, root, end) :
    v, j = arr[root], root*2

    while j <= end :
        if j < end and arr[j] < arr[j+1] :
            j = j+1
        if v >= arr[j] :  # 부모가 크면 더 이상 내려가지않는다. 
            break
        else :
            arr[int(j/2)] = arr[j]
        j *= 2

    arr[int(j/2)] = v

def heapSort(arr, n) :

    for i in range(int(n/2), 0, -1) :
        heapify(arr, i, n)  

    for i in range(n-1, 0, -1) :
       arr[1], arr[i+1] = arr[i+1], arr[1]
       heapify(arr, 1, i)

def countingSort(arr, n, max_value) :
    count = [0] * (max_value+1)

    for i in range(1, n+1) :
        count[arr[i]] = count[arr[i]] + 1

    for i in range(2, max_value+1) :
        count[i] = count[i-1] + count[i]     

    # print(count)
    for i in range(n, 0, -1) :
        arr_copy[count[arr[i]]] = arr[i]
        count[arr[i]] = count[arr[i]] - 1

    for i in range(1, n+1) :
        arr[i] = arr_copy[i]  


def kth_digit(value, k) :
    temp = 1
    for i in range (1, k) :
        temp *= 10
    value = int(value/temp)
    digit = value % 10
    return digit

def enqueue(queue, data) :
    queue.append(data)

def dequeue(queue) :
    if len(queue) == 0 :
        print('Queue is empty')
        return -1

    data = queue.pop(0)
    return data

def radixSort(arr, n, num_of_digits, queue) :  # queue는 2차원 배열
    # 1의 자리수부터 num_of_digits 자리수까지 반복:
    #   첫 번째 원소부터 마지막 원소까지 반복 :
    #       현재 원소의 자리 값을 보고
    #       그 값을 인덱스 값으로 enqueue 한다. 
    #   원본에 자리값에 따라 정렬된 원소를 반영하기 위해 position을 0으로 초기화
    #   자리수 값이 가질 수 있는 범위인 0~9까지 반복 i :
    #       queue의 i위치 값의 수만큼 반복 :
    #          position += 1
    #          arr[postion] = dequeue(queue[i])
    for k in range(1, num_of_digits+1) :
        for i in range(1, n+1) :
            digit = kth_digit(arr[i], k)
            enqueue(queue[digit], arr[i])
        position = 0
        for i in range(0, 10) : # 원본에 반영 
            while len(queue[i]) != 0 :
                position += 1
                arr[position] = dequeue(queue[i]) 

def cocktailShakerSort(arr, n) :
    to_the_right = True
    left = 1
    right = n
    for i in range(n, 1, -1) :
        # print("left: " + str(left) + ", right:" + str(right)+", to_the_right:" + str(to_the_right))
        if to_the_right == True :
            for j in range(left, right) :
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            right -= 1
            to_the_right = False
        else :
            for j in range(right, left, -1) :
                if arr[j] < arr[j-1] :
                    arr[j], arr[j-1] = arr[j-1], arr[j]
            left += 1
            to_the_right = True        
        
def exchangeSort(arr, n) :
    for i in range(1, n) :
        for j in range(i+1, n+1) :
            if arr[i] < arr[j] :
                arr[i], arr[j] = arr[j], arr[i]            

def merge(arr, left, mid, right):
    # print("merge lef:", left, " mid:", mid, " right:", right)
    for i in range(left, right+1) :
        arr_copy[i] = arr[i]
    
    i, j = left, mid+1
    k = 0

    for k in range(left, right+1) :
        if i > mid or j > right :
            break
        if arr_copy[i] < arr_copy[j] :
            arr[k] = arr_copy[i]
            i += 1
        else:
            arr[k] = arr_copy[j]
            j+=1

    if i > mid :
        start = j
        end = right + 1
    else:
        start = i
        end = mid+1

    for i in range(start, end) :
        arr[k] = arr_copy[i]
        k += 1
 
def naturalMergeSort(arr, n) :

    while True:
        left = 1
        mid = -1
        right = -1
        for i in range(1, n+1) :
            if i == n or arr[i] > arr[i+1] :
                if mid == -1 :
                    mid = i
                elif right == -1 :
                    right = i
                    merge(arr, left, mid, right)
                    left = i+1
                    mid = -1
                    right = -1
        if left == 1 : # run 이 하나밖에 없음
            break
def binary_search_upper_bound(arr, start, end, value) :
    while start < end :
        m = int((start + end)/2)
        if value >= arr[m] :
            start = m+1
        else :
            end = m
    return end

def binaryInsertionSort(arr, n) :
    for i in range(1, n+1) :
        value = arr[i]
        pos = binary_search_upper_bound(arr, 1, i, value)

        for j in range(i, pos, -1) :
            arr[j] = arr[j-1]
        arr[pos] = value

class Node :
    def __init__(self, key=None, left=None, right=None) :
        self.key = key 
        self.left = left
        self.right = right

class BinarTree :
    count = 0
    def __init__(self) :
        self.head = Node(-1, None, None)
    
    def insert(self, value) :
        previous = navigator = self.head

        while navigator != None :
            previous = navigator
            if navigator.key > value :
                navigator = navigator.left
            else :
                navigator = navigator.right

        navigator = Node(value, None, None)

        if previous.key > value :
            previous.left = navigator
        else :
            previous.right = navigator
      

def inorder_traverse(tree, arr) :
    if tree==None :
        return
    inorder_traverse(tree.left, arr)
    idx = BinarTree.count   # start from zero, to put head Node's key into zero index of arr
    arr[idx] = tree.key
    BinarTree.count += 1
    inorder_traverse(tree.right, arr)
    
def binaryTreeSort(arr, n) :

    tree = BinarTree()
    
    for i in range(1, n+1) :
        tree.insert(arr[i])
    
    inorder_traverse(tree.head, arr)
#tournament sort
#   선택정렬과 히프 정령의 아이디어 사용
#   먼저 배열을 사용해 이진 트리를 만든다. ⟸ 배열 b_arr
#   서로 다른 키 값을 가지는 배열 a_arr로부터 
#   n개의 원소를 이 트리의 리프로 복사
#   다음으로 가장 큰 원소가 루트에 복사될 때까지 형제 원소의 쌍 중에서
#   큰 것을 부모 노드로 복사하는 스포츠 토너먼트와 같이 진행
#   토너먼트를 통해 가장 큰 원소가 루트에 복사되면 가장 큰 원소를 
#   가지고 있는 b_arr[1]을 a_arr[n]으로 복사한다
#   그런 다음 트리를 따라 내려가면서 토너먼트에 참여한 노드 중에서
#   가장 큰 원소를 가지고 있는 노드의 키 값을 0으로 변경한다.
#   트리의 리프에 도달하면 다시 트리를 따라 올라가면서 
#   이전과 동일한 과정을 반복하면 정렬된 배열을 얻을 수 있다.

def tournamentSort(arr, n) :
    # caculates size of array representing a complete binary tree
    # find k which makes 2ᵏ equal to or larger than n
    # We need a binary tree of level k+1, and that means we need an array of the size which is sum from 2⁰ to 2ᵏ⁻¹ + n    
    
    num_of_nodes = k = 0
    # print(arr)
    # print('---------------------------------')
    while True :
        numOfElemementsOnLeafs = pow(2, k)
        num_of_nodes += numOfElemementsOnLeafs
        if numOfElemementsOnLeafs >= n :
            break
        k+=1
    num_of_nodes = num_of_nodes - pow(2, k) + n
    
    # make every node a full node
    if n%2 != 0 : 
        num_of_nodes += 1

    # print('num_of_nodes:', num_of_nodes)
    # make all the elements of arr be in the level k+1 of a binary tree
    b_arr = []
    b_arr.append(None)
    #initialize b_arr with 0s
    for i in range(1, num_of_nodes+1) :
        b_arr.append(0)
    
    #copy all the elements in arr to the leaf nodes of a complete binary tree represented by b_arr array
    idx = pow(2, k)
    for i in range(1, n+1) :
        b_arr[idx] =  arr[i]
        idx+=1
    
    # print(b_arr)
    # repeat tournament n times
    idx = n
    while idx > 0 :
        for i in range(int(num_of_nodes/2), 0, -1) :
            if b_arr[i*2] > b_arr[i*2+1]:
                b_arr[i] = b_arr[i*2]
            else :
                b_arr[i] = b_arr[i*2+1]        
        
        arr[idx] = b_arr[1]
        idx -= 1

        # print(b_arr)

        # considering dups in arr we follow only one path which has same value with a root
        j = 1
        root_value = b_arr[1]
        while j <= num_of_nodes :
            if b_arr[j] == root_value :
                b_arr[j] = 0
                j *= 2
            else :
                b_arr[j+1] = 0
                j = (j+1)*2
        
        # for j in range(2, num_of_nodes+1) :
        #     if b_arr[j] == b_arr[1] :
        #         b_arr[j] = 0
        
    # print('############################')

N = 10000
# M = N
M = 1000  # 계수정렬 때 사용. M이 너무 크면 안되니...
arr = []
arr.append(None)  # sentinel value or dummy value

num_of_digits = 5 # 기수 정렬 때 
M = 10000

for i in range(N) :
    arr.append(random.randint(1, N))
    # arr.append(random.randint(1, M))

# print(arr)
checkSort(arr, N, True)

arr_copy = arr.copy()

start_time = time.time()
# selectionSort(arr, N)

# bubbleSort(arr, N, False)
# cocktailShakerSort(arr, N)

# insertionSort(arr, N)
# shellSort(arr, N)
# quickSort(arr, 1, N)
# quickSort2(arr, 1, N)
# mergeSort(arr, 1, N)
# heapSort(arr, N)
# countingSort(arr, N, M)

# Q = []
# for i in range(10) :
#     Q.append([])
# radixSort(arr, N, num_of_digits, Q)  
# 

# selectionSortDesc(arr, N)

# exchangeSort(arr, N)
# naturalMergeSort(arr, N)
# binaryInsertionSort(arr, N)
# binaryTreeSort(arr, N)

tournamentSort(arr, N)

end_time = time.time()
print('정렬에 소요된 시간 (N=%d) : %0.3f' %(N, (end_time-start_time)))
checkSort(arr, N, True)
# print(arr)