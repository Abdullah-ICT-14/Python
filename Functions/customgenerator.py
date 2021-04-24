"""
Program to use generators
"""
def custom_gen(initial_value,final_value):
    """
    Generators examples
    """
    while initial_value<final_value:
        yield initial_value
        initial_value+=1

result = custom_gen(10, 18)

for i in result:
    print(i)
