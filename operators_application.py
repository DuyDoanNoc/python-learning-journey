print("=== OPERATORS - MY FINANCIAL CALCULATOR ===")
print()

# Current financial situation
monthly_income = 25 # million VND
wife_income = 10
total_income = monthly_income + wife_income

debt_interest = 3.6
debt_installment = 16
living_cost = 9
total_expense = debt_interest + debt_installment + living_cost

monthly_surplus = total_income - total_expense

print("CURRENT FINANCES:")
print(f"Total Income: {total_income} million")
print(f"Total Expense: {total_expense} million")
print(f"Monthly Surplus: {monthly_surplus:.2f} million")
print()

# After 12 months - target scenario
target_monthly = 37.5 # 1500 USD = 37.5M VND
new_total_income = target_monthly + wife_income
new_surplus = new_total_income - total_expense
increase = new_surplus - monthly_surplus

print("AFTER 12 MONTHS (TARGET):")
print(f"New Income: {new_total_income} million")
print(f"Same Expense: {total_expense} million")
print(f"New Surplus: {new_surplus} million")
print(f"Increase: +{increase} million/month")
print()

# Annual impact
annual_increase = increase * 12
debt_payoff_boost = annual_increase * 0.6   # 60% to debt

print("ANNUAL IMPACT:")
print(f"Extra income/year: {annual_increase:.0f} million")
print(f"Extra debt payment: {debt_payoff_boost:.0f} million")
print()

# Check if goal is realistic
months_to_goal = 12
hours_per_day = 2
total_hours = months_to_goal * 30 * hours_per_day

effort_sufficient = total_hours > 500 # Need 500+ hours
print(f"Total study hours planned: {total_hours}")
print(f"Is effort sufficient? {effort_sufficient}")
print()

# Motivation
if effort_sufficient:
    print("Yes! This plan will work!")
    print("Keep going, Duy!")
else:
    print("Need to study more hours")