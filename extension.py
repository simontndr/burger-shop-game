#   Function isInteger(string)
#Function takes string and verifies whether it is an interger. If it's an interger, return True.
#If not, return False
#       Parameters:
#string: string variable used to hold user-input 
#       Local Variables:
#n/a
#       Return Variable Types:
#boolean   

#   Function inputInterger(message,intErrorMessage)
#Function prompts user for input and verifies whether it is an interger. Loop will not terminate until
#integer is entered. 
#       Parameters:
#message: string variable used to hold input prompt
#intErroMessage: string variable used to hold message outputted when input is not an integer
#       Local Variables:
#result: String variable used to store user inputted response
#invalidInput: Boolean variable used to control while loop, ensuring user replies with an integer value
#       Return Variable Types:
#integer

#   Function inputIntegerBetween(message,intErrorMessage,boundErrorMessage,lowBound,highBound)
#Function prompts user for interger using inputInterger function. Function verifies whether result is between lowBound and 
#highBound; loop will not terminate until acceptable value is entered. 
#       Parameters:
#message: String variable used to hold input prompt
#intErroMessage: string variable used to hold message outputted when input is not an integer
#lowBound: Integer variable used to hold lower restriction.
#highBound: Integer variable used to hold upper restriction
#       Local Variables
#result: Integer variable used to store user inputted response
#invalidInput: Boolean variable used to control while loop, ensuring user replies with an integer between lowBound and 
#       Return Variable Types:
#integer 

#   Function searchList(userList,target)
#Function takes List varaible and verifies whether target is included within
#       Parameters:
#userList: list variable
#target: string variable used to hold search target
#       Local Variables:
#item: string variable used to contol for loop
#result: boolean variable used to hold result
#       Return Variable Types:
#boolean 

#   Function obtainYesNo(message)
#Function prompts user for input with message, 
#a while loop is created to ensure either yes or no is entered 
#       Parameters:
#message: string variable used to hold question prompt
#       Local Variables:
#invalidInput: boolean variable used to control while loop, 
#result: string variable used to hold user input
#       Return Variable Types:
#string 

#   displayInstructions()
#Function outputs game instructions
#       Parameters:
#n/a
#       Local Variables:
#n/a
#       Return Variable Types:
#n/a

# inputIngredient(availableIngredients)
#Function prompts user for an ingredient. 
#Function verifies whether input is a valid ingredient using searchList function
#While loop will not terminate until user enters a valid ingredient. 
#       Parameters:
#availableIngredients: list variable used to hold valid ingredients 
#       Local Variables:
#invalidInput: boolean variable used to control while loop, 
#result: string variable used to hold user input
#       Return Variable Types:
#string 

# determineIndex(myList,target):
#Function takes target and determines its index within myList using a for loop.  
#       Parameters:
#myList: list variable used to hold series of items 
#target: string variable used to hold target
#       Local Variables:
#result: integer variable used to hold target index
#       Return Variable Types:
#integer


# calculateRent(currentDay):
#Using currentDay, function determines users rent fee. 
#Fee progressively increases in proportion to the amount of "weeks" played
#       Parameters:
#currentDay: integer variable used to hold current day
#       Local Variables:
#result: integer variable used to hold user rent fee 
#       Return Variable Types:
#integer

# displayRecipes(menuItems,recipes,menuPrices):
#Function displays available menu items, their respective recipes as well as their price.
#       Parameters:
#menuItems: list variable used to hold menu items 
#recipes: list variable used to hold menu item recipes 
#menuPrices: list variable used to store menu item prices
#       Local Variables:
#n/a
#       Return Variable Types:
#n/a

# displayStock(availableIngredients,stock,ingredientCosts):
#Function displays available ingredients, the quantity in posession and their respective prices. 
#       Parameters:
#availableIngredients: list variable used to hold available ingredients 
#stock: list variable used to hold quantity of each ingredient 
#ingredientCosts: list variable used to hold ingredient prices
#       Local Variables:
#n/a 
#       Return Variable Types:
#n/a

# ingredientAvailable(availableIngredients,stock,ingredient):
#Function takes ingredient and determines index within availableIngredients using determineIndex Function
#Function finds index equivalent within stock and verifies whether value is greater than 0. 
#       Parameters:
#availableIngredients: list variable used to hold available ingredients
#stock: list variable used to hold ingredient stock 
#       Local Variables:
#n/a
#       Return Variable Types:
#boolean

# deleteEnd(myList):
#function creates a newList equivalent to myList, with the last entry omitted. 
#       Parameters:
#myList: list variable used to hold a series of items
#       Local Variables:
#n/a
#       Return Variable Types:
#list 

# orderCorrect(order,customerOrder):
#function takes order and verifies whether sequence of items within are parallel to customer order using a for loop
#       Parameters:
#creation: list variable used to hold user list 
#customer order: list variable used to hold customer order
#       Local Variables:
#result: boolean variable used to hold result 
#       Return Variable Types:
#boolean
 
# updateInventory(availableIngredients,stock,ingredient,quantity):
#Function determines index of ingredient within availableIngredients list using determineIndex function. 
#Next, function finds index equivalent within stock, and reduces quantity by the designated amount.
#       Parameters:
#availableIngredients: list variable used to hold available ingredients
#stock: list variable used to hold ingredient stock
#ingredient: string variable used to hold target ingredient 
#quantity: integer variable used to hold quantity in which stock will be updated 
#       Local Variables:
#n/a
#       Return Variable Types:
#list

# calculateTip(menuPrices,customerChoice,timeTaken):
#Function determines tip in relation to time taken. Tips are a percentage of customer order.
#       Parameters:
#menuPrices: list variable used to hold menu item prices 
#customerChoice: integer variable used to hold value ranging from , each corresponding to a menu item. 
#timeTaken: float variable used to hold time taken to create order. 
#       Local Variables:
#result: float variable used to hold calculated tip.
#       Return Variable Types:
#float

# serviceRating(timeTaken):
#Function determines service rating in relation to time taken.
#       Parameters:
#timeTaken: float variable used to hold time taken to create order. 
#       Local Variables:
#n/a
#       Return Variable Types:
#n/a

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

def isInteger(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
            
def inputInteger(message):
    invalidInput=True
    while invalidInput:
        result=input(message)
        if isInteger(result):
            result=int(result)
            invalidInput=False
        else:
            print(colors.bg.red+"please enter an integer value."+colors.reset)
    return result

def inputIntegerBetween(message,lowBound,highBound):
    invalidInput=True
    while invalidInput:
        result=inputInteger(message)
        if result>=lowBound and result <=highBound: 
            invalidInput=False
        else:
            if result<lowBound:
                print(colors.bg.red+"please enter a number greater than or equal to "+str(lowBound)+"."+colors.reset)
            else:
                print(colors.bg.red+"please enter a number less than or equal to  "+str(highBound)+"."+colors.reset)
    return result

def searchList(userList,target):
    result=False
    for item in userList:
        if item==target:
            result=True
            break
    return result
  
def obtainYesNo(message):
    invalidInput=True
    while invalidInput:
        result=input(message)
        result=result.strip().lower()
        if result=="yes" or result=="no":
            invalidInput=False
        else:
            print(colors.bg.red+"please type in yes or no."+colors.reset)
    return result

def displayInstructions():
    print("\n{0:^90}".format("INSTRUCTIONS"))
    print("""
    Burger shop simulator is composed of two phases— after-hours and working. 
    
    During the after-hours phase, users will be presented with a menu:
    1) View Recipes
        -Users can view the different menu items customers will request and the 
         corresponding ingredient order for assembly. Enter ingredients left to right.
    2) View/Purchase stock 
        -Users can view ingredient stock and will be prompted as to whether they want to 
         purchase more ingredients. 
        -If users run out of stock for an ingredient, they will not be able to include it 
         when assembling customer orders.
        -Make sure not to overspend though, as having low funds can be dangerous…  
    3) Begin Day
        -Program will commence the working phase, during which users cannot access the 
         After-Hours menu options. 
    4) Quit Game 
        -Program will terminate. 

    During the working phase, users will serve 1-3 customers. 
    A customer will arrive and request a random menu item.
    Users will then be prompted to assemble the order; various options are present: 
    1) Add to burger
        -Users will enter an ingredient to add to the order.
    2) Delete previous ingredient 
        -Users can remove the last ingredient added to the order. 
    3) Submit order
        -Users declare that the order is complete.
    Program will then check whether the user assembled the correct order. 
    Users will earn money if successful. A tip will be granted proportional to the time 
    taken in assembling the order. This cycle will repeat until all customers are served. 
    The working phase will then terminate. 

    Every 7 days users must pay rent. The fee will increase by $25 dollars each time. 
    If users cannot afford to pay their rent, the game will end. 
    The objective of the game is to last as long as possible without going bankrupt. 
    """)

def inputIngredient(availableIngredients):
    invalidInput=True
    while invalidInput:
        result=input("enter an ingredient: ")
        result=result.strip().lower()
        if searchList(availableIngredients,result):
            invalidInput=False
        else:
            print(colors.bg.red+"please enter an a valid ingredient."+colors.reset)
            print("options: ")
            for item in availableIngredients:
                print("\t"+item)
    return result

def determineIndex(myList,target):
    for x in range(len(myList)):
        if myList[x]==target:
            result=x
            break
    return result

def calculateRent(currentDay):
    result=0
    if currentDay>0 and currentDay%7==0:
        print("A week has passed... you must pay your rent!")
        result=currentDay/7*25
        print(colors.fg.red+"-$"+str(result)+colors.reset)
    return result 
        
def displayRecipes(menuItems,recipes,menuPrices):
    print("{0:^90}".format("RECIPES"))
    for x in range(len(menuItems)):
        print("\n"+str(x+1)+") "+menuItems[x])
        print(recipes[x])
        print("Item is currently being sold for {:.2f}".format(menuPrices[x]))

def displayStock(availableIngredients,stock,ingredientCosts):
    print("{0:^90}".format("INVENTORY\n"))
    print("{0:^30}{1:^30}{2:^30}".format("Ingredient","Stock","Cost/pc.($)"))
    for x in range(len(availableIngredients)):
        print("{0:^30}{1:^30}{2:^30.2f}".format(availableIngredients[x],stock[x],ingredientCosts[x]))

def ingredientAvailable(availableIngredients,stock,ingredient):
    if stock[determineIndex(availableIngredients,ingredient)]>0:
        return True
    else:
        return False

def deleteEnd(myList):
    newList=[]
    if len(myList)>1:
        newList=[""]*(len(myList)-1)
        for x in range(len(myList)-1):
            newList[x]=myList[x]
    return newList

def orderCorrect(creation,customerOrder):
    result=False
    if len(creation)==len(customerOrder):
        result=True
        for x in range(len(creation)):
            if creation[x]!=customerOrder[x]:
                result=False 
                break
    return result

def updateInventory(availableIngredients,stock,ingredient,quantity):
    index=determineIndex(availableIngredients,ingredient)
    stock[index]+=quantity
    return stock

def calculateTip(menuPrices,customerChoice,timeTaken):
    if timeTaken<15:
        result=0.4*(menuPrices[customerChoice])
    elif timeTaken<30:
        result=0.3*(menuPrices[customerChoice])
    elif timeTaken<45:
        result=0.2*(menuPrices[customerChoice])
    elif timeTaken<60:
        result=0.1*(menuPrices[customerChoice])
    else:
        result=0 
    result=round(result,2)
    return result

def serviceRating(timeTaken):
        if timeTaken<15:
            print("super fast! ★★★★★")
        elif timeTaken<30:
            print("pretty fast! ★★★★")
        elif timeTaken<45:
            print("decent. ★★★")
        elif timeTaken<60:
            print("A little slow... ★★")
        else:
            print("what took so long? ★")







        
        
        