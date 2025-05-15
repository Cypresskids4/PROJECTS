#grade_graph_only_styled.py
import matplotlib.pyplot as plt

print("Welcome to the Grade Grapher!\n")


#1. Ask how many grades to enter
while True:
    try:
        num_grades = int(input("how many grades would you like to graph? "))
        if num_grades <= 0:
            print("Please enter a positive number")
            continue
        break
    except ValueError:
        print("invalid input. Please enter a number")


#2. Gather grades
grades = []
labels = []


for i in range(1, num_grades + 1):
    while True:
        try:
            grade = float(input(f"Enter grade #{i}: "))
            if grade < 0:
                print("please enter a grade over 0.")
                continue
            grades.append(grade)
            labels.append(f"Grade {i}")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

colors = []
for grade in grades:
    if grade >= 90:
        colors.append('green')
    elif grade >= 70:
        colors.append('blue')
    else:
        colors.append('red')



plt.figure(figsize=(10,6))
bars = plt.bar(labels,grades,color=colors)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.1f}%', ha='center', va='bottom')

average = sum(grades) / len(grades)
plt.axhline(y=average, color='blue', linestyle='--', linewidth=1.5, label=f'Average: {average:.1f}%')

plt.title('grades Visualization')
plt.xlabel('assignments')
plt.ylabel('Grade (%)')


plt.ylim(0,110)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.xticks(rotation=45)


plt.legend()


plt.tight_layout()
plt.show()