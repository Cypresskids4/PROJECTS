import matplotlib.pyplot as plt

print("welcome to grade grapher\n")

while True:
    try:
        num_grades = int(input("Enter your grades you would want to grapgh: "))
        if num_grades<=0:
            print("Please enter a positive number.")
            continue 
        break
    except ValueError:
        print("Invalid input. Please enter numbers.")

grades = []
labels = []

for i in range(1, num_grades + 1):
    while True:
        try:
            grade = int(input(f"Enter your grade {i}: "))
            if grade < 0 or grade > 100:
                print("Please enter a number between 0 and 100.")
                continue
            grades.append(grade)
            labels.append(f"Grade {i}")
            break
        except ValueError:
            print("Invalid input. Please enter numbers.")

colors = []
for grade in grades:
    if grade >= 90:
        colors.append('green')
    elif grade >= 80:
        colors.append('blue')
    elif grade >= 70:
        colors.append('yellow')
    elif grade >= 60:
        colors.append('orange')
    else:
        colors.append('red')

            
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, grades, color=colors)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.1f}%', ha='center', va='bottom')

average = sum(grades) / len(grades)
plt.axhline(y=average, color='blue', linestyle='--', label=f'Average: {average:.1f}%')
 
plt.title("Grades graph")
plt.xlabel("assignment")
plt.ylabel("percentage")

plt.ylim(0, 110)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()