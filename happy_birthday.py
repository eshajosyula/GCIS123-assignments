def happy_birthday():
    name = input("your name: ")
    month = input("birth month: ")
    day = input("day of your birth: ")
    year = input("birth year: ")

    print(name, ", your birthday is on", month, day, ",", year)


def happy_birthday2(name, month, day, year):
    print(name, ", your birthday is on", month, day, ",", year)


#happy_birthday2("esha","october","22","2006")
    
def main():
    happy_birthday2("Esha", "October", 22, 2006)
    happy_birthday2("Alex", "June", 27, 2006)
    happy_birthday2("Nate", "September", 13, 2005)

main()

