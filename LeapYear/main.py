# Leap Year
# Function that return true or false if a given year is a leap year


def is_leap(year):
	return not year % 4 and (year % 100 or not year % 400)


a = is_leap(2400)
print(a)
