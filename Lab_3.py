# Task1
# N = int(input("Enter a positive integer: "))
# i = 1
# while i <= N:
#     print(i)
#     i += 2

# здесь эта строка кода предлагает N = int(input("Введите положительное целое число: ")) пользователю ввести положительное целое число. Он использует функцию input() для приема пользовательского ввода, который представляет собой строку, а затем преобразует его в целое число с помощью int(). Результат сохраняется в переменной N.

# i = 1: эта строка инициализирует переменную i со значением 1. Эта переменная будет использоваться для перебора нечетных чисел.

# while i <= N:-Это цикл while будет продолжать выполняться до тех пор, пока значение i меньше или равно значению N.

# print(i)- внутри цикла строка печатает текущее значение i. Поскольку i инициализируется значением 1 и увеличивается на 2 на каждой итерации, он будет печатать все нечетные числа.

# i += 2 - после печати текущего значения i эта строка увеличивает значение i на 2. Этот шаг гарантирует, что i обновится до следующего нечетного числа для следующей итерации.

# Цикл будет продолжаться до тех пор, пока i не станет больше N, после чего он завершится и программа завершит выполнение.


#Task2
# N = int(input("Enter a positive integer: "))
# factorial = 1
# while N > 0:
#     factorial *= N
#     N -= 1
# print("Factorial:", factorial)

# Factorial = 1- Здесь строка инициализирует переменную факториал значением 1

# while N > 0 - Эта строка запускает цикл while, который продолжается до тех пор, пока значение N больше 0.

# факториал *= N-  внутри цикла while эта строка умножает текущее значение факториала на текущее значение N. Именно так вычисляется факториал, поскольку он накапливает произведение всех положительных целых чисел от 1 до N.

# N -= 1- здесь  строка уменьшает значение N на 1 на каждой итерации цикла. Это необходимо для перехода от одного целого числа к следующему меньшему целому при вычислении факториала.

# print("Факториал:", факториал): потом после завершения цикла while (т. е. когда N достигает 0), эта строка печатает вычисленное значение факториала с меткой «Факториал».

#Task3
# while True:
#     number = int(input("Enter a number: "))
#     if number == 42:
#         print("Found 42! Terminating.")
#         break

# while True-  здесь опять строка запускает бесконечный цикл while. Цикл будет продолжаться бесконечно, пока не будет явно завершен с помощью оператора Break.

# Number = int(input("Введите число: ")): внутри цикла эта строка предлагает пользователю ввести число и преобразует введенное значение в целое число, которое сохраняется в переменной number.

# if Number == 42:: Эта строка проверяет, равно ли введенное пользователем значение 42.

# print("Найдено 42! Завершение."): если введенное число 42, эта строка выполняется и печатает сообщение, указывающее, что число 42 было найдено.

# Break: оператор Break используется для выхода из цикла. Когда пользователь вводит 42, программа достигнет этой точки и завершит цикл, завершив программу.

#Task4
# string = input("Enter a string: ")
# count = string.count("a")
# print("Number of 'a's:", count)

# Сначала код запрашивает у пользователя ввод строки с помощью функции input. Пользователь вводит произвольную строку текста.

# Затем программа использует метод .count("a") для подсчета количества букв "a" (маленькая латинская 'a') в введенной строке. Это значение сохраняется в переменной count.

# Наконец, программа выводит сообщение "Number of 'a's:" и значение переменной count, которое представляет собой количество букв "a" в введенной строке.
# string = input("Введите строку: ")-строка предлагает пользователю ввести строку и сохраняет введенные данные в переменной string.
# count = string.count("a")- строка использует метод count для строковой переменной для подсчета количества вхождений буквы "a" во входную строку. Затем счетчик сохраняется в переменной count.
# print("Количество букв "a:", count): Наконец, эта строка печатает количество букв "a" в строке с описательным сообщением.


# Task5
# number = input("Enter a number: ")
# digit_sum = sum(int(digit) for digit in number)
# print("Sum of digits:", digit_sum)

# эта строка Number = input("Введите число: "): предлагает пользователю ввести число (в виде строки) и сохраняет введенную строку в переменной number.

# digit_sum = sum(int(digit) for digit in число): В этой строке выражение генератора используется для перебора каждого символа (цифры) в числовой строке. Для каждой цифры он преобразует ее в целое число, используя int(digit), а затем вычисляет сумму этих целых чисел, используя функцию sum(). Полученная сумма сохраняется в переменной digit_sum.

# print("Сумма цифр:", digit_sum): Наконец, эта строка печатает сумму цифр с описательным сообщением.
# # Task6

# N = int(input("Enter a positive integer: "))
# a, b = 0, 1
# while N > 0:
#     print(a)
#     a, b = b, a + b
#     N -= 1

# здесь (a, b = 0, 1) инициализируются две переменные a и b. a установлено значение 0, а b установлено значение 1. Эти переменные будут использоваться для генерации последовательности Фибоначчи.

# while N > 0:: Эта строка запускает цикл while, который продолжается до тех пор, пока значение N больше 0.

# print(a): внутри цикла эта строка печатает текущее значение a, которое является текущим членом последовательности Фибоначчи.

# a, b = b, a + b: В этой строке обновляются переменные a и b. a устанавливается в значение b, а b устанавливается в сумму предыдущих значений a и b. Это ключевой шаг, который генерирует следующий член последовательности Фибоначчи.

# N -= 1: эта строка уменьшает значение N на 1 на каждой итерации, эффективно подсчитывая количество выводимых терминов.


# #Task7
# string = input("Enter a string: ")
# reverse_string = string[::-1]
# print("Reversed string:", reverse_string)

# Task8
# sum_odd = 0
# while True:
#     number = int(input("Enter a number: "))
#     if number % 2 == 0:
#         continue
#     sum_odd += number
#     print("Sum of odd numbers:", sum_odd)

# Task8
# import random

# target_number = random.randint(1, 100)
# while True:
#     guess = int(input("Guess the number (1-100): "))
#     if guess < target_number:
#         print("Too small")
#     elif guess > target_number:
#         print("Too large")
#     else:
#         print("You guessed it!")
#         break

#     target_number = random.randint(1, 100): эта строка генерирует случайное целое число от 1 до 100 (включительно) и сохраняет его в переменной target_number. Это случайное число и будет числом, которое пользователь должен угадать.

# while True:: Эта строка запускает бесконечный цикл while. Цикл будет продолжаться бесконечно, пока пользователь не угадает правильное число и не выйдет из цикла.

# догадка = int(input("Угадай число (1-100): ")): Внутри цикла эта строка предлагает пользователю ввести свое предположение и преобразует входные данные в целое число, сохраняя его в переменной предположения.

# if догадка < target_number:: Это условие проверяет, меньше ли предположение пользователя, чем target_number. Если это так, он печатает «Слишком маленький».

# elif догадка > целевой_номер:: Это условие проверяет, превышает ли предположение пользователя целевой_номер. Если это так, он печатает «Слишком большой».

# else:: Если догадка пользователя не слишком мала и не слишком велика, это означает, что он угадал правильное число. В этом случае код печатает «Вы догадались!» и выходит из цикла с помощью оператора Break.

# Task9
# string = input("Enter a string: ")
# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


#     X = int(input("Enter the base (X): "))
# Y = int(input("Enter the power (Y): "))
# result = 1
# while Y > 0:
#     result *= X
#     Y -= 1
# print(f"{X} to the power {Y} is {result}")
 
# Первая часть кода проверяет, является ли введенная пользователем строка палиндромом 
# (читается одинаково в прямом и обратном направлении) и печатает «Палиндром» или «Не палиндром» соответственно.
# Вторая часть кода принимает вводимые пользователем данные по основанию (X) и степени (Y) 
# и вычисляет X, возведенный в степень Y, с помощью цикла while и печатает результат.

# Task10
# N = int(input("Enter a positive integer (N): "))
# num = 2
# while num <= N:
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=' ')
#     num += 1

# number = input("Enter a number: ")
# reverse_number = number[::-1]
# print("Reversed number:", reverse_number)
# Пользователю предлагается ввести положительное целое число N.
# Затем код инициализирует переменную num со значением 2 и начинает цикл while, который продолжает выполнение, пока num не превышает введенное число N.
# Для каждого числа num в диапазоне от 2 до корня из num (округленного в большую сторону), код проверяет, является ли число простым, путем попытки деления на числа в этом диапазоне.
# Если число num является простым (не делится ни на одно из чисел в диапазоне), то устанавливается флаг is_prime в True, и число выводится.
# Затем значение num увеличивается на 1 для проверки следующего числа в диапазоне.
# Часть 2: Реверс числа

# Пользователю предлагается ввести число (как строку).
# Затем код реверсирует введенное число, используя срез [::-1].
# Реверсированное число выводится на экран вместе с сообщением "Reversed number".


# Task15
# def caesar_cipher(text, shift):
#     result = ""
#     for char in text:
#         if char.isalpha():
#             is_upper = char.isupper()
#             char = chr(((ord(char) - ord('A' if is_upper else 'a') + shift) % 26) + ord('A' if is_upper else 'a'))
#         result += char
#     return result

# text = input("Enter a string: ")
# shift = int(input("Enter the shift value (N): "))
# encrypted_text = caesar_cipher(text, shift)
# print("Encrypted string:", encrypted_text)

# result = "": Инициализирует пустую строку результата для хранения зашифрованного текста.

# for char in text:: Проходит по каждому символу входного текста.

# if char.isalpha(): проверяет, является ли текущий символ буквенным.

# is_upper = char.isupper(): определяет, находится ли текущий символ в верхнем или нижнем регистре, проверяя, 
# является ли он прописным или строчным регистром.

# char = chr(((ord(char) - ord('A' if is_upper else 'a') + сдвиг) % 26) + ord('A' if is_upper else 'a')): Эта строка вычисляет новый символ после его смещения на позиции сдвига в алфавите, гарантируя, что он переносится, если выходит за пределы «Z» или «z». Он использует функцию ord для получения ASCII-кода символа, применяет сдвиг, принимает модуль 26 для обеспечения переноса, а затем преобразует результат обратно в символ с помощью функции chr.

# result += char: добавляет зашифрованный символ в строку результата.

# Функция возвращает результат — зашифрованный текст.

# text = input("Введите строку: "): предлагает пользователю ввести строку для шифрования.

# сдвиг = int(input("Введите значение сдвига (N): "): предлагает пользователю ввести значение сдвига (N), которое является целым числом.

# зашифрованный_текст = caesar_cipher(текст, сдвиг): вызывает функцию caesar_cipher с предоставленной пользователем строкой и значением сдвига для шифрования текста.

# print("Зашифрованная строка:", Encrypted_text): печатает зашифрованную строку.