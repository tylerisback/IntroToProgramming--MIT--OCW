#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 04:55:08 2021

@author: emreuzel
"""

#Part A
#
#annual_salary = float(input('Enter your annual salary: '))
#portion_saved = float(input('Enter the portion saved: '))
#total_cost = float(input('Indicate total cost of your house: '))
#semi_annual_raise = float(input('Semi Annual Raise: '))
#
#portion_down_payment =  0.25
#current_savings = 0
#num_of_months = 0
#r = 0.04
#
#while current_savings < (total_cost * portion_down_payment):
#    current_savings += annual_salary * (portion_saved /12)
#    current_savings += current_savings * (r/12)
#    num_of_months += 1
#
#
#print('Required Number of Months: ', num_of_months)
#
## Part B
#
#annual_salary = float(input('Enter your annual salary: '))
#portion_saved = float(input('Enter the portion saved: '))
#total_cost = float(input('Indicate total cost of your house: '))
#semi_annual_raise = float(input('Semi Annual Raise: '))
#
#portion_down_payment =  0.25
#current_savings = 0
#num_of_months = 0
#r = 0.04
#
#while current_savings < (total_cost * portion_down_payment):
#    current_savings += annual_salary * (portion_saved /12)
#    current_savings += current_savings * (r/12)
#    num_of_months += 1
#    if num_of_months % 6 == 0:
#        annual_salary = annual_salary * (1 + semi_annual_raise)
#
#
#print('Required Number of Months: ', num_of_months)


# Part C

annual_salary = float(input('Enter your annual salary: '))

epsilon= 1

total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment =  0.25
current_savings = 0
num_of_months = 36
r = 0.04
num_of_iter = 0

port_min = 0.0
port_max = 0.5



while abs(current_savings - (total_cost * portion_down_payment)) >= epsilon:
    current_savings = 0
    
    
    
    port_real = (port_max + port_min) / 2
    annual_sal = annual_salary
    for i in range(1,num_of_months+1):
        current_savings += annual_sal * (port_real /12)
        current_savings += current_savings * (r/12)
        if i % 6 == 0:
            annual_sal = annual_sal * (1 + semi_annual_raise)
        
    
    if current_savings < (total_cost * portion_down_payment):
        port_min = port_real
    else:
        port_max = port_real 
    
    if port_min == 0.5:
        print('It is not possible to pay the down payment in three years')
        break
        
        
    
    num_of_iter += 1
    
    
    
if port_min != 0.5:
    print('Best Savings Rate: ', port_real)
    print('Steps in bisection search = ', num_of_iter)


























