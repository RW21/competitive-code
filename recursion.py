# Recursion timetrial

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_presents_recursively(houses):
    if len(houses) == 1:
        print('Delivering to ', houses[0])
    else:
        first_half = houses[:len(houses)//2]
        second_half = houses[len(houses)//2:]
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_recursive(accumulated_sum=0, current_number=0):
    """
    Calculate  1 + 2 + 3 ⋅⋅⋅⋅ + 10 
    """
    if current_number == 10:
        return accumulated_sum
    else:
        current_number+=1
        accumulated_sum += current_number
        return sum_recursive(accumulated_sum=accumulated_sum, current_number=current_number)

# Recursice data structure

def attach_head(element, input_list):
    return [element] + input_list

