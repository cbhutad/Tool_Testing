def add_book(bookcollection, newbook):
    
    if bookcollection.find_one({"isbn": newbook.isbn }):
        print("Book already exists")
    
    bookcollection.insert_one(newbook.mapper_no_id())

    print("Book added successfully")
