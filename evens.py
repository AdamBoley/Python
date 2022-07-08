def even_number_of_evens(list_of_numbers):
    """
    Required tests:
    Raise TypeError if anything other than a List is passed in to the function
    If list_of_numbers is empty, return False
    If the number of even numbers is odd, return False
    If the number of even numbers is 0, return False
    If the number of even numbers is even, return True
    """

    if isinstance(list_of_numbers, list):  # isistance is a method that checks if a parameter or variable is a particular data type
        if list_of_numbers == []:  # this code will pass the second test that checks if list_of_numbers is an empty list
            return False
        else:
            number_of_evens = 0
            # The code below could also work:
            # evens = sum([1 for n in numbers if n % 2 == 0])
            # If using this, eliminate the for loop as well, since this a List Comprehension, which incorporates a for loop

        for number in list_of_numbers:
            if number % 2 == 0:
                number_of_evens += 1

        # return number_of_evens % 2 == 0  # returns True if the number of evens is even and False if number of evens is odd.
        # This is the code from the walkthrough, but it is somewhat confusing to me, so I prefer my code below, which is more verbose, but clearer to me
        if number_of_evens:
            if number_of_evens % 2 == 0:
                return True
            else:
                return False
        else:
            return False
        # the if number_of_evens statement on line 23 is a Truthy Falsy check. If number_of_evens > 0, then it will return true, and if number_of_evens = 0, it will return false
        # My approach would be to initialise a variable called number_of_odds, and then co-opt the for loop to increment that variable if number if odd
        # Then add another term to the conditional check if number_of_evens % 2 == 0 line to check the value of number_of_odds as well, and return True only if both terms pass
        # The above approach could also be refactored into:
        # return True if evens and evens % 2 == 0 else False

    else:
        raise TypeError("A list was not passed into the function")




if __name__ == '__main__':
    print(even_number_of_evens(5))
