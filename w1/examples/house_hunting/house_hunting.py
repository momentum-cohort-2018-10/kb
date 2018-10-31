def accrue_savings_monthly(current_savings, amount_to_add, annual_rate):
    monthly_rate = annual_rate / 12
    interest = current_savings * monthly_rate
    return current_savings + interest + amount_to_add


def input_with_default(prompt, default):
    """
    Given a prompt for the user and a default value, ask the user for input.
    If the user doesn't give any input, then return the default value.
    """
    user_input = input(prompt + " [" + str(default) + "]:")
    if user_input:
        return user_input
    else:
        return default


annual_salary = int(input("Enter your annual salary:"))

monthly = annual_salary / 12

portion_saved = float(
    input("Enter the percent of your salary to save,as a decimal:"))

annual_rate_of_return = float(
    input_with_default("Enter the expected annual rate of return", 0.04))

total_cost = int(input("Enter the cost of your dream home:"))

percent_to_save = float(
    input_with_default(
        "Enter the percent of your home's cost to save as a down payment",
        0.25))

current_savings = 0
month = 0
r = annual_rate_of_return / 12

down_payment = int(total_cost * percent_to_save)

while current_savings <= down_payment:
    month = month + 1
    current_savings = accrue_savings_monthly(
        current_savings=current_savings,
        annual_rate=annual_rate_of_return,
        amount_to_add=monthly * portion_saved)

print("It will take you", (month),
      "months to have enough money for the down payment.")
