#3_loops.py

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for var1 in range(0, 5, 2):
for var1 in range(0, 5):
    print(var1)

# for var2 in num_list[0:5:2]:
for var2 in num_list[0:5]:
    print(var2)

var3 = 0
while var3 < 5:
    print(var3)
    var3 = var3 + 1
    # var3 = var3 + 2
