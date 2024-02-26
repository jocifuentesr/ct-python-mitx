import copy
#%%
x = (1, 2, (3, 'John', 4), 'Hi')
x[0] = 8


# %%
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[::2]


# %%
x = [1, 2, [3, 'John', 4], 'Hi'] 

x[0:1]

# %%
listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

listA.sort()
listA
listA.insert(0, 100)
listA.remove(3)
listA.append(7)
listA
listA + listB

listB.sort()
listB.pop()

listB.count('a')
# listB.remove('a')

listA.extend([4, 1, 6, 3, 4])

listA.count(4)
listA.index(1)
listA.pop(4)
listA.reverse()
listA


# %%
aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
aList == bList
aList is bList
aList
bList
cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)
cList == dList
cList is dList
cList[2] = 20
cList
dList

# %%
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    new_list = []
    for i in range(len(L)):
        new_list.append(f(L[i]))
    return new_list

def f(a):
    return a + 1 

testList = applyToEach(testList, f)
print(testList)

# %%
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

applyEachTo([inc, square, halve, abs], -3)
applyEachTo([inc, square, halve, abs], 3.0)
applyEachTo([inc, max, int], -3)

# %%
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'

animals
animals['c']
#animals['donkey']
len(animals)
animals['a'] = 'anteater'
animals['a']
len(animals['a'])
'baboon' in animals
'donkey' in animals.values()
'b' in animals
animals.keys()
del animals['b']
len(animals)
animals.values()

# %%
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# %%
