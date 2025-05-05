def evaluate_performance(punctuality, quality, efficiency, teamwork):
    score = punctuality + quality + efficiency + teamwork
    if score >= 18:
        return "Outstanding"
    elif score >= 14:
        return "Exceeds Expectations"
    elif score >= 10:
        return "Meets Expectations"
    else:
        return "Needs Improvement"


print("Enter ratings from 1 (low) to 5 (high).")
p = int(input("Punctuality: "))
q = int(input("Work Quality: "))
e = int(input("Efficiency: "))
t = int(input("Teamwork: "))

rating = evaluate_performance(p, q, e, t)
print(f"Final Performance Rating → {rating}")