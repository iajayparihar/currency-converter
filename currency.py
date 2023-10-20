import tkinter as tk

# Function to perform currency conversion
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = entry_from_currency.get().upper()
        to_currency = entry_to_currency.get().upper()
        
        # Conversion rates (hardcoded for USD to various currencies)
        conversion_rates = {
            'USD': 1.00,
            'EUR': 0.85,
            'GBP': 0.72,
            'JPY': 110.21,
            'AUD': 1.30,
            'CAD': 1.27,
            'INR': 74.96,
            'CNY': 6.45
        }
        
        converted_amount = round(amount * conversion_rates[from_currency] / conversion_rates[to_currency], 2)
        label_result.config(text=f"Converted Amount: {converted_amount} {to_currency}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Currency Converter")

root.geometry('400x400')

# Labels and entry fields
label_amount = tk.Label(root, text="Enter Amount:")
label_amount.pack(pady=10)
entry_amount = tk.Entry(root, font=("Arial", 14))
entry_amount.pack(pady=10)

label_from_currency = tk.Label(root, text="From Currency (USD or EUR):")
label_from_currency.pack(pady=10)
entry_from_currency = tk.Entry(root, font=("Arial", 14))
entry_from_currency.pack(pady=10)

label_to_currency = tk.Label(root, text="To Currency (USD or EUR):")
label_to_currency.pack(pady=10)
entry_to_currency = tk.Entry(root, font=("Arial", 14))
entry_to_currency.pack(pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency, font=("Arial", 14))
convert_button.pack(pady=20)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 16), fg="green")
label_result.pack(pady=10)

# Run the application
root.mainloop()
