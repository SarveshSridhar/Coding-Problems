from math import floor
import math

n = int(input())
input_objects = str(input())
input_emotion = str(input())

def extract_object_and_its_numbers(input_objects):
    physical_obj = []
    num_objs = []
    for obj in input_objects.split():
        num = ''
        thing = ''
        for i in range(len(obj)):
            if obj[i].isdigit():
                num += obj[i]
            else:
                thing += obj[i]
        # print(num, thing)
        physical_obj.append(thing.lower())
        num_objs.append(int(num))
    # print(physical_obj, num_objs)
    return physical_obj, num_objs

def extract_emotions_numbers(input_emotion):
    count = []
    reference = {'happy':10,'sad':5, 'neutral':2, 'none':1}
    for emotion in input_emotion.split():
        word = emotion.lower()
        number = reference[word]
        count.append(number)
    return count

def find_score_of_element(num_of_objects,emotion_score):
    score = 0
    LENGTH = len(num_of_objects)
    for i in range(LENGTH):
        score += num_of_objects[i]*emotion_score[i]
    # print(score)
    return score

def find_number_of_vowels(num_of_objects, object_names):
    vowels = 0
    i = 0
    # FIND NUMBER OF VOWELS
    for obj in object_names:
        word = obj.lower()
        vowels_in_word = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')
        vowels += vowels_in_word*num_of_objects[i]
        i += 1
        # print(obj,vowels_in_word)
        # print(vowels)
    return vowels

def check_prime(number):
    if number > 1:
        for i in range(2, int(math.sqrt(number))):
            if number%i == 0:
                return False
        return True
    else:
        return False

def numtoword(number,s):
    word = ""
    one = [ "", "one ", "two ", "three ", "four ",
        "five ", "six ", "seven ", "eight ",
        "nine ", "ten ", "eleven ", "twelve ",
        "thirteen ", "fourteen ", "fifteen ",
        "sixteen ", "seventeen ", "eighteen ",
        "nineteen "]
    ten = [ "", "", "twenty ", "thirty ", "forty ",
        "fifty ", "sixty ", "seventy ", "eighty ",
        "ninety "]
    if number>19:
        word += ten[number//10] + one[number%10]
    else:
        word += one[number%10]
    
    if number:
        word += s

    return word

def convert_number_to_word(number):
    out = ""
    out += numtoword((number//10000000),"crore")
    out += numtoword(((number // 100000) % 100),"lakh ")
    out += numtoword(((number // 1000) % 100),"thousand ")
    out += numtoword(((number // 100) % 10),"hundred ")
    if number>100 and n%100:
        out += "and "
    
    out += numtoword(number%100, "")
    out = out[0].upper() + out[1:]
    return out


def print_output(number,is_prime):
    string = ""
    if is_prime == True:
        string += 'Yes'
    else:
        string += 'No'
    # NUMBER TO WORDS
    string += " "
    string += convert_number_to_word(number)
    return string


num_physical = []
physical = []
emotions = []

# EXTRACT THE DETAILS - OBJECTS, QUANTITY
physical,num_physical = extract_object_and_its_numbers(input_objects)
emotions = extract_emotions_numbers(input_emotion)

# CALCULATE SOE
score_of_element = find_score_of_element(num_physical, emotions)

# FIND NUMBER OF VOWELS IN THE OBJECT NAMES
total_number_of_vowels = find_number_of_vowels(num_physical, physical)

# DIVIDE SOE AND NUMBER OF VOWELS
if score_of_element > total_number_of_vowels:
    soe_divided_vowels = floor(score_of_element / total_number_of_vowels)
else:
    soe_divided_vowels = floor(total_number_of_vowels / score_of_element)

# CHECK IF RESULTANT NUMBER IS PRIME OR NOT
prime_or_not = check_prime(soe_divided_vowels)

# PRINT OUTPUT
output_string = print_output(soe_divided_vowels,prime_or_not)

# print("Physical objects: ",physical)
# print("Number of physical objects: ",num_physical)
# print("Emotions: ",emotions)
# print("Score of element: ",score_of_element)
# print("Number of vowels total: ",total_number_of_vowels)
# print("Divided result: ",soe_divided_vowels)
# print("If divided number is prime or not: ",prime_or_not)
# print("Output string: ",output_string)
print(output_string)
