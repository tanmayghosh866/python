# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import datetime
from datetime import date
import pandas as pd
import csv


global a
a = [] 

# Customer first page
print("WELCOME TO SAYANI BUS SERVICES")

##Bus 1

def bus1():
    x = random.randint(100200, 900200)
    TXNID = str(x)
    y = random.randint(1100, 1200)
    fare = int(y)
    print("SELECT NUMBER OF SEATS")
    print("\n ")
    seats = int(input("Enter number of seats required: "))
    if seats > 10:
        print("Maximum seat capacity is 10, please select a different date")
        date_func()
        bus1()
    else:
        print("You have selected {} seats".format(seats))
        print("\n")
        print("Your Transaction ID is {}".format(TXNID))
        print("\n")
        final_fare = seats * fare
        print("Your final fare for {} seats booking would be {} rupees".format(seats, final_fare))
        print("\n")
        if seats not in a:
            a.append(seats)
        if TXNID not in a:
            a.append(TXNID)
####################################################################
        print("\n\nPASSENGER DETAILS\n")
        print("1.Enter passenger details")
        print("2.Go back")
        option = int(input("\nEnter your option : "))
        
        if option == 2:
            function_bus_type()
            return 0
        elif option == 1:
        		people = int(input("\nRe-confirm number of passengers: "))
        		name_l = []
        		age_l = []
        		sex_l = []
        		for p in range(people):
        			name = str(input("\nName : "))
        			name_l.append(name)
        			age  = int(input("\nAge  : "))
        			age_l.append(age)
        			sex  = str(input("\nMale or Female : "))
        			sex_l.append(sex)
        
        		restart = str(input("\nshould we proceed ahead?  Y/N : "))
        		if restart in ('n','NO','no','No'):
        			restart = ('N')
        		else :
        			x = 0
        			print("\nTotal Ticket : ",people)
        			for p in range(1,people+1):
        				print("Ticket : ",p)
        				print("Name : ", name_l[x])
        				print("Age  : ", age_l[x])
        				print("Sex : ",sex_l[x])
        				x += 1

####################################################################
        print("PLEASE SELECT YOUR PAYMENT METHOD")
        print("\n")
        print("1. Credit or Debit Card")
        print("2. UPI interface payment")
        print("3. Cash payment")
        print("4. Back to previous menu")         

#######################################

        payment = int(input("Choose your payment method: "))
        if payment == 4:
            function_bus_type()
            return 0 
        elif payment == 1:
            final_payment = final_fare * 1.02 
            print("Your final payment of card for TXN ID {} is {}".format(TXNID,final_payment))
            print("\n")
            print("Your order of ID {} for {} tickets will be emailed within 1 hour ".format(TXNID, seats))
            print("\n")
            main_bus_menu()
            return 0 
            ################################################
        elif payment == 2:
            final_payment = final_fare * 1.01 
            print("Your final payment of card for TXN ID {} is {}".format(TXNID,final_payment))
            print("\n")
            print("Your order of ID {} for {} tickets will be emailed within 1 hour ".format(TXNID, seats))
            print("\n")
            main_bus_menu()
            return 0 
        elif payment == 3:
            final_payment = final_fare * 1
            print("Your final payment of card for TXN ID {} is {}".format(TXNID,final_payment))
            print("\n")
            print("Your order of ID {} for {} tickets will be emailed within 1 hour ".format(TXNID, seats))
            print("\n")
            main_bus_menu()
            return 0 
        else:
            print("incorrect choice")
            function_bus_type()
##########################################################################################################
def bus2():
    x = random.randint(100200, 900200)
    TXNID = str(x)
    y = random.randint(800, 1000)
    fare = int(y)
    print("SELECT NUMBER OF SEATS")
    print("\n ")
    seats = int(input("Enter number of seats required: "))
    if seats > 10:
        print("Maximum seat capacity is 10, please select a different date")
        date_func()
        bus2()
    else:
        print("You have selected {} seats".format(seats))
        print("\n")
        print("Your Transaction ID is {}".format(TXNID))
        print("\n")
        final_fare = seats * fare
        print("Your final fare for {} seats booking would be {} rupees".format(seats, final_fare))
        print("\n")
        if seats not in a:
            a.append(seats)
        if TXNID not in a:
            a.append(TXNID)
####################################################################
        print("\n\nPASSENGER DETAILS\n")
        print("1.Enter passenger details")
        print("2.Go back")
        option = int(input("\nEnter your option : "))
        
        if option == 2:
            function_bus_type()
            return 0
        elif option == 1:
        		people = int(input("\nRe-confirm number of passengers: "))
        		name_l = []
        		age_l = []
        		sex_l = []
        		for p in range(people):
        			name = str(input("\nName : "))
        			name_l.append(name)
        			age  = int(input("\nAge  : "))
        			age_l.append(age)
        			sex  = str(input("\nMale or Female : "))
        			sex_l.append(sex)
        
        		restart = str(input("\nshould we proceed ahead? Y/N : "))
        		if restart in ('n','NO','no','No'):
        			restart = ('N')
        		else :
        			x = 0
        			print("\nTotal Ticket : ",people)
        			for p in range(1,people+1):
        				print("Ticket : ",p)
        				print("Name : ", name_l[x])
        				print("Age  : ", age_l[x])
        				print("Sex : ",sex_l[x])
        				x += 1

####################################################################
        print("PLEASE SELECT YOUR PAYMENT METHOD")
        print("\n")
        print("1. Credit/Debit Card")
        print("2. UPI Payment")
        print("3. Cash")
        print("4. Back to previous menu")         

#######################################

        payment = int(input("Choose your payment method: "))
        if payment == 4:
            function_bus_type()
            return 0 
        elif payment == 1:
            final_payment = final_fare * 1.02 
            print("Your final payment of card for TXN ID {} is {}".format(TXNID,final_payment))
            print("\n")
            print("Your order of ID {} for {} tickets will be emailed within 1 hour ".format(TXNID, seats))
            print("\n")
            main_bus_menu()
            return 0 
            ################################################
        elif payment == 2:
            final_payment = final_fare * 1.01 
            print("Your final payment of card for TXN ID {} is {}".format(TXNID,final_payment))
            print("\n")
            print("Your order of ID {} for {} tickets will be emailed within 1 hour ".format(TXNID, seats))
            print("\n")
            main_bus_menu()
            return 0 
        elif payment == 3:
            final_payment = final_fare * 1
            print("Your final payment of card for TXN ID {} is {}".format(TXNID,final_payment))
            print("\n")
            print("Your order of ID {} for {} tickets will be emailed within 1 hour ".format(TXNID, seats))
            print("\n")
            main_bus_menu()
            return 0 
        else:
            print("incorrect choice")
            function_bus_type()
    
##########################################################################################################
def bus3():
    x = random.randint(100200, 900200)
    TXNID = str(x)
    y = random.randint(750, 800)
    fare = int(y)
    print("SELECT NUMBER OF SEATS")
    print("\n ")
    seats = int(input("Enter number of seats required: "))
    if seats > 10:
        print("Maximum seat capacity is 10, please select a different date")
        date_func()
        bus3()
    else:
        print("You have selected {} seats".format(seats))
        print("\n")
        print("Your Transaction ID is {}".format(TXNID))
        print("\n")
        final_fare = seats * fare
        print("Your final fare for {} seats booking would be {} rupees".format(seats, final_fare))
        print("\n")
        if seats not in a:
            a.append(seats)
        if TXNID not in a:
            a.append(TXNID)
####################################################################
        print("\n\nPASSENGER DETAILS\n")
        print("1.Enter passenger details")
        print("2.Go back")
        option = int(input("\nEnter your option : "))
        
        if option == 2:
            function_bus_type()
            return 0
        elif option == 1:
        		people = int(input("\nRe-confirm number of passengers: "))
        		name_l = []
        		age_l = []
        		sex_l = []
        		for p in range(people):
        			name = str(input("\nName : "))
        			name_l.append(name)
        			age  = int(input("\nAge  : "))
        			age_l.append(age)
        			sex  = str(input("\nMale or Female : "))
        			sex_l.append(sex)
        
        		restart = str(input("\nshould we proceed ahead? Y/N : "))
        		if restart in ('n','NO','no','No'):
        			restart = ('N')
        		else :
        			x = 0
        			print("\nTotal Ticket : ",people)
        			for p in range(1,people+1):
        				print("Ticket : ",p)
        				print("Name : ", name_l[x])
        				print("Age  : ", age_l[x])
        				print("Sex : ",sex_l[x])
        				x += 1

####################################################################
        print("PLEASE SELECT YOUR PAYMENT METHOD")
        print("\n")
        print("1. Credit/Debit Card")
        print("2. UPI Payment")
        print("3. Cash")
        print("4. Back to previous menu")         

#######################################

        payment = int(input("Choose your payment method: "))
        if payment == 4:
            function_bus_type()
            return 0 
        elif payment == 1:
            final_payment = final_fare * 1.02 
            print("Your final payment of card for TXN ID {} is {}".format(TXNID,final_payment))
            print("\n")
            print("Your order of ID {} for {} tickets will be emailed within 1 hour ".format(TXNID, seats))
            print("\n")
            main_bus_menu()
            return 0 
            ################################################
        elif payment == 2:
            final_payment = final_fare * 1.01 
            print("Your final payment of card for TXN ID {} is {}".format(TXNID,final_payment))
            print("\n")
            print("Your order of ID {} for {} tickets will be emailed within 1 hour ".format(TXNID, seats))
            print("\n")
            main_bus_menu()
            return 0 
        elif payment == 3:
            final_payment = final_fare * 1
            print("Your final payment of card for TXN ID {} is {}".format(TXNID,final_payment))
            print("\n")
            print("Your order of ID {} for {} tickets will be emailed within 1 hour ".format(TXNID, seats))
            print("\n")
            main_bus_menu()
            return 0 
        else:
            print("incorrect choice")
            function_bus_type()
###################################################################################################
def bus4():
    x = random.randint(100200, 900200)
    TXNID = str(x)
    y = random.randint(600, 750)
    fare = int(y)
    print("SELECT NUMBER OF SEATS")
    print("\n ")
    seats = int(input("Enter number of seats required: "))
    if seats > 10:
        print("Maximum seat capacity is 10, please select a different date")
        date_func()
        bus4()
    else:
        print("You have selected {} seats".format(seats))
        print("\n")
        print("Your Transaction ID is {}".format(TXNID))
        print("\n")
        final_fare = seats * fare
        print("Your final fare for {} seats booking would be {} rupees".format(seats, final_fare))
        print("\n")
        if TXNID not in a:
            a.append(TXNID)
        if seats not in a:
             a.append(seats)
####################################################################
        print("\n\nPASSENGER DETAILS\n")
        print("1.Enter passenger details")
        print("2.Go back")
        option = int(input("\nEnter your option : "))
        
        if option == 2:
            function_bus_type()
            return 0
        elif option == 1:
        		people = int(input("\nRe-confirm number of passengers: "))
        		name_l = []
        		age_l = []
        		sex_l = []
        		for p in range(people):
        			name = str(input("\nName : "))
        			name_l.append(name)
        			age  = int(input("\nAge  : "))
        			age_l.append(age)
        			sex  = str(input("\nMale or Female : "))
        			sex_l.append(sex)
        
        		restart = str(input("\nshould we proceed ahead? Y/N : "))
        		if restart in ('n','NO','no','No'):
        			restart = ('N')
        		else :
        			x = 0
        			print("\nTotal Ticket : ",people)
        			for p in range(1,people+1):
        				print("Ticket : ",p)
        				print("Name : ", name_l[x])
        				print("Age  : ", age_l[x])
        				print("Sex : ",sex_l[x])
        				x += 1

####################################################################
        print("PLEASE SELECT YOUR PAYMENT METHOD")
        print("\n")
        print("1. Credit/Debit Card")
        print("2. UPI Payment")
        print("3. Cash")
        print("4. Back to previous menu")         

#############

        payment = int(input("Choose your payment method: "))
        if payment == 4:
            function_bus_type()
            return 0 
        elif payment == 1:
            final_payment = final_fare * 1.02 
            print("Your final payment of card for TXN ID {} is {}".format(TXNID,final_payment))
            print("\n")
            print("Your order of ID {} for {} tickets will be emailed within 1 hour ".format(TXNID, seats))
            print("\n")
            main_bus_menu()
            return 0 
            ################################################
        elif payment == 2:
            final_payment = final_fare * 1.01 
            print("Your final payment of card for TXN ID {} is {}".format(TXNID,final_payment))
            print("\n")
            print("Your order of ID {} for {} tickets will be emailed within 1 hour ".format(TXNID, seats))
            print("\n")
            main_bus_menu()
            return 0 
        elif payment == 3:
            final_payment = final_fare * 1
            print("Your final payment of card for TXN ID {} is {}".format(TXNID,final_payment))
            print("\n")
            print("Your order of ID {} for {} tickets will be emailed within 1 hour ".format(TXNID, seats))
            print("\n")
            main_bus_menu()
            return 0 
        else:
            print("incorrect choice")
            function_bus_type()


def function_bus_type():
    print("BUS TYPE")
    print("1. Volvo AC sleeper")
    print("2. Volvo AC seater")
    print("3. Volvo Non-AC sleeper")
    print("4. Volvo Non-AC seater")
    print("5. Go back to main menu")
    bus_type = int(input("Select your bus: "))
    if bus_type not in a:
        a.append(bus_type)
    if bus_type == 5:
        main_bus_menu()
        return 0
    elif bus_type == 1:
        bus1()
    elif bus_type == 2:
        bus2()
    elif bus_type == 3:
        bus3()
    elif bus_type == 4:
        bus4()
    else: 
        print("invalid choice")
        function_bus_type()
    

#datefunction

def date_func():
        travelday=input("What is your date of journey? (in DD/MM/YYYY) ")  
        traveldate=datetime.datetime.strptime(travelday,"%d/%m/%Y").date()
        if traveldate >= date.today():
            print("Your date of journey is : "+traveldate.strftime('%d/%B/%Y'))
            print("Available ticket capacity is 10 per bus")
            if traveldate not in a:
                a.append(traveldate)
            
        else:
            print("Invalid Date, please select different date")
            date_func()
#Menu print


def main_bus_menu():
    print("Destination Selection")
    print("\n ")
    print("1. Panji,Goa")
    print("2. Chennai")
    print("3. Tirupati")
    print("4. Hyderabad")
    print("5. Mumbai")
    print("6. Go back to main menu")
    end_point = int(input("Where do you want to go:"))
    if end_point not in a:
        a.append(end_point)
    if end_point == 6:
        start_point()
    if end_point == 1:
        date_func()
        function_bus_type()
    elif end_point == 2:
        date_func()
        function_bus_type()
    elif end_point == 3:
        date_func()
        function_bus_type()
    elif end_point == 4:
        date_func()
        function_bus_type()
    elif end_point == 5:
        date_func()
        function_bus_type()
    else:
        print("Invalid choice, please input from 1 to 5")
        start_point()
    
#####################################################
# selection of start point

def start_point():
    print("Start point from Bengaluru")
    print("\n ")
    print("1. Majestic")
    print("2. Jayanagar")
    print("3. Whitefield")
    print("4. Banashankari")
    print("5. Kormangala")
    starting_point = int(input("Where is your boarding point: "))
    if starting_point not in a:
        a.append(starting_point)
    if starting_point == 1:
         main_bus_menu()
    elif starting_point == 2:
        main_bus_menu()
    elif starting_point == 3:
        main_bus_menu()
    elif starting_point == 4:
        main_bus_menu()
    elif starting_point == 5:
        main_bus_menu()

start_point()
print(a)


##############################################################


    
        
    

