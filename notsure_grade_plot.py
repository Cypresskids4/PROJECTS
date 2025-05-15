import matplotlib.pyplot as plt

print("Welcome to the Grade Grapher!")

while True:
    try:
        num_grades = int(input("How many grades do you want to enter? "))
        if num_grades <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input, please enter a number.")


grades = []
labels = []

for i in range(1, num_grades + 1):
    while True:
        try:
            grade = float(input(f"Enter grade {i}: "))
            if 0 <= grade <= 100:
                grades.append(grade)
                labels.append(f"Grade {i}")
                break
        except ValueError:
            print("Invalid input, please enter a number.")


plt.figure(figsize=(10, 6))
plt.bar(labels, grades, color='skyblue')

bars =plt.bar(labels, grades, color='skyblue')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')


plt.title("Grades Visualization")
plt.xlabel("Assignment")
plt.ylabel('Grade (%)')


plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
