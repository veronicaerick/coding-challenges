# Given a list_of_ints, find the highest_product you can get from three of the integers.

def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception 

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]

    highest_product_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for current in list_of_ints[2:]:

        # do we have a new highest product of 3?
        highest_product_of_three = max(
            highest_product_of_three,
            current * highest_product_of_2,
            current * lowest_product_of_2
            )
        
        highest_product_of_2 = max(
            highest_product_of_2,
            current*highest,
            current*lowest)

        lowest_product_of_2 = min(
            lowest_product_of_2,
            current*highest,
            current*lowest)

        highest = max(lowest, current)
        lowest = min(lowest, current)

    return highest_product_of_three


