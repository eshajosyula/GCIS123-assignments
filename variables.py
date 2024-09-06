def variable_practice():
    age_in_months = 300 # age in months, integer
    days_in_year = 365 # number of days in a year, integer
    name_of_first_pet = "Opal" # name of first pet, string
    first_five_digs_pi = 3.1415 # first 5 digits  of pi, float

    print(age_in_months , days_in_year , name_of_first_pet , first_five_digs_pi)

def prompt_and_print():
    num1 = float(input("Chose one number: "))
    num2 = float(input("Choose another number: "))
    added = num1 + num2
    subbed = num1 - num2
    mult = num1 * num2
    divd = num1 / num2

    print(num1, " + ", num2, " = ", added) 
    print(num1, " - ", num2, " = ", subbed)
    print(num1, " * ", num2, " = ", mult)
    print(num1, "/", num2, " = ", divd )
    

prompt_and_print()