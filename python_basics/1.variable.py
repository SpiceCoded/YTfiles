# ================================
# Solutions for Python Variables Exercises
# ================================

# --------------------------------
# Exercise 1: Swap Without Temp Variable
# --------------------------------
a = 'bob
b = 'john'

# Swap without temp
a, b = b, a
print("Exercise 1 -> a =", a, "b =", b)


# --------------------------------
# Exercise 2: Track a Running Total
# --------------------------------
total = 0
for i in range(3):
    num = int(input(f"Enter number {i+1}: "))
    total += num
print("Exercise 2 -> Final total is", total)


# --------------------------------
# Exercise 3: Dynamic Typing Twist
# --------------------------------
data = 42
print("Exercise 3 ->", data, type(data))

data = "Hello, Python!"
print("Exercise 3 ->", data, type(data))

data = [1, 2, 3]
print("Exercise 3 ->", data, type(data))


# --------------------------------
# Exercise 4: Simple Banking System
# --------------------------------
balance = 1000

# Deposit 250
balance += 250
print("Exercise 4 -> Balance after deposit 250:", balance)

# Withdraw 400 (check balance)
if balance - 400 >= 0:
    balance -= 400
print("Exercise 4 -> Balance after withdraw 400:", balance)

# Deposit 120
balance += 120
print("Exercise 4 -> Balance after deposit 120:", balance)


# --------------------------------
# Exercise 5: Variable Value Tracing (Challenge)
# --------------------------------
x = 5
y = x + 3
x = y - 2
y = x * 2
x = x + y
print("Exercise 5 ->", x, y)
