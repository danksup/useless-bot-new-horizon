# problem_generator.py
import random
from .tree_quiz import generate_random_tree, NbNElmt, NbNDaun, isTreeNEmpty, isOneElmt
from .math_quiz import *

def generate_problems():
    problems = [
       {
            "code": f"def UnknownFunc(n):\n    if n == 0:\n        return 1\n    return n * UnknownFunc(n - 1)\n\nprint(UnknownFunc({random.randint(1, 5)}))",
            "expected_output": str(factorial(random.randint(1, 5))) 
        },
        {
            "code": f"def UnknownFunc(n):\n    if n <= 1:\n        return n\n    return UnknownFunc(n - 1) + UnknownFunc(n - 2)\n\nprint(UnknownFunc({random.randint(5, 10)}))",
            "expected_output": str(fibonacci(random.randint(5, 10))) 
        },
        {
            "code": f"def UnknownFunc(n):\n    total = 0\n    for i in range(1, n + 1):\n        total += i\n    return total\n\nprint(UnknownFunc({random.randint(1, 10)}))",
            "expected_output": str(sum(range(1, random.randint(1, 10) + 1))) 
        },
        {
            "code": f"def digital_root(n):\n    if n < 10:\n        return n\n    return digital_root(sum(int(digit) for digit in str(n)))\n\nprint(digital_root({random.randint(1000, 99999)}))",
            "expected_output": str(digital_root(random.randint(1000, 99999)))
        }
    ]
    
    for _ in range(4):
        tree = generate_random_tree(max_depth=random.randint(2, 4), max_children=random.randint(1, 3))
        problem_type = random.choice(["NbNElmt", "NbNDaun", "isTreeNEmpty", "isOneElmt"])
        
        if problem_type == "NbNElmt":
            problems.append({
                "code": f"def NbNElmt(PN):\n    if isTreeNEmpty(PN):\n        return 0\n    if isOneElmt(PN):\n        return 1\n    return 1 + NbNElmt(anak(PN)[0]) + NbNElmtChild(anak(PN)[1:])\n\nprint(NbNElmt({tree}))",
                "expected_output": str(NbNElmt(tree))
            })
        elif problem_type == "NbNDaun":
            problems.append({
                "code": f"def NbNDaun(PN):\n    if isTreeNEmpty(PN):\n        return 0\n    if isOneElmt(PN) and isTreeNEmpty(anak(PN)):\n        return 1\n    return NbNDaunChild(anak(PN))\n\nprint(NbNDaun({tree}))",
                "expected_output": str(NbNDaun(tree))
            })
        elif problem_type == "isTreeNEmpty":
            problems.append({
                "code": f"def isTreeNEmpty(PN):\n    return PN == []\n\nprint(isTreeNEmpty({tree}))",
                "expected_output": str(isTreeNEmpty(tree))
            })
        elif problem_type == "isOneElmt":
            problems.append({
                "code": f"def isOneElmt(PN):\n    return not isTreeNEmpty(PN) and isTreeNEmpty(anak(PN))\n\nprint(isOneElmt({tree}))",
                "expected_output": str(isOneElmt(tree))
            })
    
    return problems
