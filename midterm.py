










string = "not mutable"

# lets try to change string
    string[0] = 'I'
except TypeError as e:
    print("TypeError:", e)

# Concatenate a new string to the existing one
new_string = string + " strings"

# Print the original and new strings
print("Original string:", string)
print("New string:", new_string)