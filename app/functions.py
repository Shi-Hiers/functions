# create a function that calculates the letter grade based on the number grade
def calculate_grade(number_grade):
    try:
        # Convert number_grade to an integer
        number_grade = int(number_grade)

        if number_grade >= 90:
            letter_grade = "A"
        elif number_grade >= 80:
            letter_grade = "B"
        elif number_grade >= 70:
            letter_grade = "C"
        elif number_grade >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"

        return letter_grade
    except ValueError:
        # Handle the case where conversion fails (e.g., if input is not a valid number)
        return "Invalid grade input"


# create a function that calculates the loan amortization
def calculate_amortization(loan_amount, term_years, interest_rate):
    loan_amount = float(loan_amount)
    term_years = int(term_years)
    interest_rate = float(interest_rate)
    monthly_interest_rate = interest_rate / 12 / 100
    number_of_payments = term_years * 12
    monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
    return monthly_payment

# New function for detailed amortization schedule
def generate_amortization_schedule(loan_amount, interest_rate, loan_term_years):
    loan_term_months = loan_term_years * 12
    monthly_interest_rate = interest_rate / 12 / 100
    monthly_payment = calculate_amortization(loan_amount, loan_term_years, interest_rate)
    loan_amortization_list = []

    for i in range(1, loan_term_months + 1):
        interest_paid = loan_amount * monthly_interest_rate
        principal_paid = monthly_payment - interest_paid
        remaining_balance = loan_amount - principal_paid

        loan_amortization_list.append({
            'month': i,
            'starting_balance': loan_amount,
            'interest_paid': interest_paid,
            'principal_paid': principal_paid,
            'monthly_payment': monthly_payment,
            'remaining_balance': remaining_balance
        })

        loan_amount = remaining_balance

    return loan_amortization_list

