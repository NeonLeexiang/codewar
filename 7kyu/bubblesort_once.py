def bubblesort_once(l):
    l = l[:]
    stay = 0
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            stay = l[i]
            l[i] = l[i+1]
            l[i+1] = stay
    return l
    
 
 """
 严格的说，python没有赋值，只有名字到对象的绑定。

所以L1=L是把L所指的对象绑定到名字L1上，而L2=L[:]则是把L通过切片运算取得的新列表对象绑定到L2上。前者两个名字指向同一个对象，后者两个名字指向不同对象。

换句话说，L1和L是指的同一个东西，那么修改L1也就修改了L；L2则是不同的东西，修改L2不会改变L。

注意这个引用的概念对于所有的东西都成立，例如容器内部存储的都是引用……


 

L1 = L
以前有一套三室一厅的房子，户主叫L。后来L和L1结婚，房产证上户主的名字加了一个，但房子还是只有一套。
L如果把客厅刷成了蓝色，那L1回家的时候会发现客厅是蓝色的了。

L1 = L[:]
从前有一套三室一厅的房子，户主叫L。后来有个叫L1的，觉得L的房子不错，于是买了一套相同户型的，也装修得一模一样。
后来L把自己的客厅刷成了蓝色，L1回家发现自己家的客厅还是白色，并没有变成蓝色。

 """
 
 
 """
 def bubblesort_once(l):
    l = l[:]
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    return l
 """
 
 
 """
 def bubblesort_once(lst):
    arr = lst[:]
    for i in range(len(arr)-1):
        arr[i], arr[i+1] = sorted([arr[i], arr[i+1]])
    return arr
 """
