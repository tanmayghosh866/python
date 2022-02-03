# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 00:29:23 2022

@author: Tanmay.Ghosh
"""


import random


#HEADING
print("WELCOME TO TANMAY'S RESTAURANT")

#list1 = [list2[]]

# first menu print

global f
f = 0
def main_menu():
        global f
        f = f+1
        print("\nMENU")
        print("\n ")
        print("PLEASE SELECT YOUR MEAL COURSE")
        print("\n ")
        print("1. Vegeterian full menu")
        print("2. Non-Vegeterian full menu")
        print("3. Jain preparation menu")    
    
        food = int(input("choose your option: "))
        if food == 1:
            veg()
        elif food == 2:
            non_veg()
        elif food == 3:
            jain()
        else:
            print("Incorrect choice")
            return main_menu()
    
    #second menu after choice selection
    
def veg():
        
        print("\nVegeterian full course")
        print("\n ")
        print("PLEASE SELECT YOUR CUISINE")
        print("\n ")
        print("1. Veg in Chinese")
        print("2. Veg in Indian")
        print("3. Veg in Italian")
        print("4. Veg in Continental")
        print("5. Back to Main Menu") 
        cuisine = int(input("choose your cuisine: "))
        if cuisine  == 5:
            main_menu()
        elif cuisine == 1:
            veg_chinese()
        elif cuisine == 2:
            veg_indian()
        elif cuisine == 3:
            veg_italian()
        elif cuisine == 4:
            veg_continental()
        else:
            print("Incorrect choice")
            return main_menu()
        


# non-veg full course

def non_veg():
        
        print("\nNon-Vegeterian full course")
        print("\n ")
        print("PLEASE SELECT YOUR CUISINE")
        print("\n ")
        print("1. Non-Veg in Chinese")
        print("2. Non-Veg in Indian")
        print("3. Non-Veg in Italian")
        print("4. Non-Veg in Continental")
        print("5. Back to Main Menu") 
        nonveg = int(input("choose your cuisine: "))
        if nonveg  == 5:
            main_menu()
        elif nonveg == 1:
            non_veg_chinese()
        elif nonveg == 2:
            non_veg_indian()
        elif nonveg == 3:
            non_veg_italian()
        elif nonveg == 4:
            non_veg_continental()
        else:
            print("Incorrect choice")
            return main_menu()
    

########################################################################       
## jain preparation
###########################################################################
def jain():
        
        print("\n Jain Full course")
        print("\n ")
        print("PLEASE SELECT YOUR JAIN DISH")
        print("\n ")
        print("1. Jain thali")
        print("2. Sabu dana khichri")
        print("3. Vegetable korma and Rice")
        print("4. Dessert and sweets")
        print("5. Back to Main Menu") 
        jain_food = int(input("choose your choice of dish: "))
        if jain_food  == 5:
            main_menu()
            return 0
        
        ############################################
        elif jain_food == 1:
            a = 250
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
      ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            jain()
                            return 0
                        
                    elif payment == 1:      
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Jain Thali is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            ########################################
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Jain Thali is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                           ############################################
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Jain Thali is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return jain()
                           ######################################
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        #######################################################
        elif jain_food == 2:
            a = 185
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            jain()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Sabu Dana Khichri is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Sabu Dana Khichri is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Sabu Dana Khichri is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return jain()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        ############################################    
        elif jain_food == 3:
            a = 350
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            jain()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Rice and korma is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Rice and Korma is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Rice and Korma is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return jain()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            ############################################
            
        elif jain_food == 4:
            a = 275
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            jain()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Dessert and sweets is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Dessert and sweets is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Dessert and sweets is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return jain()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            else:
                print("Incorrect choice")
                return main_menu()
            ############################################
#########################################
##Vegetarian Menu
#########################################
            
####################################################################################################
# VEG IN CHINESE PREPARATION
####################################################################################################

def veg_chinese():
        
        print("\n Veg Chinese Full course")
        print("\n ")
        print("PLEASE SELECT YOUR DISH")
        print("\n ")
        print("1. Gobi Manchurian with Rice")
        print("2. Vegetable chowmein")
        print("3. Vegetable fried with soya sauce")
        print("4. Soya bean stew with garlic bread")
        print("5. Back to Main Menu") 
        chin_food = int(input("choose your choice of dish: "))
        if chin_food  == 5:
            main_menu()
            return 0
        
        ############################################
        elif chin_food == 1:
            a = 175
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
      ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_chinese()
                            return 0
                        
                    elif payment == 1:      
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Gobi Manchurian with Rice is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            ########################################
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Gobi Manchurian with Rice is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                           ############################################
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Gobi Manchurian with Rice is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_chinese()
                           ######################################
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        #######################################################
        elif chin_food == 2:
            a = 185
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_chinese()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Vegetable chowmein is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Vegetable chowmein is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Vegetable chowmein is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_chinese()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        ############################################    
        elif chin_food == 3:
            a = 185
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            jain()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Vegetable fried with soya sauce is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Vegetable fried with soya sauce is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Vegetable fried with soya sauce is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_chinese()
                        
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            ############################################
            
        elif chin_food == 4:
            a = 215
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            jain()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Soya bean stew with garlic bread is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Soya bean stew with garlic bread is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Soya bean stew with garlic bread is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_chinese()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            else:
                        print("Incorrect choice")
                        return main_menu()

####################################################################################################
# VEG IN INDIAN PREPARATION
####################################################################################################

def veg_indian():
        
        print("\n Veg Indian Full course")
        print("\n ")
        print("PLEASE SELECT YOUR DISH")
        print("\n ")
        print("1. Dal tadka and tandoori roti")
        print("2. Dal baati Choorma")
        print("3. Masala Dosa")
        print("4. Khichdi and kadi")
        print("5. Back to Main Menu") 
        veg_food = int(input("choose your choice of dish: "))
        if veg_food  == 5:
            main_menu()
            return 0
        
        ############################################
        elif veg_food == 1:
            a = 175
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
      ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_indian()
                            return 0
                        
                    elif payment == 1:      
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Dal tadka and tandoori roti is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            ########################################
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Dal tadka and tandoori roti is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                           ############################################
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Dal tadka and tandoori roti is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_indian()
                           ######################################
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        #######################################################
        elif veg_food == 2:
            a = 185
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_indian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Dal baati Choorma is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Dal baati Choorma is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Dal baati Choorma is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_indian()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        ############################################    
        elif veg_food == 3:
            a = 185
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_indian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Masala Dosa is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Masala Dosa is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Masala Dosa is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_indian()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            ############################################
            
        elif veg_food == 4:
            a = 215
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_indian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Khichdi and kadi is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Khichdi and kadi is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Khichdi and kadi is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_indian()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            else:
                        print("Incorrect choice")
                        return main_menu()

####################################################################################################
# VEG IN ITALIAN PREPARATION
####################################################################################################

def veg_italian():
        
        print("\n Veg Italian Full course")
        print("\n ")
        print("PLEASE SELECT YOUR DISH")
        print("\n ")
        print("1. White sauce pasta")
        print("2. Vegetable Lasagna")
        print("3. Red sauce Speghetti")
        print("4. Vegetable Pizza")
        print("5. Back to Main Menu") 
        veg_food = int(input("choose your choice of dish: "))
        if veg_food  == 5:
            main_menu()
            return 0
        
        ############################################
        elif veg_food == 1:
            a = 175
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
      ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_italian()
                            return 0
                        
                    elif payment == 1:      
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} White sauce pasta is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            ########################################
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} White sauce pasta is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                           ############################################
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} White sauce pasta is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_italian()
                           ######################################
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        #######################################################
        elif veg_food == 2:
            a = 185
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_italian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Vegetable Lasagna is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Vegetable Lasagna is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Vegetable Lasagna is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_italian()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        ############################################    
        elif veg_food == 3:
            a = 185
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_italian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Red sauce Speghetti is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Red sauce Speghetti is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Red sauce Speghetti is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_italian()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            ############################################
            
        elif veg_food == 4:
            a = 215
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_italian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Vegetable Pizza is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Vegetable Pizza is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Vegetable Pizza is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_italian()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            else:
                        print("Incorrect choice")
                        return main_menu()
        
####################################################################################################
# VEG IN CONTINENTAL PREPARATION
####################################################################################################

def veg_continental():
        
        print("\n Veg continental Full course")
        print("\n ")
        print("PLEASE SELECT YOUR DISH")
        print("\n ")
        print("1. vietnamese vegetable pho")
        print("2. Spinach and Ricotta gnocchi")
        print("3. Vegetable Wellington")
        print("4. Veg tatin with blue cheese")
        print("5. Back to Main Menu") 
        veg_food = int(input("choose your choice of dish: "))
        if veg_food  == 5:
            main_menu()
            return 0
        
        ############################################
        elif veg_food == 1:
            a = 265
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
      ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_continental()
                            return 0
                        
                    elif payment == 1:      
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} vietnamese vegetable pho is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            ########################################
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} vietnamese vegetable pho is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                           ############################################
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} vietnamese vegetable pho is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_continental()
                           ######################################
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        #######################################################
        elif veg_food == 2:
            a = 195
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_continental()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Spinach and Ricotta gnocchi is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Spinach and Ricotta gnocchi is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Spinach and Ricotta gnocchi is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_continental()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        ############################################    
        elif veg_food == 3:
            a = 185
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_continental()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Vegetable Wellington is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Vegetable Wellington is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Vegetable Wellington is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_continental()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            ############################################
            
        elif veg_food == 4:
            a = 215
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            veg_italian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Veg tatin with blue cheese is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Veg tatin with blue cheese is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Veg tatin with blue cheese is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return veg_continental()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            else:
                        print("Incorrect choice")
                        return main_menu()
            
#########################################################
###############NON-VEG MENU###############################
##############################################################

##########################################
##non-veg chinese
#########################################

def non_veg_chinese():
        
        print("\n non-veg chinese Full course")
        print("\n ")
        print("PLEASE SELECT YOUR DISH")
        print("\n ")
        print("1. chilly chicken with fried rice")
        print("2. Shrimp fried rice")
        print("3. Chicken Noodles")
        print("4. Fish fillet with shezwann sauce")
        print("5. Back to Main Menu") 
        non_veg_food = int(input("choose your choice of dish: "))
        if non_veg_food  == 5:
            main_menu()
            return 0
        
        ############################################
        elif non_veg_food == 1:
            a = 285
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
      ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_chinese()
                            return 0
                        
                    elif payment == 1:      
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} chilly chicken with fried rice is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            ########################################
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} chilly chicken with fried rice is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                           ############################################
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} chilly chicken with fried rice is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_chinese()
                           ######################################
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        #######################################################
        elif non_veg_food == 2:
            a = 230
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_chinese()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Shrimp fried rice is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Shrimp fried rice is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Shrimp fried rice is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_chinese()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        ############################################    
        elif non_veg_food == 3:
            a = 155
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_chinese()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Chicken Noodles is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Chicken Noodles is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Chicken Noodles is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_chinese()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            ############################################
            
        elif non_veg_food == 4:
            a = 245
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_chinese()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Fish fillet with shezwann sauce is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Fish fillet with shezwann sauce is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Fish fillet with shezwann sauce is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_chinese()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            else:
                        print("Incorrect choice")
                        return main_menu()
            
##########################################
##non-veg indian
#########################################

def non_veg_indian():
        
        print("\n non-veg indian Full course")
        print("\n ")
        print("PLEASE SELECT YOUR DISH")
        print("\n ")
        print("1. Butter chicken with Naan")
        print("2. Fish curry with pulao")
        print("3. Chicken Biriyani")
        print("4. Mutton Biriyani")
        print("5. Back to Main Menu") 
        non_veg_food = int(input("choose your choice of dish: "))
        if non_veg_food  == 5:
            main_menu()
            return 0
        
        ############################################
        elif non_veg_food == 1:
            a = 190
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
      ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_indian()
                            return 0
                        
                    elif payment == 1:      
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Butter chicken with Naan is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            ########################################
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Butter chicken with Naan is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                           ############################################
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Butter chicken with Naan is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_indian()
                           ######################################
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        #######################################################
        elif non_veg_food == 2:
            a = 295
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_indian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Fish curry with pulao is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Fish curry with pulao is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Fish curry with pulao is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_indian()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        ############################################    
        elif non_veg_food == 3:
            a = 350
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_indian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Chicken Biriyani is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Chicken Biriyani is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Chicken Biriyani is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_indian()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            
            ############################################
            
        elif non_veg_food == 4:
            a = 390
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_indian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Mutton Biriyani is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Mutton Biriyani is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Mutton Biriyani is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_indian()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            else:
                        print("Incorrect choice")
                        return main_menu()
            
##########################################
##non-veg italian
#########################################

def non_veg_italian():
        
        print("\n non-veg italian Full course")
        print("\n ")
        print("PLEASE SELECT YOUR DISH")
        print("\n ")
        print("1. Spaghetti Carbonara")
        print("2. Antipasto Italiano with ham")
        print("3. Pork Braciola")
        print("4. Pizza Margherita with ham")
        print("5. Back to Main Menu") 
        non_veg_food = int(input("choose your choice of dish: "))
        if non_veg_food  == 5:
            main_menu()
            return 0
        
        ############################################
        elif non_veg_food == 1:
            a = 290
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
      ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_italian()
                            return 0
                        
                    elif payment == 1:      
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Spaghetti Carbonara is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            ########################################
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Spaghetti Carbonara is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                           ############################################
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Spaghetti Carbonara is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_italian()
                           ######################################
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        #######################################################
        elif non_veg_food == 2:
            a = 175
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_italian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Antipasto Italiano with ham is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Antipasto Italiano with ham is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Antipasto Italiano with ham is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_italian()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        ############################################    
        elif non_veg_food == 3:
            a = 349
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_italian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Pork Braciola is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Pork Braciola is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Pork Braciola is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_italian()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            ############################################
            
        elif non_veg_food == 4:
            a = 275
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_italian()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Pizza Margherita with ham is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Pizza Margherita with ham is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Pizza Margherita with ham is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_italian()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            else:
                        print("Incorrect choice")
                        return main_menu()
            
##########################################
##non-veg continental
#########################################

def non_veg_continental():
        
        print("\n non-veg italian Full course")
        print("\n ")
        print("PLEASE SELECT YOUR DISH")
        print("\n ")
        print("1. Crispy Calamari Rings")
        print("2. Grilled Chicken Breasts With Chillies & Lemongrass")
        print("3. Sausage Pepper Burger")
        print("4. Glazed Ham")
        print("5. Back to Main Menu") 
        non_veg_food = int(input("choose your choice of dish: "))
        if non_veg_food  == 5:
            main_menu()
            return 0
        
        ############################################
        elif non_veg_food == 1:
            a = 445
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
      ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_continental()
                            return 0
                        
                    elif payment == 1:      
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Crispy Calamari Rings is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            ########################################
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Crispy Calamari Rings is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                           ############################################
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Crispy Calamari Rings is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_continental()
                           ######################################
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        #######################################################
        elif non_veg_food == 2:
            a = 525
            b = (a * 0.05) + a
            
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_continental()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Grilled Chicken Breasts With Chillies & Lemongrass is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Grilled Chicken Breasts With Chillies & Lemongrass is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Grilled Chicken Breasts With Chillies & Lemongrass is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_continental()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
        ############################################    
        elif non_veg_food == 3:
            a = 650
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                           non_veg_continental()
                           return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Sausage Pepper Burger is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Sausage Pepper Burger is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Sausage Pepper Burger is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_continental()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            ############################################
            
        elif non_veg_food == 4:
            a = 775
            b = (a * 0.05) + a    
            x=random.randint(10908,500876)
            randomRef=str(x)
            print("Your order ID is {}".format(randomRef))
            print("\n ")
            print("Your meal price is {} and with GST total bill is {} per plate".format(a,b))
            qty = int(input("Enter your quantity: "))
            if qty == 0:
                print("Please enter a valid number")
                
            elif qty <50:
                    final = qty * b
                    print("Your final bill is {}".format(final))
                    print("PLEASE SELECT YOUR PAYMENT METHOD")
                    print("\n ")
                    print("1. Credit/Debit Card")
                    print("2. UPI payment")
                    print("3. Cash")
                    print("4. Back to previous menu")
        
                    ############################################
                    payment = int(input("choose your payment method: "))
                    if payment  == 4:
                            non_veg_continental()
                            return 0
                    elif payment == 1:
                            charge_bill = (0.02*final) + final
                            print("Your final payment of card for txn ID {} is {}".format(randomRef, charge_bill))
                            print("\n ")
                            print("Your order for {} Glazed Ham is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                            
                    elif payment == 2:
                           charge_bill = (0.01*final) + final
                           print("Your final payment of UPI for txn ID {} is {}".format(randomRef, charge_bill))
                           print("\n ")
                           print("Your order for {} Glazed Ham is ready to be delivered".format(qty))
                           print("\n")
                           main_menu()
                           return 0
                    
                    elif payment == 3:
                            
                            print("Your final payment of cash for txn ID {} is {}".format(randomRef, final))
                            print("\n ")
                            print("Your order for {} Glazed Ham is ready to be delivered".format(qty))
                            print("\n")
                            main_menu()
                            return 0
                    else:
                        print("Incorrect choice")
                        return non_veg_continental()
                           
                    
            elif qty > 50:
                print("This is a bulk order, please place the order manually with the manager. Thank You!")
                print("\n ")
                print("Returning back to main menu")
                main_menu()
                return 0
            else:
                        print("Incorrect choice")
                        return main_menu()
        

       
main_menu()





    
    
                   
    


        


    