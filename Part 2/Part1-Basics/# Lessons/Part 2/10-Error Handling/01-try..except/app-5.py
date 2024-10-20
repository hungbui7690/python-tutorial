""" """


# It’s a good practice to catch other general errors by placing the catch Exception block at the end of the list:

try:
    # get input net sales
    print("Enter the net sales for")

    previous = float(input("- Prior period:"))
    current = float(input("- Current period:"))

    # calculate the change in percentage
    change = (current - previous) * 100 / previous

    # show the result
    if change > 0:
        result = f"Sales increase {abs(change)}%"
    else:
        result = f"Sales decrease {abs(change)}%"

    print(result)
except ValueError:
    print("Error! Please enter a number for net sales.")
except ZeroDivisionError:
    print("Error! The prior net sales cannot be zero.")
except Exception as error:
    print(error)
