import sys

def initialiseStack():
    Stack = [None for i in range(10)]
    return Stack

def push(item):
    global topPointer
    if topPointer < len(myStack) - 1:
        topPointer = topPointer + 1
        myStack[topPointer] = item
        print("Item pushed ✅")
    else:
        print("⚠Stack is full, cannot push⚠")

def pop():
    global topPointer
    global basePointer
    if topPointer == basePointer - 1:
        print("⚠Stack is empty, cannot pop⚠")
    else:
        popItem = myStack[topPointer]
        myStack[topPointer] = None
        topPointer = topPointer - 1
        print("Item {} popped✅".format(popItem))
        return popItem

def peek():
    print("--------------------------")
    print("Current stack:{}".format(myStack))
    print("--------------------------")

def menu():
    while topPointer <= len(myStack):
        print("Choose procedure to perform on the stack:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        option = int(input())

        if option == 1:
            item = int(input("Input the item to push\n"))
            push(item)
        elif option == 2:
            pop()
        elif option == 3:
            peek()
        elif option == 4:
            sys.exit()
        else:
            print("Invalid option")

myStack = initialiseStack()
basePointer = 0
topPointer = -1

menu()