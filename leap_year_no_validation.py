# Leap Year program
# Khai Phan
# 933-290-231
# CS 362 Spring Term 2021

# Determine if year entered is a leap year
# Year entered must be integer (assumed to be integer input)
def main():

    # Get user input for the year
    year_input = input("Enter a year: ")
    year = int(year_input)

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