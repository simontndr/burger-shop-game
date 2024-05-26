#created by: Simon Tenedero
#created for: mr. DiAntonio
#class: ICS3U1
#filename: burgerShop.py
#projected started on june 8, 2022
#project completed on june 20, 2022

#This programs intended function is to simulate working at a burger shop. 
#Customers will periodically arrive and prompt the user for menu items. 
#Users must test their memory and assemble the correct burger. 
#The goal is to last as long as possible without going bankrupt

#   global variables 
#availableIngredients: list variable used to hold available ingredients   
#stock: list variable used to hold quantity of each ingredient  
#ingredientCosts: list variable used to hold ingredient prices
#menuItems: list variable used to hold menu items 
#cheeseBurgerRecipe: list variable used to hold cheese burger recipe
#bltBurgerRecipe: list variable used to hold blt burger recipe
#saladBurgerRecipe: list variable used to hold salad burger recipe
#deluxeDoubleCheeseBurgerRecipe: list variable used to hold deluxe double cheese burger recipe
#recipes: list variable used to hold menu item recipes
#menuPrices: list variable used to store menu item prices
#money: float variable used to hold user money 
#currentDay: integer variable used to hold current day  
#line1: string variable used to hold 1st line variant. Used to divide segments of UI
#line2: string variable used to hold 2nd line variant. Used to divide segments of UI
#gameOver: boolean variable used to control while loop, determines when game ends. 
#title: string variable used to hold program title
#afterHours: boolean variable used to control while loop, determines whether in After-Hours phase or Working phase 
#fee: integer variable used to hold rent fee 
#answer: integer variable used to hold user After-Hours menu selection
#ingredient: string variable used to hold ingredient 
#quantity: integer variable used to hold quantity in which stock will be updated 
#index: integer variable used to hold ingredient index within availableIngredients list
#cost: boolean variable used to hold ingredient price 
#count: integer variable used to hold current amount of customers served 
#customerChoice: integer variable used to hold value ranging from 0-4, each corresponding to a menu item.  
#customerOrder: list variable used to hold customer order recipe.  
#price: float variable used to hold menu item price 
#order: list variable used to hold user-created burger
#complete: boolean variable used to control while loop when assembling order
#timeTaken: float variable used to hold time taken to create order. 

#*------------------------------------------------------------------------------
#
#Main Program
#
#*------------------------------------------------------------------------------

from extension import*
import time 
import random

availableIngredients=["bun","patty","cheese","lettuce","tomato","bacon","onion","mushroom"]
stock=[10]*len(availableIngredients)
ingredientCosts=[0.50,1.50,0.35,0.10,0.15,0.45,0.05,0.15]
menuItems=["cheese burger","BLT burger","salad burger","deluxe double cheese burger"]
cheeseBurgerRecipe=["bun","patty","cheese","bun"]
bltBurgerRecipe=["bun","patty","cheese","bacon","lettuce","tomato","bun"]
saladBurgerRecipe=["bun","patty","lettuce","tomato","onion","mushroom","bun"]
deluxeDoubleCheeseBurgerRecipe=["bun","patty","cheese","onion","patty","cheese","onion","bun"]
recipes=[cheeseBurgerRecipe,bltBurgerRecipe,saladBurgerRecipe,deluxeDoubleCheeseBurgerRecipe]
menuPrices=[4.00,6.00,5.00,6.50]
money=100
currentDay=0
line1="="*90
line2="-"*90

gameOver=False

#program outputs title and prompts user as to whether they want game instructions.
print(line1+colors.bold)
title="WELCOME TO BURGER SHOP SIMULATOR"
print("{0:^90}".format(title))
print(colors.reset+line1)

if obtainYesNo("\nWould you like the game instructions? ")=="yes":
    displayInstructions()

#while loop is created to ensure game continues until specified otherwise
while not gameOver:
    
    #users must pay rent every 7 days. Game automatially ends if user money is negative. 
    afterHours=True
    fee=calculateRent(currentDay)
    money-=fee
    if money<0:
        time.sleep(1)
        print("uh oh... you're out of money!")
        time.sleep(1)
        print(colors.bg.red+"GAME OVER"+colors.reset)
        time.sleep(1)
        gameOver=True
    
    #while loop is created for the after-hours phase. Users can select various options:
    #view recipes, view/purchase stock, begin working phase and quit game
    while afterHours and not gameOver:
        print("\n"+line2)
        print("{0:^90}".format("After-hours"))
        print("{0:>80}{1:<10.2f}".format("current funds: $",money))
        
        print("\nMenu Options:\n\t1)View Recipes\n\t2)View/Purchase Stock\n\t3)Begin Day\n\t4)Quit Game")
        userChoice=inputIntegerBetween("\nSelection: ",1,4)
        
        #view recipes 
        if userChoice==1:
            print(line2)
            displayRecipes(menuItems,recipes,menuPrices)
        
        #view stock
        elif userChoice==2:
            print(line2)
            displayStock(availableIngredients,stock,ingredientCosts)
            answer=obtainYesNo("\nbuy more ingredients? ")
            if answer=="yes":
                ingredient=inputIngredient(availableIngredients)
                quantity=inputIntegerBetween("quantity: ",1,100)
                index=determineIndex(availableIngredients,ingredient)
                cost=ingredientCosts[index]
                
                if money-cost*quantity>0:
                    updateInventory(availableIngredients,stock,ingredient,quantity)
                    money-=cost*quantity
                    money=round(money,2)
                    print(colors.bg.green+"succesful transaction! "+colors.reset)
                else:
                    print(colors.bg.red+"insufficient funds..."+colors.reset)
        
        #begin working phase
        #random amount of customers is generated, day counter is increased by 1. 
        elif userChoice==3:
            customersToServe=random.randint(1,3)
            print(line2)
            print("You head to bed for a good nights sleep")
            time.sleep(1)
            print("The sun rises...\n")
            count=1
            currentDay+=1
            afterHours=False
            print(colors.bold+"{0:^90}".format("DAY "+str(currentDay))+colors.reset)
            print(line1)
        
        #quit game 
        else:
            print("\nYou quit your job...")
            time.sleep(1)
            gameOver=True
            break
    
    #while loop is created for the working phase.    
    while not afterHours and not gameOver:
        
        #the amount of customers left to serve is presented on the top right
        #random menu item is generated and designated as customer order
        print("{0:>90}".format("remaining customers: "+str(customersToServe-count)))
        customerChoice=random.randint(0,len(menuItems)-1)
        customerOrder=recipes[customerChoice]
        price=menuPrices[customerChoice]
        
        time.sleep(2)
        print("\nA customer has arrived...")
        print('"Hello, I\'d like to order a '+colors.fg.yellow+menuItems[customerChoice]+colors.reset+'!"')
        
        #user is prompted to assemble the requested order. Time taken is recorded. 
        time.sleep(1)
        print("\n\tLet's make the order!")
        time.sleep(1)
        start=time.time()
        
        order=[]
        complete=False
        while not complete:
            #current list is displayed 
            print("current burger: ")
            for x in range(len(order)-1,-1,-1):
                print(order[x])
            
            #program prompts user to select a menu option
            print("\nMenu Options:\n\t1)Add to burger\n\t2)Delete previous ingredient\n\t3)Submit order")
            answer=inputIntegerBetween("\nSelection: ",1,3)
            
            #option 1 adds an ingredient to list, 
            #function verifies whether ingredient is available using ingredientAvailable(), 
            #then decreases stock for the respective ingredient by 1 with updateInventory()
            if answer==1:
                ingredient=inputIngredient(availableIngredients)
                if ingredientAvailable(availableIngredients,stock,ingredient):
                    updateInventory(availableIngredients,stock,ingredient,-1)
                    order+=[ingredient]
                else:
                    print(colors.bg.red+"Sorry, you're out of stock!"+colors.reset)
            
            #option 2 deletes previous ingredient from list using deleteEnd(), 
            #then increases stock for the respective ingredient by 1 with updateInventory()
            elif answer==2:
                if len(order)>0:
                    updateInventory(availableIngredients,stock,order[-1],+1)
                    order=deleteEnd(order)
                else:
                    print("nothing to delete...")
            #option 3 terminates while loop
            else:
                complete=True
            print("")
        
        finish=time.time()
        
        timeTaken= finish-start
        
        timeTaken=round(timeTaken,1)
        
        #program verifies whether user assembled the correct order. If correct, user money is increased. 
        #Additional tip is calculated based on the time taken. 
        if orderCorrect(order,customerOrder):
            print(colors.bg.green+'"Thanks so much! This is delicous!"'+colors.reset)
            print(colors.fg.green+"+${0:.2f}".format(price)+colors.reset)
            print("determining score...")
            time.sleep(2)
            print("that took you "+str(timeTaken)+" seconds.")
            serviceRating(timeTaken)
            bonus=calculateTip(menuPrices,customerChoice,timeTaken)
            print(colors.fg.green+"+${:.2f}".format(bonus)+colors.reset)
            money+=price+bonus
        else:
            print(colors.bg.red+'"UGHHH... you got my order wrong!"'+colors.reset)
        
        count+=1 
        
        #Once count is greater than customersToServe, working phase terminates. 
        if count>customersToServe:
            afterHours=True
            time.sleep(1)
            print("\nno customers left...")
            time.sleep(1)
            print("The day has finished!")
            time.sleep(1)
            
else:
    #program outputs a message once game finishes, accompanied by the amount of days survived.
    print(line1)
    print("Thanks for playing!")
    print("You lasted "+str(currentDay)+" days.")















