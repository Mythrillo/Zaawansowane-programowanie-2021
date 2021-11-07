
# Zadanie 2 a
def print_names(list_of_names: list):
    for name in list_of_names:
        print(name)


# Zadanie 2 b
def multiply_list_elements1(list_of_numbers: list):
    for i in range(len(list_of_numbers)):
        list_of_numbers[i] = list_of_numbers[i] * 2
    return list_of_numbers


def multiply_list_elements2(list_of_numbers: list):
    return [number * 2 for number in list_of_numbers]


# Zadanie 3
def print_only_even(list_of_numbers: list):
    for number in list_of_numbers:
        if number % 2 == 0:
            print(number)


# Zadanie 4
def print_every_other(list_of_numbers: list):
    for i in range(0, len(list_of_numbers), 2):
        print(list_of_numbers[i])


if __name__ == "__main__":
    print_names(["Mikołaj", "Tomasz", "Karol", "Marcin", "Adam"])
    print(multiply_list_elements1([1, 2, 3, 4, 5]))
    print(multiply_list_elements2([1, 2, 3, 4, 5]))
    print_only_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
