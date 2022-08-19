age = input("Введите возраст")

def main(age):
  
    if 2<=age<=6:
      return "Ходит в детский сад"

    elif 7<=age<=17:
      return "Ходит в школу"

    elif 18<=age<=60:
      return "Работает"

print(main(6))
print(main(12))
print(main(26))
