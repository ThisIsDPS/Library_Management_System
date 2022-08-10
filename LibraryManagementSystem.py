# 'Library' class
class Library:
    listOfBooks = []
    DictOfLendedBooks = {}

    # Constructor to initialize list of Books and name of the library
    def __init__(self, listOfBooks, nameOfLibrary):
        self.listOfBooks = listOfBooks
        self.nameOfLibrary = nameOfLibrary

    # display_books method to display the books
    def display_listOfBooks(self):
        print(f"\nWELCOME TO {self.nameOfLibrary} LIBRARY\n\nWe have the following books:")
        i = 1
        for book in self.listOfBooks:
            print(f"{i}) {book}")
            i+=1
    
    # displys lended books and their present owners
    def display_dictOfLendedBooks(self):
        if len(self.DictOfLendedBooks)>0:
            for book, name in self.DictOfLendedBooks.items():
                print(f"Book:{book} is Lended to:{name}")
        else:
            print("\nNo Books lended yet.")
    
    # lendbook method to lend a book 
    def lendBook(self, name, bookToLend):
        for book in self.listOfBooks:
            if book == bookToLend: # Book to be lended in present in the list of books
                self.DictOfLendedBooks[bookToLend] = name # dictionary of lended books with book lended as key and name of the person who lended as value
                self.listOfBooks.remove(bookToLend) # removes book from the list of books
                return f"\nThe Book:{bookToLend} is now lended to {name}"
        for book, lName in self.DictOfLendedBooks.items(): # Executes if book to be lended is not present in the list of books
            if bookToLend == book:
                return f"\nBook:{bookToLend} is not available now. This book was lended to {lName}. Please come back later."
        return f"\nWe don't have the stock for the Book: {bookToLend}"
    
    # addNewBook method to add a new book to the list of books
    def addNewBook(self, newBook):
        self.listOfBooks.append(newBook) # appends the book into the list of books
        return f"\nNew book has been added successfully."

    # returnBook method to return the book
    def returnBook(self, rName, bookName):
        for book, name in self.DictOfLendedBooks.items():
            if book == bookName and name == rName: # means Book is present in the dictionary of lended books
                self.listOfBooks.append(bookName) # append the book into the list of books
                del self.DictOfLendedBooks[bookName] # remove the book from the dictionary of lended books
                return f"\nBook:{bookName} is returned successfully."
        return "\nThis is not the book you lended."
            
if __name__ == '__main__':
    obj1 = Library(["Pyjama Profits", "Rich Daddy Poor Daddy", "C++ by E Balaguruswamy", "C by Yashwant Katnekar", "CLRS"], "UIET") # Object made and constructor called
    while(True):
        print("\nEnter 1. To display all books\nEnter 2. To lend a book\nEnter 3. To add a new book\nEnter 4. To return a book\nEnter 5. To display lended books and their present owners")
        try:
            choice = int(input("Enter option Number or 0 to exit : "))
            print("")
        except ValueError as e:
            print("Please enter a number.")

        if choice==0:
            break
        elif choice==1:
            obj1.display_listOfBooks()
        elif choice==2:
            lName = input("Please enter your name : ")
            bookName = input("Which book do you want to lend? ")
            print(obj1.lendBook(lName, bookName))
        elif choice==3:
            newBookName = input("Enter new book name: ")
            print(obj1.addNewBook(newBookName))
        elif choice==4:
            rName = input("Please enter your name : ")
            lendedBookName = input("Which book you lended? ")
            print(obj1.returnBook(rName, lendedBookName))
        elif choice==5:
            obj1.display_dictOfLendedBooks()
        else:
            print("Enter Proper Option Number")