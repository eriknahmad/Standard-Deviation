# Project Name: Standard Deviation
# File Name: StandardDeviation.py
# Author: Erik Nahmad
# Date: March 29 2021
# Purpose: To simplify doing Standard Deviation tables with data sets of over 20

import math

dataSet = []  # Initialize Data Set

while True:  # Allow user input until condition is met
  userInput = str(input("Enter a Number: "))  # Store input as str
  if userInput == "": break  # If input is empty then break
  else: dataSet.append(int(userInput))  # Otherwise add number to data set
print("\n")

summation = 0  # Sum of Squares or the Numerator
n = len(dataSet)  # Length of the data set
mean = sum(dataSet)/n  # Mean of the data set

for x in dataSet:  # For each item in data set
  middleValues = x - mean  # Subtract X by the Mean
  finalValues = middleValues**2  # Square the results
  summation += finalValues  # Sum the squared values 
  print(f"{x}   |    {middleValues}     |    {finalValues}")
print("\n") 

variance = (summation) / (n-1)
SD = math.sqrt(variance)

print("n:", n)
print("Sum:", summation)
print("Mean:", (mean))
print("Variance:", variance)
print("SD:", SD, "or", round(SD, 2))
