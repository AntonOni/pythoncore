list_of_numbers = [101, 89, 98, 78, -1, 1]

#1
def max_number(list_of_numbers):
    max_number = max(list_of_numbers)
    return max_number

print(max_number(list_of_numbers))

#2
def min_number(list_of_numbers):
    min_number = min(list_of_numbers)
    return min_number

#3
print(min_number(list_of_numbers))

def summa_elim(list_of_numbers):
    summa = sum(list_of_numbers)
    return summa

print(summa_elim(list_of_numbers))

#4
def srednee_arifmetic(list_of_numbers):
    srednee = sum(list_of_numbers) / len(list_of_numbers)
    return srednee

print(srednee_arifmetic(list_of_numbers))

#5
def srednee_min_max_func(list_of_numbers):
    srednee_min_max_celoe = (list_of_numbers[0] + list_of_numbers[-1]) / 2
    srednee_min_max_ostatok = (list_of_numbers[0] + list_of_numbers[-1]) % 2
    srednee_min_max = srednee_min_max_celoe + srednee_min_max_ostatok
    return srednee_min_max

print(srednee_min_max_func(list_of_numbers))

another_list = [100, 200, 300, -50, 70]

def maximum_another_list(another_list):
    counter = range(another_list)

    for i in another_list:

        return counter
print (maximum_another_list(another_list))