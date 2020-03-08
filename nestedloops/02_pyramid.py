# ##1
# print("#", end="")
# print("#", end="")
# print("#", end="")
# print("#", end="")

# ## 2
# for j in range(5):
#     print("#", end="")
# print(" ")

# for j in range(5):
#     print("#", end="")
# print(" ")

# for j in range(5):
#     print("#", end="")
# print(" ")

for i in range(5):  # i = rows
    for j in range(5):  # j = colums
        print("#", end="")
    print(" ")


for i in range(5):  # i = rows
    for j in range(i):  # j = colums
        print("#", end="")
    print(" ")
