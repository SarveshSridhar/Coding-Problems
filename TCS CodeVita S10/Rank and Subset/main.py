n = int(input())
rank_to_find = str(input())
objects = str(input())

# rank_to_find = "abc,dab"
# objects = "abc,dab,bc"

objects = list(objects.split(','))
rank_to_find = list(rank_to_find.split(','))
ref = dict()


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

def find_combination(n,r):
    numerator = factorial(n)
    denominator = factorial(n-r)*factorial(r)
    return numerator//denominator

def find_start_index(t_length, length):
    val = 0
    if length <= t_length:
        for i in range(1,length):
            # print("Here ",find_combination(t_length,i))
            val += find_combination(t_length,i)
    # print("Value: ",val)
    return val

# ENCODING
count = 1
for i in range(n):
    ref[objects[i]] = count
    count += 1
# print("Reference: ",ref)
new_objects = [ref[obj] for obj in objects]
# print("New encoded objects: ",new_objects)

question = [ref[obj] for obj in rank_to_find]
# print("Question: ",question)

# START MAIN
total_length = n
length = len(question)
# total_length = 5
# length = 3
# question = [1,3,5]
start_index = find_start_index(total_length,length)

# print("Total length: ",total_length, "  Length: ",length)
# print("Start index: ",start_index)

# SAMPLE CASE
blank = [i for i in range(1,length+1)]
# print("Blank: ",blank)
# print("Question: ",question)
blank1 = []
for i in range(len(question)):
    blank1.append((abs(question[i] - blank[i])))
# print("Blank1: ",blank1)

count1 = 0
for i in range(len(blank1)-1, -1,-1):
    if blank1[i] != 0:
        blank1[i] += len(blank1) - 1 - i
    count1 += blank1[i]

# print("Diff: ",count1)

required_index = start_index + 2 + count1
# print("Output: ",required_index)
print(required_index)
