'''
Name: Omkar Karbhari Hadawale
UCID: oh45
Date:23/10/2022 

'''

import logging
import random
from IcecreamExceptions import ExceededRemainingChoicesException, InvalidChoiceException, NeedsCleaningException, OutOfStockException
import IcecreamMachine
import pytest


'''Test-1
    Name: Omkar Karbhari Hadawale
    UCID: oh45  
    Until the container is not picked we cannot select flavour because the currently_selecting will still have
    container as its stage.Thus the pick flavour method will raise invalid choice exception even we make right
    choice as the other condition evalutes to false,where it checks weather self.currently_selecting == STAGE.Flavor
    and same for the toppings.
'''
def test_container_first():
    test = IcecreamMachine.IceCreamMachine()
    before_inprog_lst_length = len(test.inprogress_icecream)
    try:
        test.pick_flavor('Vanilla')
    except InvalidChoiceException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(test.inprogress_icecream))  


'''Test-2
    Name: Omkar Karbhari Hadawale
    UCID: oh45 
    The test case verifies that user should not be able to select the flavour if it's not in stock.
    The OutOfStockException is catched in the test case which is the indicator that when flavour not in
    stock this exception is raised.Further in finally block we check weather the lenght of inprogress icecream list 
    to verify that the flavour is not added.  
    '''
def test_flavour_in_stock():
    test = IcecreamMachine.IceCreamMachine()
    before_inprog_lst_length = len(test.inprogress_icecream)
    test.flavors[0].quantity = 0
    name = test.flavors[0].name.lower()
    test.currently_selecting = IcecreamMachine.STAGE.Flavor
    try:
        test.pick_flavor(name)
    except OutOfStockException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(test.inprogress_icecream))   
        
'''Test-3
    Name: Omkar Karbhari Hadawale
    UCID: oh45  
    The test case verifies that user should not be able to select the topping if it's not in stock.
    The OutOfStockException is catched in the test case which is the indicator that when topping not in
    stock this exception is raised.Further in finally block we check weather the lenght of inprogress icecream list 
    to verify that the topping is not added.  
    '''
def test_topping_in_stock():
    test = IcecreamMachine.IceCreamMachine()
    before_inprog_lst_length = len(test.inprogress_icecream)
    test.toppings[0].quantity = 0
    name = test.toppings[0].name.lower()
    test.currently_selecting = IcecreamMachine.STAGE.Toppings
    try:
        test.pick_toppings(name)
    except OutOfStockException:
        assert(before_inprog_lst_length == len(test.inprogress_icecream))
    finally:
        assert(before_inprog_lst_length == len(test.inprogress_icecream))



'''Test-4
    Name: Omkar Karbhari Hadawale
    UCID: oh45  
    The test case verifies the user should be able to add max 3 scoops by setting remaining_scoops to zero and then checking 
    weather the ExceededRemainingChoicesException is thrown or not.Further in finally block we check weather the lenght of inprogress icecream list 
    to verify that the flavour is not added.
    '''
def test_add_3_flavour():
    test = IcecreamMachine.IceCreamMachine()
    test.remaining_scoops = 0
    before_inprog_lst_length = len(test.inprogress_icecream)
    test.currently_selecting = IcecreamMachine.STAGE.Flavor
    try:
        test.pick_flavor('Vanilla')
    except ExceededRemainingChoicesException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(test.inprogress_icecream))



'''Test-5
    Name: Omkar Karbhari Hadawale
    UCID: oh45  
    The test case verifies the user should be able to add max 3 toppins by setting remaining_toppings to zero and then checking 
    weather the ExceededRemainingChoicesException is thrown or not.Further in finally block we check weather the lenght of inprogress icecream list 
    to verify that the topping is not added. 
    '''
def test_add_3_toppings():
    test = IcecreamMachine.IceCreamMachine()
    test.remaining_toppings = 0
    before_inprog_lst_length = len(test.inprogress_icecream)
    test.currently_selecting = IcecreamMachine.STAGE.Toppings
    try:
        test.pick_toppings('Sprinkles')
    except ExceededRemainingChoicesException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(test.inprogress_icecream))

'''Test-6
    Name: Omkar Karbhari Hadawale
    UCID: oh45  
    The the test case buys a ice cream with random combination of container,flavour and topping 
    and then comparing the expected price with the actual price calculated by calculate_cost() method
    '''
def test_calculate_cost():
    test = IcecreamMachine.IceCreamMachine()
    r = 0
    while r < 4:
        i = random.randrange(0, 3, 1)
        j = random.randrange(0, 3, 1)
        k = random.randrange(0, 3, 1)
        sample_ice_cream = [test.containers[i],test.flavors[j],test.toppings[k]]
        ExpectedPrice = sample_ice_cream[0].cost + sample_ice_cream[1].cost + sample_ice_cream[2].cost

        test_usable = IcecreamMachine.IceCreamMachine()
        test_usable.inprogress_icecream = sample_ice_cream
        ActualPrice = test_usable.calculate_cost()

        assert(ActualPrice==ExpectedPrice)
    
        r += 1

'''Test-7
    Name: Omkar Karbhari Hadawale
    UCID: oh45  
    The test case buys 2 ice creams and then compares the expected total scales price with 
    the actual total scales set by handle_pay method.
    '''
def test_total_sales():
    test = IcecreamMachine.IceCreamMachine()
    test.handle_pay(2.5,'2.5')
    test.handle_pay(2,'2')
    expected_total_sales = 2.5 + 2
    assert(expected_total_sales==test.total_sales)

'''Test-8
    Name: Omkar Karbhari Hadawale
    UCID: oh45  
    The test case buys 2 ice creams and checks weather the total_icecream count is 2 or not.
    '''
def test_icecream_increment():
    test = IcecreamMachine.IceCreamMachine()
    test.handle_pay(2.5,'2.5')
    test.handle_pay(2,'2')
    expected_total_icecreams = 2
    assert(expected_total_icecreams==test.total_icecreams)

