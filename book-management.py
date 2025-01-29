# #!Book Management project 

#? List of Book
#?Add a Book
#?Delete a Book
#?Exit the app

import json
B = 'Book.txt'
def load_data():
    try:
        with open(B, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_data_helper(Books):
    with open(B , 'w') as file:
        json.dump(Books, file)
def list_all_Books(Books):
    print('')
    print("*" * 50)
    for index, video in enumerate(Books, start=1):
        
        print(f"{index}. {Books['name']})")
def add_BOOKS(Books):
    name = input("Enter Book name: ")
    
    Books.append({'name':name})
    save_data_helper(Books)

def delete_Books(Books):
    list_all_Books(Books)
    index = int(input("Enter the Books number to Delete: "))
    if 1<= index <= len(Books):
        del Books[index - 1]
        save_data_helper(Books)
    else:
        print("Invalid Index!")
def main():
    Books = load_data()
    while True:
        print('''
 Book Manager | choose an option:''')
        print('1. List all Books')
        print('2. Add a Book')
        print('3. Delete a Book')
        print('4. Exit the app')
        
        
        choice = input('Enter the choice: ')
        match choice:
             case '1':
                 list_all_Books(Books)
             case '2':
                 add_BOOKS(Books)
             case '3':
                 delete_Books(Books)
             case '4':
                 break
             
             case _:
                 print("Invailed choice")
if __name__ == '__main__':
    main()


