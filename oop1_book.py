class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return f"{self.title} by {self.author}({self.pages}pages)"
book=Book("The Great Gatsby","F.Scott Fitzgerald",208)
print(book)