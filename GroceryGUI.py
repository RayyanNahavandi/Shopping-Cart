#import class from class file
#import GUI Module
from Rayyan_Nahavandi_final_project_CLASS import SmartCart, Item, Dairy, FruitVegetable, Seafood, Poultry, FilePro
from functools import partial
import random, string #used in random receipt no function
from tkinter import *


class MyFrame(Frame):
    def __init__(self, root):
        '''Constructor method'''
        Frame.__init__(self, root) #Frame class initialization
        self.init_container() #initialize all widget containers
        self.cart = SmartCart() #initialize SmartCart dict object - key = Item object item selected, value = quantity
        self.welcome() #start the application
        self.data = StringVar(self, 'Subtotal: 0.0') #Associated with subtotal label

        
    def init_container(self):
        '''Initialize widget containers'''
        self.quantity_entries = [] #qunatity entry list
        self.states = [] #holds state if selected/not i-th list item holds selection for i-th item
 
    def clear_frame(self): 
        '''Clears the previous frame'''
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        '''Exits the program'''
        root.destroy()

 
    def welcome(self):
        '''1. Welcome window - refer spec file for details'''
        self.clear_frame()
        Label(self, text = '****Welcome to Instant Cart!****', background="gray70").pack(side = TOP)
        #your code here
        #Start Ordering: Button – start the program, command = shop_by_category
        Button(self, text="Start Ordering", command=self.shop_by_category).pack()
        #Exit Application: Button – exit the program, command = exit_application
        Button(self, text="Exit Application", command=self.exit_application).pack()

        

    def shop_by_category(self):
        '''2. Widget to display different category of items - refer spec file for details'''
        self.clear_frame()
        self.init_container()
        #your code here
        #a.	Choose Category: label
        cat = Label(self, text="Choose Category")
        cat.grid(row=0, column=0)
        #b.	Dairy: Button – command = start (code below)
        self.dairy_button = Button(self, text="Dairy", command=partial(self.start, Dairy.dairy_items))
        self.dairy_button.grid(row=1, column=0)
        #partial is a special method to pass an argument during button command
        #for dairy category Dairy.dairy_items will be passed to display all dairy item
        self.dairy_button  = Button(self, text = "Dairy", command=partial(self.start, Dairy.dairy_items))
        #your code here
        #c.	Vegetable and Fruit - veg_fruit_button: Button – command = start (Same as dairy)
        self.fruit_veg_button = Button(self, text="Fruit & Vegetables",command=partial(self.start, FruitVegetable.veg_fruit_items))
        self.fruit_veg_button.grid(row=2, column=0)
        #d.	Poultry and Meat - poultry_meat_button: Button – command = start(Same as dairy)
        self.poultry_button = Button(self, text="Poultry", command=partial(self.start, Poultry.poultry_items))
        self.poultry_button.grid(row=3, column=0)
        #e.	Seafood: Button - seafood_button – command = start(Same as dairy)
        self.seafood_button = Button(self, text="Seafood", command=partial(self.start, Seafood.seafood_items))
        self.seafood_button.grid(row=4, column=0)
        #f.	Go Back: Button – command = welcome (go back to #1)
        self.back_button = Button(self, text="Go Back", command=self.welcome)
        self.back_button.grid(row=5, column=0)
        #layout manager for all the widgets

        
    def start(self, current_items):
        ''''3. Start ordering from selected category,
        list passed by command will be used as current_items'''
        self.clear_frame()
        self.init_container()
        
        #creating widgets for items using a for loop
        #iterative over each item of current items and
        #create that many checkbutton, price, exp date and specialty label,and quantity entry
        row = 0######### or use enumerate
        for item in current_items:
            self.states.append(IntVar()) #keeps track if an item is selected
            checkbutton = Checkbutton(self, text=item.get_name(), variable=self.states[row])#create check buttons
            checkbutton.grid(row = row, column = 0)

            #your code here
            #create and layout a price label, set text to item.get_price()
            start = Label(self, text="${}".format(round(item.get_price(), 2)))
            start.grid(row=row, column=1)
            #create and layout a quantity entry and append to quantity_entries, set width = 2
            quantity_entry = Entry(self, width=2)
            quantity_entry.grid(row=row, column=2)
            self.quantity_entries.append(quantity_entry)
            #create and layout exp_date_label and set text to item.get_expiration_date() method
            exp = Label(self, text=item.get_expiration_date())
            exp.grid(row=row, column=3)
            #create and layout speciality_label and set text to item.get_spec() method
            spec = Label(self, text=item.get_spec())
            spec.grid(row=row, column=4)
            row += 1
        #create and layout subtotal label, set textvaribale = self.data so it changes
        subtotal = Label(self, textvariable=self.data)
        subtotal.grid(row=row, column=0)
        #with each add_to_cart button being pressedng
        #create and layout select categories: button, command = shop_by_category
        select_categories = Button(self, text="Select Categories", command=self.shop_by_category)
        select_categories.grid(row=row + 1, column=0)
        #create and layout add_to_cart_button, command = partial(self.add_to_cart, current_items)
        add_to_cart = Button(self, text="Add to Cart", command=partial(self.add_to_cart, current_items))
        add_to_cart.grid(row=row + 1, column=1)
        #create and layout button: checkout, command = self.checkout
        checkout = Button(self, text="Checkout", command=self.checkout)
        checkout.grid(row=row + 1, column=2)

    def add_to_cart(self, current_items): #####
        '''3. Added to cart, displays subtotal - see spec file for details layout'''
        for i in range(len(current_items)):
            #your code here
            #get() the value of i-th item of self.states -> returns 1 if selected otherwise 0
            #if item is selected:
                #get the product quantity from quantity_entries using get() function
                #add item to self.cart dict where k = item object, v = quantity
            if self.states[i].get() == 1:  # item selected
                if self.quantity_entries[i].get():  # Check quantity entry has a value
                    quantity = int(self.quantity_entries[i].get())
                else:
                    quantity = 0  # default 0 if no value is entered

                if quantity > 0:  # add item to cart if quantity is greater than 0
                    self.cart[current_items[i]] = self.cart.get(current_items[i], 0) + quantity
            #set subtotal
            self.data.set("Subtotal: ${}".format(round(self.cart.subtotal(), 2)))
    def get_receipt_number(self):
        '''Generate random receipt number'''
        return  ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))

    def checkout(self):
        '''4. Check out window '''
        self.clear_frame()
        # your code here to create and layout following widgets:
        # refer to receipt frame
        # Your e-receipt: Label
        Label(self, text="Your e-receipt").pack()
        # Receipt Number: Label - Randomly generated by program - text = get_receipt_number()
        Label(self, text="Receipt Number: {}".format(self.get_receipt_number())).pack()
        # Name Price Quantity Expiration Date, Speciality: Header Label
        Label(self, text="Name      Price      Quantity      Expiration Date      Specialty").pack()
        # Item purchased, price quantity, exp.date, specialty: Label - from cart dictionary
        # using for loop to iterate over self.cart.items()
        for item, quantity in self.cart.items():
            Label(self, text="{}       ${}       {}       {}       {}".format(item.get_name(), round(item.get_price(), 2), quantity, item.get_expiration_date(), item.get_spec())).pack()
        # Subtotal: Label - get self.cart subtotal - new label
        Label(self, text="Subtotal: ${}".format(round(self.cart.subtotal(), 2))).pack()
        # Tax: Label - 4.3%
        Label(self, text="Tax: ${}".format(round(self.cart.tax(), 2))).pack()
        # Total: Label - subtotal + tax
        Label(self, text="Total: ${}".format(round(self.cart.total(), 2))).pack()
        # Apply coupon label
        Label(self, text="Apply Coupon:").pack()
        # An entry to obtain the discount code, for e.g. SAVE10
        self.coupon_entry = Entry(self)  # instance attribute
        self.coupon_entry.pack()
        # Create discount calculate button and command is apply_discount
        Button(self, text="Apply Discount", command=self.apply_discount).pack()
        # create two stringVar and initial text discount and discounted_total
        self.discount = StringVar()
        self.discount.set("Discount: $0.00")
        self.discounted_total = StringVar()
        self.discounted_total.set("Discounted Total: $0.00")
        Label(self, textvariable=self.discount).pack()
        Label(self, textvariable=self.discounted_total).pack()
        # ‘Thank you’ message: Label
        Label(self, text="Thank you for shopping!").pack()
        # Exit application: Button – exit the program- command = exit_application
        Button(self, text="Exit", command=self.exit_application).pack()

    def apply_discount(self):
        # your code here
        # check if user entered any discount
        # set the two stringVar to cart's methods discount and discounted_total
        coupon = self.coupon_entry.get()
        #calculate discount
        discount = round(self.cart.discount(coupon), 2)
        discounted_total = round(self.cart.discounted_total(coupon), 2)
        #update StringVar
        self.discount.set("Discount: ${}".format(discount))
        self.discounted_total.set("Discounted Total: ${}".format(discounted_total))

#main driver code
root = Tk()
#your code here
#create root window
root.title("Instant Cart") #set window title
#your code here
frame = MyFrame(root)
#create a myframe object and layout
frame.pack()
#call mainloop
root.mainloop()



