class LibraryCatalog:
    def __init__(self, books):
        self.__books = books

    def search_book(self, target_book):
        found=False
        for i in range(0,len(self.__books)):
            if self.__books[i]==target_book:
                found=True
        if found:
            return #book details
        else:
            return "book not found"

    


library = LibraryCatalog(["Harry Potter", "Lord of the Rings", "To Kill a Mockingbird"])
result = library.search_book("Lord of the Rings")
print(result)
