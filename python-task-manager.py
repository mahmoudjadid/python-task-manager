
queue=[]

title=input("enter task title : ")
duration=int(input("enter duration for this tank : "))
prior=int(input("enter the prioriy : "))

def isempty():
     return len(queue)==0 
        
def task(title, duration, prior):
    if isempty :
        print('no tasks')
    for i in task(prior):
        if max(prior):
            print(title)
            i-=1
    
def search_for_task(title):
    left=0
    right=len(task)-1
    mid=(left+right)//2
    while left <= right :
        if mid == title :
            return mid
        elif prior(title)<prior(mid):
            right = mid+1
        else :
            left = mid + 1 
            



