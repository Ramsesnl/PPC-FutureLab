import math


def calculate_distance(x1, y1, x2, y2):
    """"This method calculates te distance between two points"""

    dx = x2 - x1
    dy = y2 - y1
    result = math.sqrt(dx ** 2 + dy ** 2)  # macht 2
    return result

# print(calculate_distance(0, 0, 3, 4, ))  # result is 5, the famous 3, 4, 5, triangle
# print(calculate_distance(0, 0, 6, 8, ))  # result is 10, the famous 6, 8, 10, triangle
# print(calculate_distance(1, 10, 6, 22, ))  # result is 13, the famous 5, 12, 13, triangle

# divide_by = int(input("delen door? : "))
# result = 0
# try:
#     result = 15 / divide_by
# except Exception as e:
#     print("Something is wrong with your calculation. Reverting to the default result: \n")
#     print("Default is: " + str(15 / 2))
#     print (e)
# finally:
#     print(result)




# def calculate_lengte_schuine(L1, L2):
#     """"This method calculates te distance between two points"""
#
#
#
#     result2 = math.sqrt(L1 ** 2 + L2 ** 2)  # macht 2
#     return result2
#
#
#
#     L1 = int(input("lengte been 1 : "))
#     L2 = int(input("lengte been 2 : "))
#
# print(calculate_lengte_schuine(L1, L2))

# T1 = "Hello World!\n"
# T2 = "Vialis is hier @ the FutureLab"
#
# A = 5
# print (A, T1, T2)

# A = 5
# print (A)
# A += 3
# print(A)
#
# b = 5
# print (A + b)


# a = int(input("How much?\n : "))
#
#
# if (a >= 2):
#     print ("Wow that's nice!")
# elif (a < 2 and a >= 0):
#     print ("better improve on it")
# else:
#     print ("oh whatever")


# a = int(input("How much? :"))
# while a > 10:
#     a -= 1 # elke keer weer a - 1
#     print(a)
#
# print("Good job! End result: " + str(a))


# for i in range (0, 101):
#     print("teller is: " + str (i))
#
#
# for i in range (1, 101, 2):
#     print("teller is: " + str (i))

# fruit = ["pear", "banana", "cherry", "orange"]
# for x in fruit:
#     if x == "cherry":
#         break
#     # print (x)
#     if x == "pear":
#         continue
#     print(x)

fruit = ["pear", "banana", "cherry", "orange"]
print(fruit)

fruit.append("seafruit")
fruit.insert(3, "guava")# ook hier geld 0 is 1
fruit.remove



print(fruit)
