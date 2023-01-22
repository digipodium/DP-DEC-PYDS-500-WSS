from pprint import pp
contacts = {'emergency' : 112}
while True:
    # menu
    print('1. Add contact')
    print('2. View contacts')
    print('3. Delete contact')
    print('4. Exit')
    print("Select a number:")
    ch = int(input('Enter your choice: '))
    if ch == 1:
        name = input('Enter name: ')
        number = input('Enter number: ')
        contacts[name] = number
        print("contact saved")
    elif ch == 2:
        pp(contacts, width=1)
    elif ch == 3:
        name = input('Enter name: ')
        if name in contacts:
            contacts.pop(name)
        print('contact deleted')
    elif ch == 4:
        break
    else:
        print('Invalid choice')