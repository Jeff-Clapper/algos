import random



def get_question():
    options = ["Arrays","Binary Search Trees","Binary Trees","Dynamic Programming","Famous Algorithms","Graphs","Greedy Algorithms","Heaps","Linked Lists","Recursion","Searching","Sorting","Stacks","Strings","Tries"]
    completed = ["Sorting", "Famous Algorithms"]

    index = random.randint(0,len(options)-1)

    while options[index] in completed:
        index = random.randint(0,len(options)-1)

    return options[index]

print(get_question())