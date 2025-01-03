class SmartCart(dict):
    '''dict subclass to maintain user cart'''
    discount_coupon = {'SAVE10': 10, 'SAVE20': 20, 'SAVE30': 30}
    def subtotal(self):
        '''Returns subtotal from a dictionary object'''
        total = 0
        #iterate over each key, value in dict
        #obtain the price and quantity for each key
        #add to total variable after multiplying price with the quantity
        for item, quantity in self.items():   #iterate through items
            total += item.get_price() * quantity #price times quantity
        return total
    def tax(self):
         #your code here
        total = self.subtotal() * 0.043 # subtotal times 4.3%
        return total
    
    def total(self): # before discount
        #your code here
        total =  self.subtotal() + self.tax() # real total is subtotal plus tax
        return total

    def discount(self, coupon_code): #calculate discount
        # your code here
        if coupon_code in self.discount_coupon: # checks if any of the coupon codes are in discount_coupon
            discount_percentage = self.discount_coupon[coupon_code] # checks the value
            discount_amount = self.total() * (discount_percentage / 100) # clac discount amount
            return discount_amount
        else:
            return 0  # returns 0 when code invalid - return None , return ""

    def discounted_total(self,coupon_code): #after discount if applied
        # your code here
        total = self.total()  # total before discount
        disc_amount = self.discount(coupon_code)  #discount based on coupon code
        disc_total = total - disc_amount #subtract discount ammount from total
        return disc_total
class Item(object):
    '''Item class defines an item
    available in store. Item object saved in
    lists per category'''
    
    def __init__(self, category, name, price, expiration_date):
        '''Initialization method'''
        #your code here
        #assuming all the variables are private.
        self.__category = category
        self.__name = name
        self.__price = price
        self.__expiration_date = expiration_date

    #define all the get methods to obtain the instance variables.
    #define a __str__ method to obtain all four instance attributes.
    def get_category(self): # get category
        return self.__category

    def get_name(self):  # get name
        return self.__name

    def get_price(self): # get price
        return self.__price

    def get_expiration_date(self): # get expiration date
        return self.__expiration_date

    def __str__(self):
        return "{}: {}, ${}, Expires on {}".format(self.__category, self.__name, round(self.__price, 2), self.__expiration_date)

class Dairy(Item): #dairy subclass
    dairy_items = []
    def __init__(self, name, category, price, expiration_date, pasture_raised):
        super().__init__(name, category, price, expiration_date)
        self.__pasture_raised = pasture_raised
        Dairy.dairy_items.append(self)

    def get_spec(self):
        #your code here
        #return __pasture_raised
        return self.__pasture_raised

    def __str__(self):
        return "{}, {}".format(super().__str__(), self.get_spec())

#define FruitVegetable, Seafood and Poultry Subclass
#these are alll polymorphic class.
class FruitVegetable(Item): #fv subclass
    veg_fruit_items = []

    def __init__(self, category, name, price, expiration_date, organic):
        super().__init__(category, name, price, expiration_date)
        self.__organic = organic # set organic
        FruitVegetable.veg_fruit_items.append(self) # append to list

    def get_spec(self):
        return self.__organic

    def __str__(self):
        return "{}, {}".format(super().__str__(), self.get_spec())


class Seafood(Item): #seafood subclass
    seafood_items = []

    def __init__(self, category, name, price, expiration_date, wild_caught):
        super().__init__(category, name, price, expiration_date)
        self.__wild_caught = wild_caught # set wild caught
        Seafood.seafood_items.append(self) # append to list

    def get_spec(self):
        return self.__wild_caught

    def __str__(self):
        return "{}, {}".format(super().__str__(), self.get_spec())


class Poultry(Item): # poultry subclass
    poultry_items = []

    def __init__(self, category, name, price, expiration_date, organic):
        super().__init__(category, name, price, expiration_date)
        self.__organic = organic # set organic
        Poultry.poultry_items.append(self) # append to list

    def get_spec(self):
        return self.__organic

    def __str__(self):
        return "{}, {}".format(super().__str__(), self.get_spec())

#process file
#open file, read information, create different category of objects
def FilePro(filename):
    '''Processes the input file and creates item objects'''
    with open(filename, 'r') as f:
        for line in f:
            p = line.strip().split('|')
            # name/ category/ price/ expiration date
            #  the name is the first part category is third from last
            # price is the second from last expiration date is  last
            name, category, price, expiration_date = p[0], p[-3], float(p[-2]), p[-1]
            if len(p) > 4: # if the line has more than 4 parts to see if there is a speciality tag
                speciality = p[1]
            else:
                speciality = None #if there isnt a specialty set it to none

            # if category is dairy it creates a dairy object
            # uses the provided specialty but if there isnt one it sets to default
            if category == "Dairy":
                if speciality is None: #if none update to default
                    speciality = "Non Pasture Raised"
                Dairy(category, name, price, expiration_date, speciality)
            # if category is Fruit or veg it creates a dairy object
            # uses the provided specialty but if there isnt one it sets to default
            elif category in ["Fruit", "Vegetable"]:
                if speciality is None:
                    speciality = "Non Organic"
                FruitVegetable(category, name, price, expiration_date, speciality)
            # if category is Seafood it creates a dairy object
            # uses the provided specialty but if there isnt one it sets to default
            elif category == "Seafood":
                if speciality is None:
                    speciality = "Farm Raised"
                Seafood(category, name, price, expiration_date, speciality)
            # if category is Poultry it creates a dairy object
            # uses the provided specialty but if there isnt one it sets to default
            elif category == "Poultry":
                if speciality is None:
                    speciality = "Non Organic"
                Poultry(category, name, price, expiration_date, speciality)

FilePro("Grocerys.txt") # call the file
'''
Testing code to check object creation per category list
Comment out when done. After successful completion
of class, the following code will print each item in the input file


print('+++++ Dairy +++++')
for item in Dairy.dairy_items:
    print(item)

print('+++++ Fruit & Vegetable ++++')
for item in FruitVegetable.veg_fruit_items:
    print(item)

print('+++++ Seafood +++++')
for item in Seafood.seafood_items:
    print(item)

print('+++++ Poultry +++++')
for item in Poultry.poultry_items:
    print(item)
'''





          

