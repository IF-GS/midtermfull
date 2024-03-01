# Define string
string = "immutable"

# Try to change a characters
try:
    string[0] = 'I'
except TypeError as e:
    print("TypeError:", e)

dis_list = [1, 2, 3, 4, 5]
print(dis_list)
dis_list = [3, 4, 5, 6]
print(dis_list)
