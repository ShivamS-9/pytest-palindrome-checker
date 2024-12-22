def check_pali_day(day, month, year):
    day_str = "{:02}".format(day)
    month_str = "{:02}".format(month)
    year_str = str(year)
    date_str = day_str + month_str + year_str
    return date_str == date_str[::-1]


def pali_day_iterate(year):
    if not isinstance(year, int) or year < 1:
        raise ValueError("Year must be a positive integer greater than 0")

    pali_days = []
    for month in range(1, 13):
        if month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                days_in_month = 29
            else:
                days_in_month = 28
        elif month in {4, 6, 9, 11}:
            days_in_month = 30
        else:
            days_in_month = 31

        for day in range(1, days_in_month + 1):
            if check_pali_day(day, month, year):
                pali_days.append(f"{day:02d}-{month:02d}-{year}")

    if pali_days:
        print("Palindrome days in", year, "are:")
        for day in pali_days:
            print(day)
    else:
        print("No Palindrome days available in the given year", year)
    return pali_days

if __name__ == "pali_day_iterate":
    year = input("Enter year: ")
    try:
        int_year = int(year)
        pali_day_iterate(year)
    except ValueError as e:
        print("Invalid input:", e)