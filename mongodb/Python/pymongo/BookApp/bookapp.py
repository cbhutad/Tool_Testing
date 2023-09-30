from db import client
from api import api
from entities.book import Book

def start():
    
    mongoclient = client.create_client()
    bookappdb = client.database(mongoclient, "bookapp")
    book_collection = client.collection(bookappdb, "books") 

    isbn = None
    author = None
    price = None
    quantity = None
    choice = -1

    while choice != 0 and choice < 9:
        choice = menu()

        if choice == 0:
            break
        
        elif choice == 1:
            isbn = read_user_input("isbn")
            author = read_user_input("author")
            price = int(read_user_input("price"))
            quantity = int(read_user_input("quantity"))
            
            newbook = Book(isbn, author, price, quantity)

            try:
                api.add_book(book_collection, newbook)
            except Exception as err:
                pass



def menu():
    print("0. Exit.")
    print("1. Add a new Book.")
    print("2. Display all books in forward order.")
    print("3. Display all books in reverse order.")
    print("4. Search a given book with isbn.")
    print("5. Delete a book for given isbn.")
    print("6. Sort all books in descending order.")
    print("7. Replace book at given index with a new book.")
    print("8. Remove all books with price < 200.")
    return int(read_user_input("choice"))

def read_user_input(inputData):
    return input(f"Enter {inputData} : \n")


if __name__ == "__main__":
    start()

