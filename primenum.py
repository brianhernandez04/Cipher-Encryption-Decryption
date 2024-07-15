# Write your code below this line 👇
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def prime_checker(number):
    if number in prime_list:
      print("It's a prime number.")
    else:
      print("It's not a prime number.")

# Write your code above this line 👆
user = int(input("Input a number between 1 - 100: "))
#Do NOT change any of the code below👇
n = user # Check this number
prime_checker(number=n)