import project


Data = project.Record()



while True:
    print('==== Contacts Book ====')
    print('1. Add Contact')
    print('2. Update Contact')
    print('3. Delete Contact')
    print('4. List Contacts')
    print('0. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        name = str(input('Enter name: '))
        email = str(input('Enter email: '))
        phone = str(input('Enter phone: '))
        address = str(input('Enter address: '))
        Data.add(name, email, phone, address)
    elif choice == '2':
        name = str(input('Enter name to update: '))
        phone = str(input('Enter new phone: '))
        Data.update(name,phone)
    elif choice == '3':
        name = str(input('Enter name to delete: '))
        Data.delete(name)
    elif choice == '4' :
        Data.list()    
    elif choice == '0':
        break
    else:
        print('Invalid choice. Please try again.')