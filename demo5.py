grocery_item = ""
grocery_list = []
while grocery_item != "done":
    grocery_item = input("Please write down an item to add to your grocery list. When you are done writing the list then simply type: done")
    if grocery_item == 'done':
        continue
    else:
        print("adding the item to the list")
        grocery_list.append(grocery_item)
print("Here is our grocery list:")
print(grocery_list)

