# allow us to take a certain number and raise it to a specific power

# taking in 2 paramenters.Base number and what we are raising it by
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
        


print(raise_to_power(2, 3))