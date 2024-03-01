import re

#making a function
def find_pattern(text):
    """
    Find all occurrences of a pattern that starts with "C" ends with "jeb" in text.
    :param text:
    :return: matches found.
    """
    #define the pattern we look for, as long as there is a character between C and jeb.
    pattern = r'C\w+jeb'  # Regular expression pattern

    #make the length of matches the same as number of ocurrences
    matches = re.findall(pattern, text)
    return len(matches)

#Attempt:
text = "There was a BIE Cstudentjeb who really wanted to Cpassjeb programing."
print("Number of occurrences:", find_pattern(text))