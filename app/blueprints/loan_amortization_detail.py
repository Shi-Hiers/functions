from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db
from app.functions import generate_amortization_schedule

loan_amortization_detail = Blueprint('loan_amortization_detail', __name__)

@loan_amortization_detail.route('/loan_detail/<int:loan_info_id>')
def loan_detail(loan_info_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute('SELECT loan_amount, interest_rate, term_years FROM loan_info WHERE loan_info_id = %s', (loan_info_id,))
    loan_data = cursor.fetchone()

    loan_amount = float(loan_data['loan_amount'])
    interest_rate = float(loan_data['interest_rate'])
    loan_term_years = int(loan_data['term_years'])

    # Use the external function for the amortization schedule
    amortization_schedule = generate_amortization_schedule(loan_amount, interest_rate, loan_term_years)

    return render_template('loan_detail.html', loan_schedule=amortization_schedule, loan_id=loan_info_id)
