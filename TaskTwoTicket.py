import random

def get_numbers_ticket(min: int, max: int, quantity: int):
   if min < 1 or max > 1000:
        return []
   if min > max:
        raise ValueError("=== The minimum value cannot be greater than the maximum ===")
   if quantity > (max - min + 1):
        raise ValueError("=== It is not possible to generate that many unique numbers within the specified range ===")
   
   numbers = random.sample(range(min, max + 1), quantity)
   sorted_numbers = sorted(numbers)

   print(sorted_numbers) 


def run_program():
    try:
        min_val = int(input("Enter a minimum value: "))
        max_val = int(input("Enter the maximum value: "))
        count = int(input("Enter the number of numbers: "))
        
        get_numbers_ticket(min_val, max_val, count)

    except ValueError as e:
        print("Error:", e)

run_program()        