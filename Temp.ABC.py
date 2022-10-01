# # Identify A, B, C values and assign ascending order to A, B, C
#
# A = int(input("Input value A:"))
# B = int(input("Input value B:"))
# C = int(input("Input value C:"))
#
# if (A < B):
#     if (B < C):
#         print("Ascending order ABC")
#     else:
#         if (A < C):
#             print("Swap B with C")
#         else:
#             print("Swap A with C")
#             print("Swap B with C")
# else:
#     if (A< C):
#         print("Swap A with B")
#     else:
#         if (B > C):
#             print("Swap A with C")
#         else:
#             print("Swap A with B")
#             print("Swap B with C")



# 2. Identify A, B, C values and assign ascending order to A, B, C

A = int(input("Input value A:"))
B = int(input("Input value B:"))
C = int(input("Input value C:"))

if (A < B):
    if (B < C):
        print("Ascending order ABC")
    elif (A < C):
        print("Swap B with C")
    else:
        print("Swap A with C")
        print("Swap B with C")
else:
    if (A< C):
        print("Swap A with B")
    elif (B > C):
        print("Swap A with C")
    else:
        print("Swap A with B")
        print("Swap B with C")














