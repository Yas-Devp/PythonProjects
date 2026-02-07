import os

#constants
STORE_NAME = "Yastore"
STORE_RATE = 4.7
STORE_PLACE = "agadir , morocco"
STORE_PRICE_IN = "$"

#variables
admin = False
products = []
basket = []
total = 0.0

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
    
        

def get_product(name):
    for i in products:
        if i["name"].lower() == name.lower():
            return i
    return {}
    

def buy_product():
    show_products()
    global basket
    global products
    global total
    
    clear_screen()
    name = input("enter the name exact of the product : ")
    size = int(input("how much you want : "))
    
    product = get_product(name)
    
    if product != {}:
        basket.append({"name": product["name"], "quantity" : size})
        for i in range(size):
            total += product["price"]
    
    print(f"{size} {name} added to basket !")
   
def login_as_admin(a=3):
    clear_screen()
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
    clear_screen()
    global admin
    
    if not admin :
        print("this action isn't permitted for normal users !")
        return
    
    
    name = input("enter product name : ")
    category = input("choose category : \n #phones\n #pc/laptops\n\n => your choice : ")
    stock = int(input("quantity to add to stock : "))
    price = float(input(f"specify the price ({STORE_PRICE_IN}): "))
    
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
    clear_screen()
    print("="*25)
    for i in products :
        print(f' name : {i["name"]}')
        print(f' category : {i["category"]}')
        print(f' stock : {i["stock"]}')
        print(f' price : {i["price"]}{STORE_PRICE_IN}')
        print("="*25)

def show_basket():
    clear_screen()
    print("="*25)
    for i in basket :
        print(f'{i["name"]} × {i["quantity"]}')
        print("="*25)
    print("=>total :", total , STORE_PRICE_IN)
    print()

def clear_screen():
    os.system('clear')
    list_()
    
def banner():
    print(f"Welcome to {STORE_NAME} (rate : {STORE_RATE}", "★"* int(STORE_RATE) + ")")
    
def list_():
   print('|==============================|')
   print('|       - Store List -         |')
   print('|                              |')
   print('| 1- show products             |')
   print('| 2- buy product               |')
   print('| 3- show store list            |')
   print('| 4- login as admin / logout |')
   if admin :
      print('| 41- add new product          |')
   print('| 5- show basket             |')
   print('| 99- quit                      |')
   print('|==============================|')


setup_db()
banner()
list_()

while True:
    choice = int(input("choose the number of service you want : "))
    
    match choice:
        case 1:
            show_products()
        case 2:
            buy_product()
        case 3:
            list_()
        case 4:
            if admin :
                admin = False
            else :
                login_as_admin()
        case 41:
            add_product()
        case 5:
            show_basket()
        case 99:
            break
        case _ :
            print('please specify a number of service !')
        
