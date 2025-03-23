import csv
import urllib.request, json
import pyfiglet
import time, sys

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.002)

# search for ISBN on google books
def isbn_websearch(isbn):
    try:
        with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn) as url:
            bookdata = json.load(url)
            # link right info to right variables
            title = bookdata['items'][0]['volumeInfo']['title']
            pages = bookdata['items'][0]['volumeInfo']['pageCount']
            languages = bookdata['items'][0]['volumeInfo']['language']
            authorname = bookdata['items'][0]['volumeInfo']['authors'][0]
    except:
        authorname = ""
        pass
    # for user to check output
    if authorname:
        print("Author: ", authorname)
        print("Title: ", title)
        print("Number of pages: ", pages)
        print("Languages: ", languages)
        print("ISBN: ", isbn)
        # if output makes sense, add to database?
        confirm_to_db = input("Do you want to add this book to the database yes/no? ")
        if confirm_to_db.lower() in ("yes","y"):
            # add book to csv with ISBN
            with open("libdat.csv", "a", newline="") as file:
                writer = csv.writer(file)
                # New CSV row: title, author, isbn, pages, languages
                writer.writerow([title, authorname, isbn, pages, languages])
                print("\nadded")
        else:
            print("\nnot added")
    else:
        print("Info not found")

# function to delete a book from the catalogue
def delete_book():
    text = "Delete Book from Catalogue"
    ascii_art = pyfiglet.figlet_format(text, width=150)
    print(ascii_art)
    search_value = input("Enter part of the title or author of the book to delete: ").strip().lower()
    
    all_books = []
    matching_books = []
    
    # Read all rows, saving each row with its index
    with open("libdat.csv", "r") as file:
        reader = csv.reader(file)
        for idx, row in enumerate(reader):
            all_books.append(row)
            if search_value in row[0].lower() or search_value in row[1].lower():
                matching_books.append((idx, row))
    
    if not matching_books:
        print("No matching books found.")
        return
    
    # Display matching books with a sequential number for user selection
    print("Matching books:")
    for i, (original_index, book) in enumerate(matching_books):
        print(f"{i+1}: Title: {book[0]}, Author: {book[1]}")
    
    try:
        choice = int(input("Enter the number of the book you want to delete (or 0 to cancel): "))
    except ValueError:
        print("Invalid input. Cancelling deletion.")
        return
    
    if choice == 0:
        print("Deletion cancelled.")
        return
    if choice < 1 or choice > len(matching_books):
        print("Invalid selection.")
        return
    
    original_index, book_to_delete = matching_books[choice - 1]
    confirm = input(f"Are you sure you want to delete '{book_to_delete[0]}' by {book_to_delete[1]}? (yes/no): ").strip().lower()
    if confirm not in ("yes", "y"):
        print("Deletion cancelled.")
        return
    
    # Remove only the selected occurrence using its index
    del all_books[original_index]
    
    # Write the updated list back to the CSV file
    with open("libdat.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(all_books)
    print("Book deleted successfully.")

# function to perform a catalogue search with the ability to search repeatedly or return to main menu
def search_catalogue():
    while True:
        text = "Search Catalogue"
        ascii_art = pyfiglet.figlet_format(text, width=150)
        print(ascii_art)
        search_value = input('Please enter your search query (or type "menu" to return):\n\n').strip().lower()
        
        # if the user chooses to return to main menu
        if search_value == "menu":
            break
        
        if not search_value:
            print("Please enter a valid search query")
        else:
            found = False
            with open("libdat.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if search_value in row[0].lower() or search_value in row[1].lower():
                        found = True
                        if len(row) >= 5:
                            print(f"Title: {row[0]}\nAuthor: {row[1]}\nISBN: {row[2]}\nLanguage: {row[4]}\n" + "-"*30)
                        else:
                            print(f"Title: {row[0]}\nAuthor: {row[1]}\n" + "-"*30)
            if not found:
                print("No matching books found.")
        
        # Ask the user if they want to search again or return to main menu
        option = input("Press Enter to search again, or type 'menu' to return to the main menu: ").strip().lower()
        if option == "menu":
            break

# main menu function
def menu():
    while True:
        print("1: add book, 2: search, 3: view database, 4: delete book, 5: exit")
        choice = input('Please choose an option: ')
        if choice:
            choice = int(choice)
            while choice in range(1, 6):
                match choice:
                    case 1:
                        text = "Add Book to Collection"
                        ascii_art = pyfiglet.figlet_format(text, width=150)
                        print(ascii_art)
                        isbn_input = input("To add a book, please enter ISBN: ")
                        isbn_websearch(isbn_input)
                        menu()
                    case 2:
                        search_catalogue()  # call the search loop function
                        menu()
                    case 3:
                        text = "View Catalogue"
                        ascii_art = pyfiglet.figlet_format(text, width=150)
                        print(ascii_art)
                        with open("libdat.csv", "r") as file:
                            reader = csv.reader(file)
                            for row in reader:
                                if len(row) >= 5:
                                    print(f"Title: {row[0]}\nAuthor: {row[1]}\nISBN: {row[2]}\nLanguage: {row[4]}\n" + "-"*30)
                                else:
                                    print(f"Title: {row[0]}\nAuthor: {row[1]}\n" + "-"*30)
                        input("Press Enter to return to the menu...")
                        menu()
                    case 4:
                        delete_book()
                        input("Press Enter to return to the menu...")
                        menu()
                    case 5:
                        print("Thanks")
                        exit()
        else:
            print("Please enter a valid choice")

text = "Simple Library Catalogue"
ascii_art = pyfiglet.figlet_format(text)
typingPrint(ascii_art)
menu()