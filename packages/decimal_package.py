# Python handles floating point numbers strangely
# to correct for this, we can use the Decimal package

from decimal import Decimal

cost_of_gum = 0.10
cost_of_gumdrop = 0.35

cost_of_transaction = cost_of_gum + cost_of_gumdrop
print(cost_of_transaction)
# returns 0.44999999999999996

# We can reassign the variables:

cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumdrop
print(cost_of_transaction)
# Returns 0.45

# Decimal can be used when adding floating point numbers:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)
