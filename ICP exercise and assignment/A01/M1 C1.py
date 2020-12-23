#Q: Using the code editor below, write a program that asks the user for their first name and their last name. Next, compute how much the user should leave as a tip at a restaurant for a $150.00 bill. Assume a tip rate of 15%. Then have your program produce the following output (assume the user entered "John Smith" as their full name):
#Welcome to the restaurant John Smith !
#For a bill of $150.00 you should leave 22.5 for your server
#With this tip your total bill will be 172.5



firstname = input ("What is your first name?")
lastname = input ("What is your last name?")
print ("Welcome to the restaurant",firstname,lastname, "!")
bill = input ("How much did you spend?")
tip = int(bill)*0.15
print ("For a bill of $",bill,"you should leave $",tip,"for your server")
total = int(bill) + int(tip)
print ("With this tip your total bill will be $",total)
