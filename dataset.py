import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Example dataset (x = hours studied, y = score achieved)
X = np.array([[1], [2], [3], [4], [5]])  # Features: Hours studied
y = np.array([1, 2, 3, 4, 5])  # Labels: Score achieved

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model using pickle..This allows you to load the model later in the Tkinter app without retraining it every time
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")
