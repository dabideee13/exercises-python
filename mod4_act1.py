# mod4_act1.py

"""
Tasks
1. Create a Record Keeping App
2. The application will ask the user to choose between:
    a. Add Data
    b. Delete Data
    c. End
3. If Add Data, the application will ask the user to input key and
    its value
    a. Enter Key: Lastname
    b. Enter Value: Doe
4. Store the information in a dictionary
5. Display the result
6. If Delete Data, the application will ask for the key
    a. Enter Key: Lastname
7. Remove the item from the dictionary
8. Display the result
9. If End, display THANK YOU
"""

data_storage = dict()
counter = 0

while True:

    print("Choose: Add Data, Delete Data, End\n")
    choice = input("Action: ")

    if choice.lower() == 'add data':

        key = input("Enter Key: ")
        val = input("Enter Value: ")

        if key not in data_storage.keys():
            data_storage[key] = val

        else:

            if counter == 0:
                data_storage[key] = [data_storage[key]]
                data_storage[key].append(val)

                counter += 1

            else:
                data_storage[key].append(val)

        print(data_storage, '\n')

    if choice.lower() == 'delete data':

        key = input("Enter Key: ")
        data_storage.pop(key)

        print(data_storage, '\n')

    if choice.lower() == 'end':
        print("THANK YOU")
        break