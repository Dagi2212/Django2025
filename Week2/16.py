grades = {"Dagim": "A", "Dagi": "B", "Kidan": "A"}
new_dict = {}

for name, grade in grades.items():
    new_dict.setdefault(grade, []).append(name)

print(new_dict)
