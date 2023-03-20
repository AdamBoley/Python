# We can use the unpacking operators in our function calls as well
# This is useful in cases where the function accepts a certain number of arguments, and we want to map the elements of a list or dictionary to those arguments

# We'll demonstrate using a function that calculates how much each member of a party must pay, including the tip:

def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)


# We define a list containing the price, tip percentage and the number of people to split by
table_7_total = [534.50, 20.0, 5]

# We can now pass variable into the function using the unpacking operator to map each element of the list to a positional argument
calculate_price_per_person(*table_7_total)

# We can do the same with the keywords unpacking operator and a dictionary:
table_8_total = {
    'total': 678.30,
    'tip': 17.5,
    'split': 4
}

calculate_price_per_person(**table_8_total)

# We can also combine packing and unpacking into one application:
num_collection = [3, 6, 9]
# Define a list of numbers


def power_two(*nums):
    # unpack the list
    for num in nums:
        print(num**2)


# pack the list up to be passed to the function
power_two(*num_collection)
