import os
os.chdir('Atm')
balance=50000
pin=1234
l=[]
def login():
    incorrect=0
    while True:
        try:
         o=int(input("enter pin:"))
        except ValueError:
           print("please enter inetegars")
           continue
        if o==pin:
            return True
            
        else:
            incorrect+=1
        if incorrect==3:
           return False
          
def menu():
    print("\t ATM MACHINE")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Transaction History")
    print("5. Exit")
    
def deposit():
    global l
    while True:
        try:
         d=int(input("enter deposit amount:"))
        except ValueError:
           print("please enter integar")
           continue
        if d<=0:
         print("invlid amount try again:") 
        else:
            global balance
            balance+=d
            l.append(f"depost={d}")
            f=open("transcation.txt","a")
            f.write(f"\ndeposit amount={d}")
            f.close()
            f=open("balance.txt",'w')
            f.write(str(balance))
            f.close()
            print("deposit successfully")
            break

def withdraw():
    global l
    global balance
    while True:
        try:
         w=int(input("enter withdraw amount:"))
        except ValueError:
           print("please enter integar")
           continue
        if w<=0:
            print("invlid amount try again:")
        elif w>balance:
            print("invalid amount try again")
        else:
            balance-=w
            l.append(f"widthra:{w}")
            f=open("transcation.txt","a")
            f.write(f"\nwithdraw amount={w}")
            f.close()
            f=open("balance.txt",'w')
            f.write(str(balance))
            f.close()
            print("withdraw successfully")
            break

def chk_history():
    if os.path.exists("transcation.txt"):
      f=open("transcation.txt","r")
      r=f.read()
      print(r)
      f.close()
    else:
        print("file not exist")

    print(f"temporary transcation history:{l}")


def chk_balance():
    global balance
    print(f"your balance:{balance}")

def load():
   global balance
   if not os.path.exists("balance.txt"):
      f=open("balance.txt",'w')
      f.write(str(balance))
      f.close()
   else:
      f=open("balance.txt",'r')
      y=f.read()
      balance=int(y)
      f.close()
g=login()
if g==True:
   load()   
else:
   exit()
while True:
    menu()
    try:
       us=int(input("enter choice:"))
    except ValueError:
       print("please enter integar")
       continue
    if us>5 or us<=0:
     print("invalid choice try again")
    else:
     if us==1:
        chk_balance()
     elif us==2:
       withdraw()
     elif us==3:
      deposit()
     elif us==4:
      chk_history()
     elif us==5:
      print("thank you for using atm")
      break