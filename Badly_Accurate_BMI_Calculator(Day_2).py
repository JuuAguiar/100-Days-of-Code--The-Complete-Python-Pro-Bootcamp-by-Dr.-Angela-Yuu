print("Welcome to your badly accurate BMI calculator!!!") # Name/Title
weight = float(input("What is your weight?\n")) # The valor of the variable "weight" is introduced with the input function
height = float(input("What is your height? Remember to use '.'\nExample: 1.69\n")) # The valor of the variable "height" is introduced with the input function
BMI = weight/(height ** 2) # Calculation
print("Your BMI is: " + str(round(BMI))) # Will print the final rounded answer