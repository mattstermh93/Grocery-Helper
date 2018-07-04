class FoodInfo():
    def __init__(self):
        self.food = ['grapes', 'olives', 'apples', 'oranges', 'donuts', 'bread', 'cheese', 'milk', 'salad', 'burgers', 'tomatos', 'potatos', 'almonds', 'eggs',
       'olive oil', 'peaches', 'plums', 'garlic', 'pepper', 'salt', 'bananas', 'chicken', 'meat', 'soy', 'macaroni', 'pasta',
       'sauce', 'toilet paper', 'tissues', 'orange juice', 'grape juice', 'wine', 'beer', 'liquor', 'tequila', 'grapefruit', 'mango']

        self.shopping_list = []

class GoingShopping(FoodInfo):
    def __init__(self):
        super().__init__()

    def displayInstructions(self):
        print('Type add to add an item to your cart')
        print('You can type delete to delete items from your shopping cart')
        print('You can type show to see what is currently in your shopping cart')
        print('You can type quit to exit the program and see what is in your shopping cart')

    def addItem(self):
        what_item = input('What would you like to add?  ')
        self.shopping_list.append(what_item)  
        print('{} has been added'.format(what_item))
        if what_item not in self.food:
            print('Sorry, I do not understand. Please try again. ')
            
    def deleteItems(self):
        deleteItem = input('what would you like to delete? ')
        if deleteItem not in self.shopping_list:
            print('That item is not in the list!')
        else:
            self.shopping_list.remove(deleteItem)
            print('{} Has been removed from your shopping list.'.format(deleteItem))
            
    def showItems(self):
        print('Here are your items\n \n ---------- \n ---------- \n  \n {} '.format(self.shopping_list))
   
    def quitProgram(self):
        quit = input("Do you want to quit? Type yes or no")
        print('Have a great day! Here are your items \n----------\n---------- \n {} '.format(self.shopping_list))
        if quit == 'yes':
            return True
        elif quit == 'no':
            return False

    def goShopping(self):
        
        self.displayInstructions()
        while True:
            what_to_do = input ("What would you like to to do? ")
            if what_to_do == 'add':
                self.addItem()
                continue
            elif what_to_do == 'quit':
                if self.quitProgram() == True:
                    break
                else:
                    continue
            elif what_to_do == 'show':
                self.showItems()
            elif what_to_do == 'delete':
                self.deleteItems()
                continue              
                

shopping_time = GoingShopping()
shopping_time.goShopping()