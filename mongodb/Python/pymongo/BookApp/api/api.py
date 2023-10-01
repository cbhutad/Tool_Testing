import pymongo

def add_book(bookcollection, newbook):
    if bookcollection.find_one({"isbn": newbook.isbn }):
        print("Book already exists")
    
    bookcollection.insert_one(newbook.mapper_no_id())
    print("Book added successfully")

def all_books_forward(bookcollection):
    if bookcollection.count_documents({}) > 0:
        books = bookcollection.find({})
        print("Books in forward direction : \n")
        print_books(books)
    else:
        print("No books added")

def all_books_reverse(bookcollection):
    if bookcollection.count_documents({}) > 0:
        books = bookcollection.find({}).sort("_id", -1)
        print("Books in reverse direction : \n")
        print_books(books)
    else:
        print("No books added")


def book_by_isbn(bookcollection, isbn):
    book = bookcollection.find_one({"isbn" : isbn})
    if book != None:
        print()
        for key in book.keys():
            if key != "_id":
                print(f"{key} : {book[key]}")
        print()
    else:
        print(f"Mentioned book with ISBN : {isbn} not in stock")

def delete_book_by_isbn(bookcollection, isbn):
    result = bookcollection.delete_one({"isbn" : isbn})
    if result.acknowledged == True:
        print("Book deleted successfully")
    else :
        print(f"Book with ISBN : {isbn} not in stock")

def sort_by_price_quantity(bookcollection):
    if bookcollection.count_documents({}) > 0:
        books = bookcollection.find().sort([("price", pymongo.DESCENDING), ("quantity", pymongo.ASCENDING)])
        print_books(books)
    else:
        print("No books added")

def delete_books_below_price(bookcollection, price):
    if bookcollection.count_documents({}) > 0:
        result = bookcollection.delete_many({"price" : {"$lt" : 200}})
        if result.acknowledged == True:
            print("Books removed successfully")
        else:
            print("No book under given price tag present")
    else:
        print("No books added")

def replace_book_by_isbn(bookcollection, isbn, book):
    originalbook = bookcollection.find_one({"isbn" : isbn})
    if originalbook != None:
        result = bookcollection.find_one_and_replace({"isbn" : isbn}, book.mapper_no_id())
        if result["_id"] == originalbook["_id"]:
            print("Book replaced successfully")
    else :
        print(f"Mentioned book with ISBN : {isbn} not in stock. You can add it by pressing option 2.")

def print_books(books):
    for book in books:
        for key in book.keys():
            if key != "_id":
                print(f"{key} : {book[key]}")
        print()

