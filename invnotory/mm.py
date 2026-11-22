import json
Record={}
def login():
    pin=2344
    count=0
    while True:
        try:
          p=int(input("enter password:"))
        except ValueError:
            print("password only intgr")
            continue
        if p==pin:
            return True
        else:
            if p!=pin:
                count+=1
        if count==3:
            return False


def menu():
    print("\t Inventory Management System")
    print("1.Add Item")
    print("2.View All Items")
    print("3.Search Item")
    print("4.Update Stock")
    print("5.Sell Item")
    print("6.Low Stock Alert")
    print("7.Delete Item")
    print("8.Total Stock Value")
    print("9.exit")

def add():
    global Record
    while True:
        try:
          i=int(input('entr Id:'))
        except ValueError:
            print("please enter integr Id only")
            continue
        if i<0:
            print("enter positive value or 0 to stop")
            continue
        if i==0:
            break
        found=False
        for nam,val in Record.items():
            if nam==i:
                print("same id not allow")
                found=True
        if found==True:
            continue
        duplict=False
        n=input("enter name:")
        for k,v in Record.items():
            if v['Name']==n:
                print("same name not allow")
                duplict=True
        if duplict==True:
            continue
        try:
         p=int(input("enter price per kg:"))
        except ValueError:
            print("please enter integr price only")
            continue
        if p<=0:
            print("enter valid price")
            continue
        try:
          q=int(input("enter quantity:"))
        except ValueError:
            print("please enter integar only")
            continue
        if q<0:
            print("please enter valid quantity")
            continue
        Record[i]={"Name":n , "price":p ,"quantity":q}
        save()


def view():
    global Record
    for id,val in Record.items():
        print(f"ID#{id}:")
        for k,v in val.items():
            print(f"\t {k}:{v}",end=" ")
        print()
def search():
    global Record
    while True:
         s=input("enter product name:")
         if s=="done":
            break
         for i,v in Record.items():
            if v["Name"]==s:
                print(f"ID:{i} price:{v["price"]} quantity:{v["quantity"]}")
                break
         else:
            print(f"Item:{s} not found")

def update():
    global Record
    while True:
        try:
            ii=int(input("enter ID:"))
        except ValueError:
            print("invlid input please integar value")
            continue
        if ii==0:
            break
        for id,vl in Record.items():
            if id==ii:
                c=input("what you want to change:")
                if c=='price':
                    try:
                     pp=int(input("entr new price:"))
                    except  ValueError:
                        print("please enter integar")
                        break
                    if pp<=0:
                        print("invlid price")
                        break
                    vl["price"]=pp
                    save()
                    break
                elif c=="quantity":
                    try:
                      qq=int(input("enter new quantity:"))
                    except ValueError:
                        print("please enter integar")
                        break
                    if qq<0:
                        print("invlid quntity")
                        break
                    vl["quantity"]=qq
                    save()
                    break
                else:
                    print("invlid name")
                    break
        else:
            print("id not found try again")

def sell():
    global Record
    while True:
        try:
         o=int(input("enter id or 0 to stop:"))
        except ValueError:
            print("invalid id please enter integar")
            continue
        if o==0:
            break
        for k,v in Record.items():
            if k==o:
                try:
                 p=int(input("enter quantity in kg:"))
                 if p<=0:
                     print("invalid quantity")
                     break
                except ValueError:
                    print("only integar allow")
                    break
                if p>v["quantity"]:
                    print("out of stock")
                    break
                else:
                    v["quantity"]-=p
                    print(f"price:{p*v["price"]}")
                    save()
                    break
        else:
            print("id not found")
def low_stock():
    global Record
    found=False
    for k,v in Record.items():
        if v["quantity"]<5:
            print(f"ID:{k} Name:{v["Name"]} quantity:{v["quantity"]}")
            found=True
    if found==False:
            print("all stock are available")

def dlt():
    global Record
    while True:
        try:
          a=int(input("enter ID to delete (0 to exit):"))
        except ValueError:
            print("invallid input please integar")
            continue
        if a==0:
            break
        if a in Record:
            del Record[a]
            save()
            print("deleted")
        else:
            print("id not found")

                
def totl():
    global Record
    total=0
    for k,v in Record.items():
            total+=v["quantity"]*v["price"]
    print(f'total record price:{total}')

def save():
    f=open("Record.json","w")
    json.dump(Record,f)
    f.close()

def load():
    try:
        f=open("Record.json","r")
        d=json.load(f)
        for k ,v in d.items():
            Record[int(k)]=v
        f.close()
    except FileNotFoundError:
        pass


r=login()
if r==True:
    load()
else:
    print("incorret pin your ")
    exit()
while True:
    menu()
    try:
     choice=int(input("enter your choice"))
    except ValueError:
        print("enter only integr")
        continue
    if choice==1:
        add()
    elif choice==2:
        view()
    elif choice==3:
        search()
    elif choice==4:
        update()
    elif choice==5:
        sell()
    elif choice==6:
        low_stock()
    elif choice==7:
        dlt()
    elif choice==8:
        totl()
    elif choice==9:
        print("thnk you for using")
        break
    else:
        print("invlid choice")


