from functools import reduce

#1
def sum_list(num_list):
    total = 0
    for number in num_list:
        total = total + number
    return total


#2
def remove_duplicates(input_list):
    return list(set(input_list))


#3
def hyphen_string(input_list):
    return '-'.join(sorted(input_list))


#4
def perfect_number(input_number):
    total = 0
    for i in range(1, input_number):
        if input_number % i == 0:
            total = total + i
    return total == input_number


#5
def prime_checker(input_number):
    if input_number <= 2:
        return False
    prime = True
    for i in range(2, input_number):
        if input_number % i == 0:
            prime = False
    return prime


#6
def palindrome(input_string):
    reversed_string = ''.join(reversed(input_string))
    is_palindrome = True
    for i in range(0, len(input_string)):
        if input_string[i] != reversed_string[i]:
            is_palindrome = False
    return is_palindrome


#7
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_list():
    number_list = []
    for i in range(0, 10):
        number_list.append(fibonacci(i))
    return number_list


#8
def product(a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0 and b != 0:
        return b
    elif a != 0 and b == 0:
        return a
    else:
        return a * b


#9
def factorial(n):
    if n < 1:
        return 1
    else:
        return factorial(n - 1) * n


#10
def count_words(input_string):
    stopwords = ["the", "is", "and"]
    text = input_string.split(" ")
    count = len([word for word in text if word not in stopwords])
    return count


def main():
    num_list = [2, 5, 8, 1, 10, 10, 20, 7]

    print(sum_list(num_list))

    print(remove_duplicates(num_list))

    print(hyphen_string("HOALFJENVSZXY"))

    print(perfect_number(496))

#Print prime from 1 - 100
    for i in range(0, 100):
        if prime_checker(i):
            print(i)

    print(palindrome("RACECAR"))

    print(list(map(fibonacci, range(0, 10))))

    print(reduce(product, [10, 0, 5]))

    print(reduce(product, filter(lambda i: i != 0, [5, 10, 0])))

    print(list(map(factorial, range(0, 10))))

    print(count_words("hello world how are you the and is"))


    return

main()


