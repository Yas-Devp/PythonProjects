import os

STORE_NAME = "Yastore"
STORE_RATE = "4.7"
STORE_PLACE = "agadir , morocco"
STORE_PRICE_IN = "$"

admin = False

'''
products = [
             {"name": "Iphone 17" ,
              "category": "phones",
              "stock" : 125,
              "price" : 1250
             },
             {"name": "macbook air m2",
              "category" : "pc/laptops",
              "stock" : 20,
              "price" : 2050
             }
]
'''
products = []
def setup_db():
    global products
    with open('data', 'r') as file:
        content = file.read()
        pr1 = content.split('\n\n')
        
        for i in pr1:
            pr2 = i.split('\n')
            name = pr2[0].split(':')[1]
            category = pr2[1].split(':')[1]
            stock = int(pr2[2].split(':')[1])
            price = float(pr2[3].split(':')[1])
            
            new_product = {"name": name, "category": category, "stock": stock, "price": price}
    
            products.append(new_product)
    
        

def is_product_exist(name):
    for i in products:
        if i.name.lower() == name.lower():
            return True
    return False
    
    
def login_as_admin(a=3):
    os.system('clear')
    attemps = a
    global admin
    
    if admin :
        print("you are already logged in as admin")
        return
    username = input("enter username : ")
    password = input("enter password : ")
    
    if username=="yassin" and password=="loris":
        admin = True
        print("login successfully , you are admin now !")
        return
    else :
        attemps -= 1
        if attemps==0:
            print("you are not the admin •_• ")
            return
        print("Error : wrong username or password!")
        login_as_admin(attemps)
    
def add_product():
    os.system('clear')
    global admin
    
    if not admin :
        print("this action isn't permitted for normal users !")
        return
    
    
    name = input("enter product name : ")
    category = input("choose category : \n #phones\n #pc/laptops\n\n => your choice : ")
    stock = int(input("quantity to add to stock : "))
    price = float(input("specify the price ($): "))
    
    new_product = {"name": name, "category": category, "stock": stock, "price": price}
    
    products.append(new_product)
    
    data_to_add= [
        f"\nname:{name}\n",
        f"category:{category}\n",
        f"stock:{stock}\n",
        f"price:{price}\n"
    ]
    with open('data', 'a') as file:
        file.writelines(data_to_add)

def show_products():
    os.system('clear')
    print("="*25)
    for i in products :
        print(f' name : {i["name"]}')
        print(f' category : {i["category"]}')
        print(f' stock : {i["stock"]}')
        print(f' price : {i["price"]}')
        print("="*25)
        

def banner():
    print(f"Welcome to {STORE_NAME} (rate : {STORE_RATE}★")
def user_list():
   os.system('clear')
   print('|==============================|')
   print('|       - Store List -         |')
   print('|                              |')
   print('| 1- show products             |')
   print('| 2- buy product               |')
   print('| 3- show store list            |')
   print('| 4- quit                      |')
   print('|==============================|')

def admin_list():
   os.system('clear')
   print('|==============================|')
   print('|       - Store List -         |')
   print('|                              |')
   print('| 1- show products             |')
   print('| 2- buy product               |')
   print('| 3- show store list            |')
   print('| 4- quit                      |')
   print('| 5- login as admin / logout |')
   print('| 6- add new product          |')
   print('|==============================|')


os.system('clear')
setup_db()
banner()
user_list()

while True:
    choice = int(input("choose the number of service you want : "))
    
    match choice:
        case 1:
            show_products()
        case 2:
            print('this feature isn\'t added yet')
        case 3:
            admin_list() if admin else user_list()
        case 4:
            break
        case 5:
            if admin :
                admin = False
            else :
                login_as_admin()
        case 6:
            add_product()
        case _ :
            print('please specify a number of service !')
        