# Leap Year program
# Khai Phan
# 933-290-231
# CS 362 Spring Term 2021

# Gets integer input or "intput" as I like to call it
# Loops through the input prompt provided as parameter until user input can be
# converted to integer verifying that it is in fact an integer.
# Handled with try and catch exceptions for invalid inputs that can't
# be converted to integers and so aren't integers.
def get_intput(prompt):

    # Infinite loop until user enters valid integer input
    # Break and return if valid int, print error and loop
    # again to re-prompt otherwise
    while True:
        try:
            intput = int(input(prompt))
            return intput
        except ValueError:
            print("You must enter a valid integer!")


# Determine if year entered is a leap year
def main():

    # Get user input for the year
    year = get_intput("Enter a year: ")

    # Check if divisible by 4
    if year % 4 == 0:

        # Check if divisible by 100
        if year % 100 == 0:

            # Check if divisible by 400
            if year % 400 == 0:

                # It is a leap year
                print(f"{year} is a leap year.")

            else:

                # It is not a leap year
                print(f"{year} is NOT a leap year.")

        else:

            # It is a leap year
            print(f"{year} is a leap year.")

    else:

        # It is not a leap year
        print(f"{year} is NOT a leap year.")


if __name__ == "__main__":
    main()
