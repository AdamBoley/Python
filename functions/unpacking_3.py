# We can combine *args and **kwargs in a function definition together, provided they are in the format:
# positional arguments, *args, standard keyword arguments, **kwargs
# This looks like:


def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
    print(appetizer)
    print(entrees)
    print(sides)
    print(dessert_scoops)


single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops', sides='Mashed Potatoes', dessert_scoops='Vanilla, Cookies and Cream')
# Note that we order the parameters of the function call in the order defined above