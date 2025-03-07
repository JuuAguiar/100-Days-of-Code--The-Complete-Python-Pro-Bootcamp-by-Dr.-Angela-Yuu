print("Welcome to the tip calculator!\n") #Title
bill = float(input("What was the total bill? $\n")) #Introduce the total value of the bill by the input function
tip = int(input("What percentage tip would you like to give? 10 12 15\n ")) #When answered with the input function decides which will be the percent of the tip
people = int(input("How many people to split the bill?\n ")) # With the input function it will be decided on how many people the bill will be split
tip_as_percent = tip / 100 # Variable responsible for making the tip's percent
total_tip_amount = bill * tip_as_percent # Variable that defines the final value of the tip
total_bill = bill + total_tip_amount # Variable that defines the final value of the inicial bill
bill_per_person = total_bill / people # Variable that defines the value of the bill per person after the total amount was split
final_amount = round(bill_per_person) # Variable that will define the value each person will have to pay
print(f"Each person should pay: $ {final_amount}") #Final part of the code which will show the amount each person will have to pay
