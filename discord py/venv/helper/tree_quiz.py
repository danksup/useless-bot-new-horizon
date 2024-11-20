# tree_helpers.py
import random

def makePN(A, PN):
    return [A, PN]

def akar(PN):
    return PN[0]

def anak(PN):
    return PN[1]

def isTreeNEmpty(PN):
    return PN == []

def isOneElmt(PN):
    return not isTreeNEmpty(PN) and isTreeNEmpty(anak(PN))

def NbNElmt(PN):
    if isTreeNEmpty(PN):
        return 0
    if isOneElmt(PN):
        return 1
    return 1 + NbNElmt(anak(PN)[0]) + NbNElmtChild(anak(PN)[1:])

def NbNElmtChild(PN):
    if isTreeNEmpty(PN):
        return 0
    return NbNElmt(PN[0]) + NbNElmtChild(PN[1:])

def NbNDaun(PN):
    if isTreeNEmpty(PN):
        return 0
    if isOneElmt(PN) and isTreeNEmpty(anak(PN)):
        return 1
    return NbNDaunChild(anak(PN))

def NbNDaunChild(PN):
    if isTreeNEmpty(PN):
        return 0
    return NbNDaun(PN[0]) + NbNDaunChild(PN[1:])

def generate_random_tree(max_depth=3, max_children=3):
    """Generate a random tree structure."""
    if max_depth == 0 or random.random() < 0.2: 
        return makePN(random.randint(1, 100), [])
    
    num_children = random.randint(0, max_children)  
    children = [generate_random_tree(max_depth - 1, max_children) for _ in range(num_children)]
    return makePN(random.randint(1, 100), children)
