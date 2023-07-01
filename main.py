import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font


def is_armstrong_number(number):
    """
    Check if a given number is an Armstrong number.

    An Armstrong number of 3 digits is a number where the sum of the cubes of each digit is equal to the number itself.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    # Calculate the sum of the cubes of each digit
    sum_of_cubes = 0
    temp_num = number
    while temp_num > 0:
        digit = temp_num % 10
        sum_of_cubes += digit ** 3
        temp_num //= 10

    # Check if it's an Armstrong number
    return sum_of_cubes == number


def check_armstrong_number(event=None):
    """
    Handle the check button click or Enter key press event.

    This function retrieves the number from the entry field, validates it, and checks if it is an Armstrong number.
    The result is displayed in a messagebox.

    Args:
        event (tk.Event, optional): The event triggered by the check button or Enter key press. Defaults to None.
    """
    try:
        number = entry.get().strip()
        if not number.isdigit():
            raise ValueError("Invalid input: Please enter a numeric value.")
        number = int(number)
        if number < 100 or number > 999:
            raise ValueError("Invalid input: Please enter a 3-digit number between 100 and 999.")
    except ValueError as e:
        messagebox.showwarning("Invalid Input", str(e))
        return

    if is_armstrong_number(number):
        messagebox.showinfo("Result", f"{number} is an Armstrong number.")
    else:
        messagebox.showinfo("Result", f"{number} is not an Armstrong number.")

    entry.delete(0, tk.END)  # Clear the entry field


if __name__ == "__main__":
    # Create the main window
    window = tk.Tk()
    window.title("Armstrong Number Checker")
    window.geometry("350x200")

    # Define custom fonts
    title_font = Font(family="Arial", size=16, weight="bold")
    label_font = Font(family="Arial", size=12)
    button_font = Font(family="Arial", size=12, weight="bold")

    # Create the title label
    title_label = tk.Label(window, text="Armstrong Number Checker", font=title_font)
    title_label.pack(pady=10)

    # Create the label and entry for input
    label = tk.Label(window, text="Enter a 3-digit number:", font=label_font)
    label.pack()
    entry = tk.Entry(window, font=label_font)
    entry.pack()

    # Bind the Enter key press event to the check_armstrong_number function
    window.bind("<Return>", check_armstrong_number)

    # Create the check button
    check_button = tk.Button(window, text="Check", command=check_armstrong_number, font=button_font)
    check_button.pack(pady=10)

    # Run the GUI event loop
    window.mainloop()
