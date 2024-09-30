def GreedyChange(money): # uses a integer or float as input
    
    change={"0.01":0,
            "0.05":0,
            "0.1":0,
            "0.25":0,
            "0.5":0,
            "1.0":0,
            "2.0":0,
            "5.0":0,
            "10.0":0,
            "20.0":0,
            "50.0":0,
            "100.0":0}
    
    change_back=0
    while money>0:
        for key in change:
            if float(key)<=money and float(key)>change_back:
                change_back=float(key)
                change_back=round(change_back,2)
        
        change[str(change_back)]+=1
        
        money-=change_back
        money=round(money,2)
        change_back=0
    
    keepers=[]    
    for key in change:
        if change[key]!=0:
            keepers+=[key]
    
    change={key: change[key] for key in change if key in keepers}
    
    return(change)
        
def RecursiveChange(money,coins): # coins : list of integers. ATTENTION: VERY SLOW!!
    if money == 0:
        return 0
    minNumCoins = float("inf")
    for i in coins:
        if money>=i:
            numCoins=RecursiveChange(money-i, coins)
            if numCoins + 1 < minNumCoins:
                minNumCoins = numCoins + 1
    return minNumCoins


def DPChange(money,coins): # coins : list of integers.
    MinNumCoins=[0]
    for m in range(money+1):
        MinNumCoins+=[float("inf")]
        for i in coins:
            if m>=i:
                if MinNumCoins[m-i]+1 < MinNumCoins[m]:
                    MinNumCoins[m]=MinNumCoins[m-i]+1
    return MinNumCoins[money]
    


def SouthOrEast(i,j,Wi=0,Wj=0):
    
    if i==0 and j==0:
        return 0
    
    x=-float("inf")
    y=-float("inf")
    
    if i>0:
        x=SouthOrEast(i-1,j)+ Wi
    
    if j>0:
        y=SouthOrEast(i,j-1)+ Wj
    
    return max(x,y)        

 

def LongestPath(graph): # graph : list of lists of numbers
    
    edges=[[-float("inf") for x in line] for line in graph]
    edges[0][0]=0
    
    graph=sum(graph,[])
    edges=sum(edges,[])
    
    for b in range(len(graph)):
        edges[b]=max([sum(x) for x in zip(graph[:b+1],edges[:b+1])])

    return edges[-1]


def merge(L1,L2):
    sorted_list=[]
    l1=L1
    l2=L2
    while l1!=[] and l2!=[]:
        if min(l1)<min(l2):
            sorted_list+=[min(l1)]
            l1.remove(min(l1))
        else:
            sorted_list+=[min(l2)]
            l2.remove(min(l2))
    if l1!=[]:
        while l1!=[]:
            sorted_list +=[min(l1)]
            l1.remove(min(l1))
    if l2!=[]:
        while l2!=[]:
            sorted_list +=[min(l2)]
            l2.remove(min(l2))
    return sorted_list

def MergeSort(List):
    if len(List)<=1:
        return List
    half=int(len(List)/2)
    first_half = List[:half]
    second_half = List[half:]
    sorted_first_half = MergeSort(first_half)
    sorted_second_half = MergeSort(second_half)  
    sorted_list=merge(sorted_first_half,sorted_second_half)
    return sorted_list







