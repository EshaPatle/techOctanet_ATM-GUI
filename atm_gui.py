import customtkinter as ctk
from tkinter import messagebox

# Initialize the app
app = ctk.CTk()
app.title("ATM Machine")
app.geometry("400x500")

# Data store (mock DB)
user_data = {
    "pin": "1234",
    "balance": 10000,
    "history": []
}

# Global frame
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Functions
def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

def home_screen():
    clear_frame()
    ctk.CTkLabel(frame, text="Welcome to ATM", font=("Arial", 22)).pack(pady=20)

    ctk.CTkButton(frame, text="Balance Inquiry", command=balance_inquiry).pack(pady=10)
    ctk.CTkButton(frame, text="Deposit", command=deposit_screen).pack(pady=10)
    ctk.CTkButton(frame, text="Withdraw", command=withdraw_screen).pack(pady=10)
    ctk.CTkButton(frame, text="Change PIN", command=change_pin_screen).pack(pady=10)
    ctk.CTkButton(frame, text="Transaction History", command=transaction_history).pack(pady=10)

def balance_inquiry():
    clear_frame()
    ctk.CTkLabel(frame, text=f"Your Balance is ₹{user_data['balance']}", font=("Arial", 18)).pack(pady=20)
    ctk.CTkButton(frame, text="Back", command=home_screen).pack(pady=10)

def deposit_screen():
    clear_frame()
    ctk.CTkLabel(frame, text="Enter amount to deposit:", font=("Arial", 16)).pack(pady=10)
    amount_entry = ctk.CTkEntry(frame)
    amount_entry.pack(pady=5)

    def do_deposit():
        try:
            amount = int(amount_entry.get())
            if amount <= 0:
                raise ValueError
            user_data['balance'] += amount
            user_data['history'].append(f"Deposited ₹{amount}")
            messagebox.showinfo("Success", f"₹{amount} deposited successfully.")
            home_screen()
        except ValueError:
            messagebox.showerror("Invalid", "Enter a valid amount")

    ctk.CTkButton(frame, text="Deposit", command=do_deposit).pack(pady=10)
    ctk.CTkButton(frame, text="Back", command=home_screen).pack(pady=5)

def withdraw_screen():
    clear_frame()
    ctk.CTkLabel(frame, text="Enter amount to withdraw:", font=("Arial", 16)).pack(pady=10)
    amount_entry = ctk.CTkEntry(frame)
    amount_entry.pack(pady=5)

    def do_withdraw():
        try:
            amount = int(amount_entry.get())
            if amount <= 0 or amount > user_data['balance']:
                raise ValueError
            user_data['balance'] -= amount
            user_data['history'].append(f"Withdrew ₹{amount}")
            messagebox.showinfo("Success", f"₹{amount} withdrawn successfully.")
            home_screen()
        except ValueError:
            messagebox.showerror("Invalid", "Enter valid amount within available balance")

    ctk.CTkButton(frame, text="Withdraw", command=do_withdraw).pack(pady=10)
    ctk.CTkButton(frame, text="Back", command=home_screen).pack(pady=5)

def change_pin_screen():
    clear_frame()
    ctk.CTkLabel(frame, text="Enter current PIN:").pack(pady=5)
    old_pin = ctk.CTkEntry(frame, show="*")
    old_pin.pack(pady=5)

    ctk.CTkLabel(frame, text="Enter new PIN:").pack(pady=5)
    new_pin = ctk.CTkEntry(frame, show="*")
    new_pin.pack(pady=5)

    def update_pin():
        if old_pin.get() == user_data['pin']:
            user_data['pin'] = new_pin.get()
            user_data['history'].append("PIN changed successfully")
            messagebox.showinfo("Success", "PIN updated successfully.")
            home_screen()
        else:
            messagebox.showerror("Error", "Incorrect current PIN")

    ctk.CTkButton(frame, text="Change PIN", command=update_pin).pack(pady=10)
    ctk.CTkButton(frame, text="Back", command=home_screen).pack(pady=5)

def transaction_history():
    clear_frame()
    ctk.CTkLabel(frame, text="Last Transactions:", font=("Arial", 16)).pack(pady=10)
    for item in user_data['history'][-5:][::-1]:
        ctk.CTkLabel(frame, text=item).pack()
    ctk.CTkButton(frame, text="Back", command=home_screen).pack(pady=10)

# Start
home_screen()
app.mainloop()

