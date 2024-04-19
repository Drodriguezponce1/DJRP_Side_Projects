class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"[Title: {self.title}, Author: {self.author}, Pages: {self.pages}]"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")
    
book = Book("YOOOO", "Danny", 124)

print(book)
print(len(book))

del book
