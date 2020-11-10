class node :
    def __init__(self, key=None) :
        self.key = key

class Dict:
    def __init__(self) :
        Dict.a = []

    def sequential_search(self, search_key) :
        i = 0
        n = len(Dict.a)
        while(i < n and Dict.a[i].key != search_key) :
            i += 1
        if i==n :
            return -1
        else :
            return i
    
    def binary_search(self, search_key) :
        left = 0
        right = len(Dict.a) - 1

        while right >= left :
            mid = int((left+right)/2)
            if Dict.a[mid].key == search_key :
                return mid
            if Dict.a[mid].key > search_key :
                right = mid - 1
            else :
                left = mid + 1

        return -1

    def insert(self, v) :
        Dict.a.append(node(v))

import random, time

N = 10000

key = list(range(1, N+1))

search_key = list(range(1, N+1))

# In case of binary search, search keys are suffled because you need sorted records
random.shuffle(search_key)  

d = Dict()

for i in range(N) :
    d.insert(key[i])

start_time = time.time()

for i in range(N) :
    result = d.binary_search(search_key[i])
    if result==-1 or key[result] != search_key[i] :
        print("탐색오류")

end_time = time.time() - start_time

print('탐색 실행 시간 (N=%d) : %0.3f'%(N, end_time))
print('탐색 완료')

