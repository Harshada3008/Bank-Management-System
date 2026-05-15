from flask import Flask, render_template, request, redirect, url_for, session, flash
from src.bank import Bank

app = Flask(__name__)
app.secret_key = 'replace-with-a-secure-key'

bank = Bank()


def get_current_user():
    email = session.get('email')
    if not email:
        return None
    if not bank.current_user or bank.current_user.email != email:
        bank.load_user_by_email(email)
    return bank.get_current_user()


@app.route('/')
def index():
    if get_current_user():
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        if not name or not email or not password:
            flash('All fields are required.', 'error')
        elif bank.register_user(name, email, password):
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('User already exists with that email.', 'error')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        if bank.login(email, password):
            session['email'] = email
            flash('Login successful.', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid email or password.', 'error')
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    balance = bank.get_balance()
    transactions = bank.get_transactions()
    return render_template('dashboard.html', user=user, balance=balance, transactions=transactions)


@app.route('/deposit', methods=['POST'])
def deposit():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    amount = request.form.get('amount', '0')
    try:
        value = float(amount)
    except ValueError:
        flash('Enter a valid amount.', 'error')
        return redirect(url_for('dashboard'))
    if bank.deposit(value):
        flash('Deposit successful.', 'success')
    else:
        flash('Deposit failed. Amount must be positive.', 'error')
    return redirect(url_for('dashboard'))


@app.route('/withdraw', methods=['POST'])
def withdraw():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    amount = request.form.get('amount', '0')
    try:
        value = float(amount)
    except ValueError:
        flash('Enter a valid amount.', 'error')
        return redirect(url_for('dashboard'))
    if bank.withdraw(value):
        flash('Withdrawal successful.', 'success')
    else:
        flash('Withdrawal failed. Check your balance.', 'error')
    return redirect(url_for('dashboard'))


@app.route('/transfer', methods=['POST'])
def transfer():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    amount = request.form.get('amount', '0')
    to_email = request.form.get('to_email', '').strip().lower()
    try:
        value = float(amount)
    except ValueError:
        flash('Enter a valid amount.', 'error')
        return redirect(url_for('dashboard'))
    if not to_email:
        flash('Recipient email is required.', 'error')
        return redirect(url_for('dashboard'))
    if bank.transfer(to_email, value):
        flash('Transfer completed.', 'success')
    else:
        flash('Transfer failed. Check recipient and balance.', 'error')
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    session.clear()
    bank.logout()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
