def Leap_year(year):
  if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    return True


def Days_in_a_month(month, year):
  if month == 2 and Leap_year(year):
    return 29
  elif month == 2:
    return 28
  elif ((month -1) % 7) % 2 == 0:
    return 31
  else:
    return 30

def main():
  month = int(input("Enter the month: "))
  year = int(input("Enter the year: "))
  day = Days_in_a_month(month, year)
  print("There are %s days in that month." %day)

main()
