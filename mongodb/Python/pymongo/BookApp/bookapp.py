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

        elif choice == 2:
            try:
                api.all_books_forward(book_collection)
            except Exception as err:
                pass
        
        elif choice == 3:
            try:
                api.all_books_reverse(book_collection)
            except Exception as err:
                print(err)

        elif choice == 4:
            try:
                book_isbn = read_user_input("isbn")
                api.book_by_isbn(book_collection, book_isbn)
            except Exception as err:
                print(err)

        elif choice == 5:
            try:
                book_isbn = read_user_input("isbn")
                api.delete_book_by_isbn(book_collection, book_isbn)
            except Exception as err:
                print(err)

        elif choice == 6:
            try:
                api.sort_by_price_quantity(book_collection)
            except Exception as err:
                print(err)

        elif choice == 7:
            try:
                print("Enter the new book details : ")
                replace_isbn = read_user_input("isbn")
                replace_author = read_user_input("author")
                replace_price = int(read_user_input("price"))
                replace_quantity = int(read_user_input("quantity"))
                replace_book = Book(replace_isbn, replace_author, replace_price, replace_quantity)
                isbn_to_replace = input("Enter isbn for the book to replace : ")
                api.replace_book_by_isbn(book_collection, isbn_to_replace, replace_book)
            except Exception as err:
                print(err)

        elif choice == 8:
            try:
                api.delete_books_below_price(book_collection, 200)
            except Exception as err:
                print(err)

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
