project = float(input("Enter project score (out of 100): "))
internal = float(input("Enter internal score (out of 100): "))
external = float(input("Enter external score (out of 100): "))

if project < 50:
    print(f"You failed the project with score:{project}")
if internal < 50:
    print(f"You failed the internal score with score:{internal}")
if external < 50:
    print(f"You failed the external score with score:{external}")
else:
    total_score = (project * 0.7) + (internal * 0.1) + (external * 0.2)

    if total_score >= 90:
        grade = "A"
    elif total_score >= 80:
        grade = "B"
    else:
        grade = "C"

    print(f"Total score: {total_score:.2f}%")
    print(f"Grade: {grade}")

