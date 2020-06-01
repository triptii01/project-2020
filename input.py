input_year = int(input("enter te year:"))
input_month = int(input("enter the month:"))
input_date = int(input("enter the date:"))

number_of_days = 0

if input_year % 4 == 0:
        number_of_days = number_of_days + 366
else:
        number_of_days = number_of_days + 365


months = {'january':31, 'february':28, 'march':31, 'april':30, 'may':30, 'june':30, 'july':31, 'august':31, 'september':30, 'october':31, 'november':30, 'december':31}

if input_month == month.keys:
         
