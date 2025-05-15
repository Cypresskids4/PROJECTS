import matplotlib.pyplot as plt
print("welcome Grade Plotting Module\n")



while True:
    try:
        num_grades = int(input("how many grades would you like to graph? "))
        if num_grades <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invaled input. Please enter a number.")


grades = []
labels = []
for i in range(1, num_grades + 1):
    while True:
        try:
            grade = float(input(f"Enter grade #{i}: "))
            if grade < 0 or grade > 100:
                print("Please enter a grade between 0 and 100.")
                continue
            grades.append(grade)
            labels.append(f"Grade {i}")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

            plt.figure(figsize=(10, 6))
            bars = plt.bar(labels, grades, color='skyblue')

            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}', ha='center', va='bottom',)


bars = plt.bar(labels, grades, color='skyblue')

for bars in bars:
    yval = bars.get_height()
    plt.text(bars.get_x() + bars.get_width()/2, yval + 1, f'{yval}', ha='center', va='bottom', fontsize=10)

plt.title("Grades visualization")
plt.xlabel("Assignments")
plt.ylabel("Grades %")


plt.ylim(0, 110)
plt.grid(axis='y', linestyle='--', alpha=0.7)




plt.tight_layout()
plt.show()
