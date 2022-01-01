import random



def get_question():
    options = ["Arrays","Binary Search Trees","Binary Trees","Dynamic Programming","Famous Algorithms","Graphs","Greedy Algorithms","Heaps","Linked Lists","Recursion","Searching","Sorting","Stacks","Strings","Tries","Starred"]
    completed = ["Sorting", "Famous Algorithms","Greedy Algorithms"]

    index = random.randint(0,len(options)-1)

    while options[index] in completed:
        index = random.randint(0,len(options)-1)

    if options[index] == "Starred":
        secondary = random.randint(0,len(options)-2)
        return [options[index],options[secondary]]
    return options[index]

print(get_question())