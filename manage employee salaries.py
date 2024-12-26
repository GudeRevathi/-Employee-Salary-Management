employees = {}


def add_employee(name, salary):
    if name in employees:
        print(f"Employee '{name}' already exists.")
    else:
        employees[name] = salary
        print(f"Employee '{name}' added with a salary of ${salary:.2f}.")


def update_salary(name, salary):
    if name in employees:
        employees[name] = salary
        print(f"Salary of '{name}' updated to ${salary:.2f}.")
    else:
        print(f"Employee '{name}' does not exist.")


def display_employees():
    if not employees:
        print("No employees found.")
    else:
        print("\nEmployee Salary List:")
        for name, salary in employees.items():
            print(f"{name}: ${salary:.2f}")

while True:
    print("\n1. Add Employee")
    print("2. Update Salary")
    print("3. Display Employees")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter employee name: ")
        salary = float(input("Enter employee salary: "))
        add_employee(name, salary)
    elif choice == "2":
        name = input("Enter employee name: ")
        salary = float(input("Enter new salary: "))
        update_salary(name, salary)
    elif choice == "3":
        display_employees()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
