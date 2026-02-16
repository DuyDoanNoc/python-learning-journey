print("=== MY 12-MONTH PROJECTION ===")
print()

# Current state
current_salary = 25 # million VND
wife_salary = 10
total_income = current_salary + wife_salary

debt_interest = 3.6
debt_installment = 16
living_cost = 9
total_expense = debt_interest + debt_installment + living_cost

monthly_surplus = total_income - total_expense

print("CURRENT (Month 0):")
print("Income:", total_income, "million")
print("Expense:", total_expense, "million")
print("Surplus:", monthly_surplus, "million")

# After 12 months
target_salary_usd = 1500
usd_rate = 25
target_salary_vnd = (target_salary_usd * usd_rate) / 1000
new_total_income = target_salary_vnd + wife_salary
new_surplus = new_total_income - total_expense
increase = new_surplus - monthly_surplus

print("AFTER 12 MONTHS (Target):")
print("New income:", round(new_total_income, 1), "million")
print("Expense:", total_expense, "million(same)")
print("New surplus:", round(new_surplus, 1), "million")
print("Increase:", round(increase, 1), "million/month")
print()

# Annual projection
annual_increase = increase * 12
print("ANNUAL IMPACT:")
print("Extra income/year:", round(annual_increase, 1), "million")
print("Can pay extra debt:", round(annual_increase * 0.6, 1), "million/year")
print()
print("This is why I'm learning Python!")
print("Let's make it happen! pump!")