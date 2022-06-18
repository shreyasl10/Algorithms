
# The question is to print the distinct and common subjects present in an array consisting of 9 subjects (3 sets of 3 subjects)

# Sample Input

# ENGLISH
# MATHS
# SCIENCE
# HINDI
# SCIENCE
# MATHS
# MATHS
# ECONOMICS
# SCIENCE

# Sample Output

# ECONOMICS
# ENGLISH
# HINDI
# MATHS
# SCIENCE
# MATHS
# SCIENCE


subjects = []
for i in range(9):
    # Getting input from user for 9 subjects(3 sets of 3 subjects) and storing them in the subjects array
    subject = input()
    subjects.append(subject)
d = {}
for i in subjects:
    # Creating a dictionary to find out the frequency of subjects in the subjects array
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
common = []
distinct = []
for i in d.keys():
    # If a subject is present in all 3 sets , it is a common subject and it is added to the common array
    if d[i] == 3:
        common.append(i)
for i in subjects:
    # Finding out the distinct/unique subjects in the array and adding them to the distinct array
    if i not in distinct:
        distinct.append(i)
distinct.sort()
common.sort()
# Printing the two arrays as per the order defined in the question(distinct first followed by common)
print(*distinct, sep='\n')
print(*common, sep='\n')
