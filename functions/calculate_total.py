# Write a function calculate_total that takes 3 parameters:
#   a. meal: the cost of the meal
#   b. tax_rate: the percent tax (e.g., NJ tax would be 0.07)
#   c. tip_rate: the percent tip (e.g., a 20% tip rate is 0.20)
# Proper tipping technique dictates that the tip should be calculated
# based on the total cost of the meal, before tax is applied. Then,
# return the total. Test your function works by using the following call:
#   calculate_total(53.48, .07, .18).

# Note that the total for the above meal with tax & tip is $66.85.

def calculate_total(meal, tax_rate, tip_rate):
    tip = meal * tip_rate
    tax = meal * tax_rate
    return (meal + tip + tax)


def main():
    print(calculate_total(53.48, .07, .18))

main()