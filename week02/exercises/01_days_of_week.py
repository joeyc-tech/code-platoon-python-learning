#You Try: 
# 1) Start with the following list:
# days_of_week = ["Monday", "Wednesday"]
# Insert "Tuesday" between the two days.
# Add "Thursday" to the end.
# Add "Sunday" to the beginning.

days_of_week = ["Monday", "Wednesday"]
days_of_week.insert(1, "Tuesday")
days_of_week.append("Thursday")
days_of_week.insert(0, "Sunday")
print(days_of_week)
