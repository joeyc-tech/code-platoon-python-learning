

days_of_week = ["Monday", "Wednesday"]
days_of_week.insert(1, "Tuesday")
days_of_week.append("Thursday")
days_of_week.insert(0, "Sunday")
print(days_of_week)

# use.remove and .POP

days_of_week.remove("Tuesday")
days_of_week.pop()
days_of_week.remove("Sunday")
print(days_of_week)