# Property of NoviX Development
# https://nsic.dev/

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = ["98", "97", "85", "88"]

# Define a nested list containing a course and a grade (str, int)
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print("Gradebook \n")
print(gradebook)

# CS100 score came back as an ace, append it to gradebook
print('CS100 score added')
print('Gradebook \n')
gradebook.append(["computer science", 100])
print(gradebook)

# Vis arts (tf is this?) came back at a 93
print('Vis arts score added')
gradebook.append(["visual arts", 93])
print(gradebook)

# Fix the profs mistake, hes bumping vis arts by 5 pts
gradebook[-1][-1] += 5

# Poetry sucks, i just wanna know if i pass
for course in gradebook:
    if course[0] == "poetry":
        course.remove(course[1])
        course.append("Pass")
        break

# Full gradebook
print('All the grades: \n')

full_gradebook = last_semester_gradebook + [gradebook]


# Print that shii
print(full_gradebook)