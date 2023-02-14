import os
os.system('cls')

class Shopper:
    def __init__(self,name,amount) :
        self.name= name
        self.amount= amount
        self.cart=[]

    def add_cart(self,item,price,quantity): 
        self.cart.append({'item' : item,'price' : price ,'quantity' : quantity}) 
    def view_cart(self):
            total_cost= 0
            for j in range (0,len(self.cart)):

                print("\n\tItem name : ",end="")
                print(self.cart[j]['item'])
                print("\tPrice(per pcs) : ",end="")
                print(self.cart[j]['price'])
                print("\tQuantity : ",end="")
                print(self.cart[j]['quantity'])
                print("\t Totall : ",end="")
                print( int(self.cart[j]['quantity']) * int( self.cart[j]['price'] ) )
                total_cost = total_cost +( int(self.cart[j]['quantity'] )* int( self.cart[j]['price']) )

                print("\n==========================\n")

            print(f"Total cost : {total_cost}")
            print("\n==========================\n")
            print(f"\nMr.{self.name}\nyour current balance is {self.amount-total_cost} tk")    
    

    def checkout(self):
        os.system('cls')
        price = 0
  
        for i in range (0,len(self.cart)):
            
            print("\n",self.cart[i]['item'],"'s price (per pis): ",self.cart[i]['price'])
            print(f"Quantity of {self.cart[i]['item']} : {self.cart[i]['quantity'] } ")
            price = price +( int(self.cart[i]['quantity']) *  int(self.cart[i]['price']))
            print(f"Price of {self.cart[i]['item']} :{int(self.cart[i]['quantity']) *  int(self.cart[i]['price'])} ")

        if self.amount<price:
            print("You dont have enough money! ")
            print(f'Please give me more {price - self.amount} taka') 
            

            # print("Do you want to add money ? \n1.yes\n2.no)")
            # yes_no=input( "Do you want to add money & buy those product ? \n1.yes\n2.no)" )
            # if yes_no=="1":
              #  # add_more_money=int(input("Add money : "))  
                # add_more_money=price - self.amount
                # self.amount=self.amount+add_more_money
# 
            # else:
                # print("You do not money. So you cant buy those product \n")           
        else:
            print( f'\nCost : {price}')
            self.amount=self.amount-price
    
    def view_profile(self):
        print(f"Name            : {self.name}")
        print(f"Current balance : {self.amount}")
        


def menu():
    print("1.Buy Product : \n2.View cart\n3.Profile\n4.Exit ")

print("****Open your account ****")
Shopper_name=input("Enter your name : ")
Shopper_amount=int(input("Enter your amount : "))
Shopping=Shopper(Shopper_name,Shopper_amount)

while 1:
    os.system('cls')
    menu()
    option=input("Enter your option : ")

    if option=="1":
        os.system('cls')

        # Buy product
        print("\nItem List            price   \n")
        print("1.Pant --------------1,299 tk ")
        print("2.Shirt -------------  999 tk")
        print("3.T-shirt -------------499 tk  ")
        print("4.Panjabi -----------1,599 tk ")

        shopping_item=input("Enter your no : ")
        item_quantity=input("& quantity no : ")

        if shopping_item =="1":
            Shopping.add_cart( "Pant" ,1299 , item_quantity ) 
        elif shopping_item=="2":
            Shopping.add_cart( "Shirt" ,999 , item_quantity )
        elif shopping_item=="3":
            Shopping.add_cart( "T-shirt" ,499 , item_quantity )
        elif shopping_item=="4":
            Shopping.add_cart("Panjabi" ,1599 , item_quantity ) 
        else:
            press_continue1=input("\n\tEnter any key to continue \n")
            # Shopping.checkout()
            continue 
        Shopping.checkout()
        press_continue1=input("\n\tEnter any key to continue \n")
   

        

    elif option =="2":
        os.system('cls')

        #view cart
        print("\n\tView cart\n")
        Shopping.view_cart()
        press_continue1=input("\n\tEnter any key to continue \n")


    elif option =="3":
        os.system('cls')

        #profile
        print("Profile")
        Shopping.view_profile()
        press_continue1=input("\n\tEnter any key to continue \n")


    elif option =="4":
        # Exit
        break



