from os import *

def input_n():
n = input('Введите путь к папке: ')
if path.isdir(n) == True:
return dictionary(n)
else:
return input_n()

def dictionary(n):
result = {}
for i in listdir(n):
if path.isdir(n + "\\" + i):
result.update(dictionary(n + "\\" + i))
elif path.isfile(n + '\\' + i):
result[n + "\\" + i] = path.getsize(n + "\\" + i)
return result

def duplicate(a: dict):
duplicate_2(input_n())

def duplicate_2(result):
for key, val in result.items():
print(val)
for i in key:
print(key)
print()

if __name__ == '__main__dqwjbjdbjqwjd':
duplicate_2(input_n())
