import sys
import library_functions as lf
choice='y'
while choice=='y':
    print("_______________MGT Library Management System:)_________________")
    print()
    print("             ............Main Menu..............       ")
    print()
    print("                   1.Add new Book Record   ")
    print("                   2.Display Book Records  ")
    print("                   3.Issue a book          ")
    print("                   4.Return a book         ")
    print("                   5.Modify or delete Book record")
    print("                   6.Finance Status        ")
    print("                   7.Exit                  ")
    print()
    if ch==1:
        choice_add_book='y'
        print("#___Welcome to Record Viewing Section__#")
        while choice_add_book=='y':
            lf.add_book()
            print()
            choice_add_book=input("Do You want to add more Books?y/n:")
    elif ch==2:
        choice_view_book='y'
        print()
        print("#________Welcome to book viewing section______#")
        print()
        while choice_view_book=='y':
            print("     1.Display complete book record")
            print("     2.Display Authors")
            print("     3.Display Book Names")
            print("     4.Total no. of books available")
            print("     5.Display specific book record")
            view=int(input("Enter the no. of choice you choose:"))
            lf.view_book(view)
            print()
            choice_view_book=input("Do you want to view more books?y/n")
            print()
    elif ch==3:
         choice_issue_book='y'
         print("#________Welcome to book issuing section______#")
         while choice_issue_book=='y':
             print()
             book_no=int(input("Enter the book no.="))
             lf.issue_book()
             choice_issue_book=input("Do You Want to issue more books?y/n=")
    elif ch==4:
        choice_return_book='y'
        print()
        print("#________Welcome to book returning section_____#")
        while choice_return_book=='y':
            print()
            book_no=int(input("Enter the book no.="))
            lf.return_book()
            choice_return_book=input("Do You Want to return more books?y/n=")
            print()
    elif ch==5:
        choice_modify='y'
        print("#________Welcome to Record modification________#")
        print()
        print("       Select the data you want to modify:     ")
        print("       1.Book Name")
        print("       2.Author Name")
        print("       3. Cost")
        print("       4.Update return date")
        print("       5.Delete a record")
        while choice_modify=='y':
            print()
            option=int(input("Select any one of the two choices from above"))
            if option==5:
                lf.delete_record()
            else:
                lf.modify_record(option)
            choice_modify=input("Do you want to modify any other data?y/n:")
    elif choice==6:
        choice_finance_status='y'
        print()
        print("#________Welcome to Finance Section_____________#")
        print()
        print("      1.Most expensive book")
        print("      2.Least expensive book")
        while choice_finance_status=='y':
            print()
            option=int(input("Select one of the above choices:"))
            lf.finance_status(option)
            choice_finance_status=input("Do you want to porceed?y/n:")
    elif ch==7:
        print()
        print("_________THANKS FOR COMING TO MGT LIBRARY________")
        print("...........WISH YOU A GOOD DAY AHEAD...........")
        print("         KEEP READING____GOOD BYE :))          ")
        sys.exit()
    choice=input("Do you want to continue more?y/n")
        