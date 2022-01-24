
def TwoSum(lst,n,target):
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if lst[i]+lst[j] == target:
                return[i,j]
n = input()
lst = [int(item) for item in n.split()]
target = int(input())
TwoSum(lst,n,target)

