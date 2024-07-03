import tkinter as tk
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

def generate_yearly_report(expense_data):
    yearly_expenses = defaultdict(float)
    for expense in expense_data:
        year = expense[0][:4]  # Extracting year from date (assuming date format is YYYY-MM-DD)
        yearly_expenses[year] += expense[2]
    
    years = list(yearly_expenses.keys())
    total_expenses = [yearly_expenses[year] for year in years]

    plt.figure(figsize=(8, 6))
    plt.bar(years, total_expenses, color='skyblue')
    plt.xlabel('Year')
    plt.ylabel('Total Expenses ($)')
    plt.title('Yearly Expense Report')
    plt.grid(True)
    plt.show()

def generate_monthly_report(expense_data):
    monthly_expenses = defaultdict(float)
    for expense in expense_data:
        month = expense[0][5:7]  # Extracting month from date (assuming date format is YYYY-MM-DD)
        monthly_expenses[month] += expense[2]
    
    months = list(monthly_expenses.keys())
    total_expenses = [monthly_expenses[month] for month in months]

    plt.figure(figsize=(8, 6))
    plt.bar(months, total_expenses, color='lightgreen')
    plt.xlabel('Month')
    plt.ylabel('Total Expenses ($)')
    plt.title('Monthly Expense Report')
    plt.grid(True)
    plt.show()

def generate_category_report(expense_data):
    category_expenses = defaultdict(float)
    for expense in expense_data:
        category = expense[1]  # Category
        category_expenses[category] += expense[2]
    
    categories = list(category_expenses.keys())
    total_expenses = [category_expenses[category] for category in categories]

    plt.figure(figsize=(10, 6))
    plt.bar(categories, total_expenses, color='orange')
    plt.xlabel('Category')
    plt.ylabel('Total Expenses ($)')
    plt.title('Category-wise Expense Report')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def generate_daily_report(expense_data):
    daily_expenses = defaultdict(float)
    for expense in expense_data:
        date = expense[0]  # Assuming date format is YYYY-MM-DD
        daily_expenses[date] += expense[2]
    
    dates = list(daily_expenses.keys())
    total_expenses = [daily_expenses[date] for date in dates]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, total_expenses, marker='o', color='purple')
    plt.xlabel('Date')
    plt.ylabel('Total Expenses ($)')
    plt.title('Daily Expense Report')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def generate_graph(parameter, expense_data):
    if parameter == 'Year':
        generate_yearly_report(expense_data)
    elif parameter == 'Month':
        generate_monthly_report(expense_data)
    elif parameter == 'Date':
        generate_daily_report(expense_data)
    elif parameter == 'Category':
        generate_category_report(expense_data)

def expense_page():
    login_window.destroy()
    expenses = []

    def add_expense():
        date = date_entry.get()
        category = category_combobox.get()
        amount = amount_entry.get()
        
        try:
            amount = float(amount)
            expenses.append((date, category, amount))
            update_expense_list()
            update_total_expenses()
        except ValueError:
            print("Please enter a valid amount")

    def update_expense_list():
        expense_listbox.delete(0, tk.END)
        for expense in expenses:
            expense_listbox.insert(tk.END, f"{expense[0]} - {expense[1]} - ${expense[2]:.2f}")

    def update_total_expenses():
        total_amount = sum(expense[2] for expense in expenses)
        total_label.config(text=f"Total Expenses: ${total_amount:.2f}")

    def generate_report():
       parameter = report_parameter.get()
       generate_graph(parameter, expenses)

    # Initialize the main window
    root = tk.Tk()
    root.title("Expense Tracker - Add Expense")
    root.geometry("1920x1080")  # Larger window size
    root.configure(bg="#f7f7f7")

    # Define custom fonts
    custom_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
    sub_font = tkfont.Font(family="Helvetica", size=14)

    # Create a frame to hold the widgets
    frame = tk.Frame(root, bg="#f7f7f7")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Create and place the heading with increased padding
    heading = tk.Label(frame, text="Add Expense", font=custom_font, bg="#f7f7f7", fg="#333")
    heading.grid(row=0, columnspan=2, pady=(50, 30))  # Increased top padding to 50, bottom padding to 30

    # Create and place the date label and entry
    date_label = tk.Label(frame, text="Date (YYYY-MM-DD):", font=sub_font, bg="#f7f7f7", fg="#666")
    date_label.grid(row=1, column=0, pady=10, padx=10, sticky="e")

    def validate_date(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def on_validate_date(P):
        if validate_date(P) or P == "":
            return True
        else:
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
            return False
    
    date_var = tk.StringVar()
    validate_cmd = (root.register(on_validate_date), '%P')
    date_entry = tk.Entry(frame, textvariable=date_var, font=sub_font, width=30, validate="focusout", validatecommand=validate_cmd)
    date_entry.grid(row=1, column=1, pady=10)

    # Create and place the category label and combobox
    category_label = tk.Label(frame, text="Category:", font=sub_font, bg="#f7f7f7", fg="#666")
    category_label.grid(row=2, column=0, pady=10, padx=10, sticky="e")
    category_combobox = tk.Entry(frame, font=sub_font, width=30)
    category_combobox.grid(row=2, column=1, pady=10)

    # Create and place the amount label and entry
    amount_label = tk.Label(frame, text="Amount:", font=sub_font, bg="#f7f7f7", fg="#666")
    amount_label.grid(row=3, column=0, pady=10, padx=10, sticky="e")
    amount_entry = tk.Entry(frame, font=sub_font, width=30)
    amount_entry.grid(row=3, column=1, pady=10)

    # Create and place the add expense button
    add_expense_button = tk.Button(frame, text="Add Expense", font=sub_font, bg="#007bff", fg="#fff", padx=20, pady=10, relief="flat", command=add_expense)
    add_expense_button.grid(row=4, columnspan=2, pady=20)

    # Create and place the expense listbox
    expense_listbox = tk.Listbox(frame, font=sub_font, width=50, height=10)
    expense_listbox.grid(row=5, columnspan=2, pady=10)

    # Create and place the total label with increased bottom padding
    total_label = tk.Label(frame, text="Total Expenses: $0.00", font=sub_font, bg="#f7f7f7", fg="#333")
    total_label.grid(row=6, columnspan=2, pady=30)  # Increased bottom padding to 30

    # Create a label for report parameter
    report_param_label = tk.Label(frame, text="Generate Report By:", font=sub_font, bg="#f7f7f7", fg="#666")
    report_param_label.grid(row=7, column=0, pady=10, padx=10, sticky="e")

    # Dropdown menu for report parameter options
    global report_parameter
    report_parameter_options = ['Year', 'Month', 'Date', 'Category']
    report_parameter = tk.StringVar()
    report_param_dropdown = tk.OptionMenu(frame, report_parameter, *report_parameter_options)
    report_param_dropdown.config(font=sub_font, bg="#fff", fg="#333", width=20)
    report_param_dropdown.grid(row=7, column=1, pady=10)

    # Create and place the generate report button
    generate_report_button = tk.Button(frame, text="Generate Report", font=sub_font, bg="#28a745", fg="#fff", padx=20, pady=10, relief="flat", command=generate_report)
    generate_report_button.grid(row=8, columnspan=2, pady=20)

    # Run the application
    root.mainloop()


def login_screen():
    welcome_window.destroy()
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if (username=="root" and password=="root@123"):
            expense_page()
        print(f"Username: {username}, Password: {password}")
    # Add your login logic here

    # Initialize the main window
    root = tk.Tk()
    global login_window
    login_window = root
    root.title("Expense Tracker - Login")
    root.geometry("1920x1080")
    root.configure(bg="#f7f7f7")

    # Define custom fonts
    custom_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
    sub_font = tkfont.Font(family="Helvetica", size=14)

    # Create a frame to hold the widgets
    frame = tk.Frame(root, bg="#f7f7f7")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Create and place the heading
    heading = tk.Label(frame, text="Login Using Your Details", font=custom_font, bg="#f7f7f7", fg="#333")
    heading.grid(row=0, columnspan=2, pady=40)

    # Create and place the username label and entry
    username_label = tk.Label(frame, text="Username:", font=sub_font, bg="#f7f7f7", fg="#666")
    username_label.grid(row=1, column=0, pady=5, padx=10, sticky="e")
    username_entry = tk.Entry(frame, font=sub_font, width=30)
    username_entry.grid(row=1, column=1, pady=5)

    # Create and place the password label and entry
    password_label = tk.Label(frame, text="Password:", font=sub_font, bg="#f7f7f7", fg="#666")
    password_label.grid(row=2, column=0, pady=5, padx=10, sticky="e")
    password_entry = tk.Entry(frame, font=sub_font, width=30, show="*")
    password_entry.grid(row=2, column=1, pady=5)

    # Create and place the login button
    login_button = tk.Button(frame, text="Login", font=sub_font, bg="#007bff", fg="#fff", padx=20, pady=10, relief="flat", command=login)
    login_button.grid(row=3, columnspan=2, pady=20)

    # Run the application
    root.mainloop()


def welcome_screen():
    def get_started():
        # Placeholder function for button click
        print("Get Started button clicked")

    # Initialize the main window
    root = tk.Tk()
    global welcome_window
    welcome_window = root
    root.title("Expense Tracker")
    root.geometry("1920x1080")
    root.configure(bg="#f7f7f7")

    # Define custom fonts
    custom_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
    sub_font = tkfont.Font(family="Helvetica", size=14)

    # Create a frame to hold the widgets
    frame = tk.Frame(root, bg="#f7f7f7")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Create and place the heading
    heading = tk.Label(frame, text="Welcome to Expense Tracker", font=custom_font, bg="#f7f7f7", fg="#333")
    heading.pack(pady=10)

    # Create and place the sub heading
    sub_heading = tk.Label(frame, text="Your personal finance manager", font=sub_font, bg="#f7f7f7", fg="#666")
    sub_heading.pack(pady=10)

    # Create and place the get started button
    get_started_button = tk.Button(frame, text="Get Started", font=sub_font, bg="#007bff", fg="#fff", padx=20, pady=10, relief="flat", command=login_screen)
    get_started_button.pack(pady=20)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    welcome_screen()
