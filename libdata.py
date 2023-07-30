import pickle
def add_record():
    book_name=input("Enter Book name:")
    book_no=int(input("Enter Book no.:"))
    book_Author=input("Enter Author name:")
    book_cost=int(input("Enter Book cost:(in rupees)"))
    book_genre=input("Enter book genre:")
    book_publishing_house=input("Enter name of the publishing house:")
    book_status=input("Enter issue Status:")
    book_issue_date=input("Enter issue date:")
    book_return_date=input("Enter return date:")
    record={"Book Name":book_name,"Book No.":book_no,"Book Author":book_Author,"Book Cost":book_cost,"Book Genre":book_genre,"Book Publishing House":book_publishing_house,"Issue Status":book_status,"Issue Date":book_issue_date,"Return Date":book_return_date}
    library=open("library.dat","ab+")
    pickle.dump(record,library)
    library.close()
    print("Book Added Successfully:")
def view_book(choice):
    if choice==1:
        library=open("library.dat","rb+")
        while True:
            try:
                record=pickle.load(library)
                print(record)
            except EOFError:
                break
        library.close()
    if choice==2:
        library=open("library.dat","rb+")
        while True:
            try:
                record=pickle.load(library)
                print("Book Author:",record['Book Author'])
            except EOFError:
                break
        library.close()
    if choice==3:
        library=open("library.dat","rb+")
        while True:
            try:
                record=pickle.load(library)
                print("Book Name:",record['Book Name'])
            except EOFError:
                break
        library.close()
    if choice==4:
        library=open("library.dat","rb+")
        while True:
            try:
                record=pickle.load(library)
                print("Book Publishing House:",record['Book Publishing House'])
            except EOFError:
                break
        library.close()
    if choice==5:
        library=open("library.dat","rb+")
        while True:
            try:
                record=pickle.load(library)
                print("Book Genre:",record['Book Genre'])
            except EOFError:
                break
        library.close()
    if choice==6:
        library=open("library.dat","rb+")
        while True:
            try:
                record=pickle.load(library)
                print("Issue Status:",record['Issue Status'])
            except EOFError:
                break
        library.close()
    if choice==7:
        library=open("library.dat","rb+")
        while True:
            try:
                record=pickle.load(library)
                print("Issue Date:",record['Issue Date'])
            except EOFError:
                break
        library.close()
    if choice==8:
        library=open("library.dat","rb+")
        while True:
            try:
                record=pickle.load(library)
                print("Return Date:",record['Return Date'])
            except EOFError:
                break
        library.close()
def issue_book(book_no):
    library=open("library.dat","rb+")
    recordlist=[]
    while True:
        try:
            record=pickle.load(library)
            recordlist.append(record)
        except EOFError:
            break
    library.close()
    for i in range(len(recordlist)):
        if recordlist[i]['Book No.']==book_no:
            recordlist[i]['Issue Status']="Issued"
            recordlist[i]['Issue Date']=input("Enter date of issue=")
            recordlist[i]['Return Date']=input("Enter Return Date=")
    library=open("library.dat","wb")
    for j in recordlist:
        pickle.dump(j,library)
    library.close()
def return_book(book_no):
    library=open("library.dat","rb+")
    recordlist=[]
    while True:
        try:
            record=pickle.load(library)
            recordlist.append(record)
        except EOFError:
            break
    library.close()
    for i in range(len(recordlist)):
        if recordlist[i]['Book No.']==book_no:
            recordlist[i]['Issue Status']="Not Issued"
            recordlist[i]['Issue Date']=None
            recordlist[i]['Return Date']=None
    library=open("library.dat","wb")
    for j in recordlist:
        pickle.dump(j,library)
    library.close()
def modify_book_record(choice,book_no):
    if choice==1:
        library=open("library.dat","rb")
        recordlist=[]
        while True:
            try:
                record=pickle.load(library)
                recordlist.append(record)
            except EOFError:
                break
        library.close()
        library=open("library.dat","wb")
        for i in recordlist:
            if i['Book No.']==book_no:
                continue
            pickle.dump(i,library)
        library.close()
        print("Data Successfully Deleted :(") 
    elif choice==2:
        to_modify=input("Enter the data to modify i.e book name/genre etc.")
        library=open("library.dat","rb")
        recordlist=[]
        while True:
            try:
                record=pickle.load(library)
                recordlist.append(record)
            except EOFError:
                break
        library.close()
        for i in range(len(recordlist)):
            if recordlist[i]['Book No.']==book_no:
                recordlist[i][to_modify]=input("Enter the new data=")
        library=open("library.dat","wb")
        for j in recordlist:
            pickle.dump(j,library)
        library.close()
        print("Data Successfully modified :)")
def finance_status(choice):
    if choice==1:
        library=open("library.dat","rb")
        recordlist=[]
        while True:
            try:
                record=pickle.load(library)
                recordlist.append(record)
            except EOFError:
                break
        library.close()
        total=0
        for i in range(len(recordlist)):
            total+=recordlist[i]["Book Cost"]
        print("Total Cost of all the Books=",total)
    elif choice==2:
        library=open("library.dat","rb")
        recordlist=[]
        while True:
            try:
                record=pickle.load(library)
                recordlist.append(record)
            except EOFError:
                break
        library.close()
        total=0
        num=0
        for i in range(len(recordlist)):
            total+=recordlist[i]["Book Cost"]
            num+=1
        avg=total/num
        print("Average cost of all the books is=",avg)
    elif choice==3:
        library=open("library.dat","rb")
        recordlist=[]
        while True:
            try:
                record=pickle.load(library)
                recordlist.append(record)
            except EOFError:
                break
        library.close()
        maxnum=0
        book_pos=0
        for i in range(len(recordlist)):
            if recordlist[i]["Book Cost"]>maxnum:
                maxnum=recordlist[i]["Book Cost"]
                book_pos=i
        print("Most Expensive Book is:",recordlist[book_pos]['Book Name'],"with cost:",maxnum)
    elif choice==4:
        library=open("library.dat","rb")
        recordlist=[]
        while True:
            try:
                record=pickle.load(library)
                recordlist.append(record)
            except EOFError:
                break
        library.close()
        minnum=recordlist[0]["Book Cost"]
        book_pos=0
        for i in range(len(recordlist)):
            if recordlist[i]["Book Cost"]<minnum:
                minnum=recordlist[i]["Book Cost"]
                book_pos=i
        print("Least Expensive Book is:",recordlist[book_pos]['Book Name'],"with cost:",minnum)

        
        