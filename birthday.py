def days_since_birthday():
    """
    Calculate the number of days that have passed since the birthday (excluding the birth year and the current year).
    :return: Number of days passed since the birthday.
    """
    # Get the current date
    import datetime
    current_date = datetime.datetime.now()

    # Ask for birthdate input
    birthday_input = input("Enter your birthday (DD-MM-YYYY): ")
    # Convert the input string to a datetime object
    birthday = datetime.datetime.strptime(birthday_input, "%d-%m-%Y")

    # Get the birth year from the birthday
    birth_year = birthday.year

    # Calculate the total number of years between the birth year and the current year (excluding the birth year and current year)
    total_years = current_date.year - birth_year - 1

    # Calculate the total number of days passed (excluding the days in the birth year and the current year)
    days_passed = total_years*365

    return days_passed

# Example usage:
print("Days passed since birthday:", days_since_birthday())