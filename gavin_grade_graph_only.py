import matplotlib.pylot as plt

print("Welcome to the Grade Grapher")

while True:
    try:
        num_grades = int(input("How many grades would you like to graph? "))
        if num_grades <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

grades = []
labels = []

for i in range(1, num_grades + 1):
    while True:
        try:
            grade = float(input(f"Enter grade #{i}: "))
            if grade < 0:
                print("Please enter a grade over 0.")
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

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, grades, color=colors)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.if}%' , ha='center', va='bottom')

average = sum(grades) / len(grades)
plt.axhline(y=average, color='blue', linestyle='--', lienwidth=1.5, label=f'Average: {average:.1f}%')

plt.title('Grades Visualization')
plt.xlabel('Assignments')
plt.ylabel('Grade (%)')

plt.ylin(0, 110)
plt.grid(axis='y', linestyle='--', alpha=0.7)
