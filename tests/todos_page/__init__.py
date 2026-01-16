import random

def getListOfTasksToAdd():
    listPotentialTasks = [
        "feed the goldfish",
        "walk the dog",
        "have a haircut",
        "cook your girlfriend something nice",
        "fill up the petrol",
        "take the trash out",
        "jog up to 5km"
    ]

    numTasksToAdd = random.randrange(1,len(listPotentialTasks))
    arrTasksToAdd = []
    while numTasksToAdd > 0:
        selectedTask = random.choice(listPotentialTasks)
        while selectedTask in arrTasksToAdd:
            selectedTask = random.choice(listPotentialTasks)
        arrTasksToAdd.append(selectedTask)
        numTasksToAdd -= 1
    return arrTasksToAdd




if __name__=='__main__':
    print(f"numTasksToAdd: {getListOfTasksToAdd()}")


