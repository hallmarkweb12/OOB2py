class Library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lend = {}

    def display(self)    :
        print(f"We have the following books in our library:{self.name}")
        for book in self.booklist:
            print(book)


    def lendbook(self,user,book):
        if book not in self.lend.keys():
            self.lend.update({book:user})
            print("Lender-book database has been updated.You can take the book now.")
        else:
            print(f"Book is alredy being used by {self.lend[book]}")    


    def addbook(self,book):
        self.booklist.append(book)       
        print("Bok has been added to the book list")

    def returnbook(self,book):
        self.lend.pop(book)

    if __name__ == '_main_':
        books = Library(['Python','HTML','CSS','Java','ML','Data Science'])

    while True:
        print(f"Welcome to the {books.name} library.Enter an option")
        print("1.Display Books")
        print("2. Lend Book")
        print("3.Add a book")
        print("4.Return a book")
        userchoice = input()
        if userchoice not in ['1','2','3','4'] :
            print("Please enter a valid option")
            continue
        else:
            userchoice = int(userchoice)
        if userchoice == 1 :
            books.displaybooks()    
        elif userchoice == 2:
            book = input("Enter the name of the book you want to lend")    
            user = input("Enter your name")
            books.lendbook(user,book)

        elif userchoice == 3:
            input("Enter the name of the book you want to return")
            books.returnbook(book)
        else:
            print("This is not a valid option")

        print("Press c to continue and q to quit")         
        userchoice2 =""
        if userchoice2 == "Q" or "q":
            quit()
        elif userchoice2 == "C" or "c":
            continue