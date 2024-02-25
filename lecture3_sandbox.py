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
