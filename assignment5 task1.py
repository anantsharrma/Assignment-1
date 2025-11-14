marks = {"john":98, "mathew":76, "sebastian":89, "mia":67}
name = input("Enter the name of student:").strip()
if name in marks:
    print(f"{name}'s marks is {marks[name]}")
else:
    print(f"Student not found")