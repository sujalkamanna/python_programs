import random

alphabets_capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alphabets_lower = "abcdefghijklmnopqrstuvwxyz"

numbers = "123456789"

symbols = " !#$%&'()*+,-./:;<=>?@[]^_`{|}~"

password = alphabets_capital + alphabets_lower + numbers + symbols

length = int(input("Enter length of password:"))

password = "".join(random.sample(password, length))

print(password)