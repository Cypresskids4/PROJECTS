# garde _graph_only.py
import matplotlib.pyplot as plt

print("Welcome to the Grade Grapher!\n")

# 1. Ask how many grades to enter
while True:
    try:
        num_grades = int(input("How many grades would you like to graph? "))
        if num_grades <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number")

# 2. Gather grades
grades = []
labels = []

for i in range(1, num_grades + 1):
    while True:
        try:
            grade = float(input(f"Enter garde #{i}:"))
            if grade < 0:
                print("Please enter a grade over 0.")
                continue
            grades.append(grade)
            labels.append(f"Grade {i}")
            break
        except ValueError:
            print("Invalid input. Please enetr a number.")

# 3. Determine bar colors based on garde values # <-- added
colors = []
for grade in grades: # <-- added
    if grade >= 90: # <-- added
        colors.append('green') # <-- added
    elif grade >= 70: # <-- added
        colors.append('blue') # <-- added
    else:
        colors.append('red') # <-- added

# 4. Plot the grades
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, grades, color=colors)

#Annotate bars with grade values
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.1f}%', ha='center', va='bottom')

# Add an average line # # <-- added
average = sum(grades) / len(grades) # <-- added
plt.axhline(y=average, color='blue', linestyle='--', linewidth=1.5, label=f'Average: {average:.1f}%') # <-- added

# Set titles and labels
plt.title('Grades Visualization')
plt.xlabel('Assignments')
plt.ylabel('Grade (%)')

# Set y-axis limit for better visuals
plt.ylim(0, 110)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Improve tick formatting # <-- added
plt.xticks(rotation=45) # <-- added for better label spacing

# Add legend for the average line # <-- added
plt.legend() # <-- added

plt.tight_layout()
plt.show()
