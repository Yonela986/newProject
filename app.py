import tkinter as tk
from tkinter import messagebox
import pickle

# Load the pre-trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Function to predict the score based on user input
def predict_score():
    try:
        # Get the input value from the entry widget
        hours = float(entry.get())
        
        # Predict the score using the trained model
        predicted_score = model.predict([[hours]])[0]
        
        # Display the result in the label
        result_label.config(text=f"Predicted Score: {predicted_score:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for hours studied.")

# Create the main window
root = tk.Tk()
root.title("Machine Learning Model - Prediction")

# Create and place widgets
entry_label = tk.Label(root, text="Enter Hours Studied:")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

predict_button = tk.Button(root, text="Predict Score", command=predict_score)
predict_button.pack(pady=10)

result_label = tk.Label(root, text="Predicted Score: N/A")
result_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
