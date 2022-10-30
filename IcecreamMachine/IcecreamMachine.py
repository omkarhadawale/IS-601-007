'''
Name: Omkar Karbhari Hadawale
UCID: oh45
Date:23/10/2022 

'''

from enum import Enum
from IcecreamExceptions import ExceededRemainingChoicesException, InvalidChoiceException, NeedsCleaningException, OutOfStockException
from IcecreamExceptions import InvalidPaymentException

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity = 10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException
        return self.quantity 

    def in_stock(self):
        return self.quantity > 0

class Container(Usable):
    pass

class Flavor(Usable):
    pass

class Toppings(Usable):
    pass

class STAGE(Enum):
    Container = 1
    Flavor = 2
    Toppings = 3
    Pay = 4

class IceCreamMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 100
    MAX_SCOOPS = 3
    MAX_TOPPINGS = 3


    containers = [Container(name="Waffle Cone", cost=1.5), Container(name="Sugar Cone", cost=1), Container("Cup", cost=1)]
    flavors = [Flavor(name="Vanilla", quantity=100, cost=1), Flavor(name="Chocolate", quantity=100, cost=1), Flavor(name="Strawberry", quantity=100, cost=1)]
    toppings = [Toppings(name="Sprinkles", quantity=200, cost=.25), Toppings(name="Chocolate Chips", quantity=200, cost=.25), Toppings(name="M&Ms", quantity=200, cost=.25), \
    Toppings(name="Gummy Bears", quantity=200, cost=.25), Toppings(name="Peanuts", quantity=200, cost=.25)] 


    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_scoops = MAX_SCOOPS
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_icecreams = 0

    inprogress_icecream = []
    currently_selecting = STAGE.Container

    # rules
    # 1 - container must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - scoops can't exceed max
    # 4 - toppings can't exceed max
    # 5 - a container and at least 1 scoop or toppings must be selected
    # 6 - proper cost must be calculated and shown to the user
    # 7 - cleaning must be done after certain number of uses before any more icecreams can be made
    # 8 - total sales should calculate properly based on cost calculation
    # 9 - total_icecreams should increment properly after a payment
    

    def pick_container(self, choice):
        for c in self.containers:
            if c.name.lower() == choice:
                c.use()
                self.inprogress_icecream.append(c)
                return
        raise InvalidChoiceException

    def pick_flavor(self, choice):
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_scoops <= 0:
            raise ExceededRemainingChoicesException
        for f in self.flavors:
            if f.name.lower() == choice and self.currently_selecting == STAGE.Flavor:
                f.use()
                self.inprogress_icecream.append(f)
                self.remaining_scoops -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException

    def pick_toppings(self, choice):
        if self.remaining_toppings <= 0:
            raise ExceededRemainingChoicesException
        for t in self.toppings:
            if t.name.lower() == choice and self.currently_selecting == STAGE.Toppings:
                t.use()
                self.inprogress_icecream.append(t)
                self.remaining_toppings -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        self.remaining_scoops = self.MAX_SCOOPS
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_icecream = []
        self.currently_selecting = STAGE.Container

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        
    def handle_container(self, container):
        self.pick_container(container)
        self.currently_selecting = STAGE.Flavor

    def handle_flavor(self, flavor):
        if flavor == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_flavor(flavor)

    def handle_toppings(self, toppings):
        if toppings == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_toppings(toppings)

    def handle_pay(self, expected, total):
        if total == str(expected):
            print("Thank you! Enjoy your icecream!")
            self.total_icecreams += 1
            self.total_sales += expected # only if successful
            self.reset()
        else:
            raise InvalidPaymentException
            
        ''' 
        Name: Omkar Karbhari Hadawale
        UCID: oh45
        This function calculates cost of current ice cream by interating over in 
        inprogress_icecream list and addind up cost element in each object in the list
        '''       
    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_icecream
        total_cost = 0
        for i in self.inprogress_icecream:
            total_cost += i.cost
        return total_cost 

    def run(self):
        
        if self.currently_selecting == STAGE.Container:
            container = input(f"Would you like a {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.containers))))}?\n")
            ''' 
            Name: Omkar Karbhari Hadawale
            UCID: oh45
            1)InvalidChoiceException: The InvalidChoiceException is handled by try except block.
            When the exception is thrown the user is given appropriate message and the run()
            is called again to ask user
            for another input.  
            2)OutOfStockException: The out of stock exception is handled by try except block.
            when the exception is thrown the user is given prompt to select from available choices.
            '''    
            try:
                self.handle_container(container.lower())
            except  OutOfStockException:
                print(f"The container '{container}' you selected in out of stock.")
                print("Please select from avialable ones")
                self.run()
            except InvalidChoiceException:
                print("Invalid Choice.Please select valid choice from below list")
                self.run()
        elif self.currently_selecting == STAGE.Flavor:
            flavor = input(f"Would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.flavors))))}? Or type next.\n")
            ''' 
            Name: Omkar Karbhari Hadawale
            UCID: oh45
            1)InvalidChoiceException: The InvalidChoiceException is handled by try except block.
                When the exception is thrown the user is given appropriate message and the run()
                is called again to ask user for another input.
            2)NeedsCleaningException:This exception is handled by the "except NeedsCleaningException:" 
                block.When the NeedsCleaningException is thrown the user is prompted that the machine is
                cleaned and the clean_machine() is called.Their after the run() is called recursively to
                ask user to make the choice again    
            3)ExceededRemainingChoicesException:This exception is handled by the "except ExceededRemainingChoicesException:" 
                block.When the exception is thrown the user is prompted that you have exceeded the maximum limit to select 
                the item and the user is directed to the next stage by setting the currently_selecting variable to next stage 
                and calling run() recursively.
            4)OutOfStockException: The out of stock exception is handled by try except block.
            when the exception is thrown the user is given prompt to select from available choices.
            ''' 
            try:
                self.handle_flavor(flavor.lower())
            except  OutOfStockException:
                print(f"The flavour '{flavor}' you selected in out of stock.")
                print("Please select from avialable ones")
                self.run()
            except InvalidChoiceException:
                print("Invalid Choice.Please select valid choice from below list")
                self.run()
            except NeedsCleaningException:
                print("The machine is being cleaned....Sorry for inconvinience")
                self.clean_machine()
                print("Please again make a choice")
                self.run()
            except ExceededRemainingChoicesException:
                print(f"Max Scoops exceeded. You can select maximum of {self.MAX_SCOOPS}scoops.\nPlease go ahead and select toppings")
                self.currently_selecting = STAGE.Toppings
                self.run()    
        elif self.currently_selecting == STAGE.Toppings:
            toppings = input(f"Would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")

            ''' 
            Name: Omkar Karbhari Hadawale
            UCID: oh45
            1)InvalidChoiceException: The InvalidChoiceException is handled by try except block.
                When the exception is thrown the user is given appropriate message and the run()
                is called again to ask user for another input.
            2)ExceededRemainingChoicesException:This exception is handled by the "except ExceededRemainingChoicesException:" 
                block.When the exception is thrown the user is prompted that you have exceeded the maximum limit to select 
                the item and the user is directed to the next stage by setting the currently_selecting variable to next stage 
                and calling run() recursively.
            3)OutOfStockException: The out of stock exception is handled by try except block.
                when the exception is thrown the user is given prompt to select from available choices.    
            ''' 
            try:
                self.handle_toppings(toppings.lower())
            except  OutOfStockException:
                print(f"The topping '{toppings}' you selected in out of stock.")
                print("Please select from avialable ones")
                self.run()
            except InvalidChoiceException:
                print("Invalid Choice.Please select valid choice from below list")
                self.run()
            except ExceededRemainingChoicesException:
                print(f"Max toppings exceeded. You can select maximum of {self.MAX_SCOOPS} toppings./n Please checkout and make payment")
                self.currently_selecting = STAGE.Pay
                self.run()    
        elif self.currently_selecting == STAGE.Pay:
            expected = self.calculate_cost()
            total = input(f"Your total is $ {expected}, please enter the exact value.\n")
            ''' 
            Name: Omkar Karbhari Hadawale
            UCID: oh45
            1)InvalidPaymentException: The InvalidChoiceException is handled by try except block.
                When the exception is thrown the user is to ask user to enter exact amount to complete the payment
                and the run() is called again recursively till the user enters exact value.     
            ''' 
            try:
                self.handle_pay(expected, total)
            except InvalidPaymentException:
                print(f"Please enter the correct amount.\nYou are expected to pay ${expected} but you entered ${total}")
                self.run()
            choice = input("What would you like to do? (icecream or quit)\n")
            if choice == "quit":
                exit()
        self.run()

    def start(self):
        self.run()

    
if __name__ == "__main__":
    icm = IceCreamMachine()
    icm.start()
