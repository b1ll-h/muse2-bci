import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import joblib

print("Loading data...")
X = np.load("X.npy")
y = np.load("y.npy")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.4, random_state=42, stratify=y)

clf = MLPClassifier(
    hidden_layer_sizes=(64, 32),
    activation="tanh",
    max_iter=1000,
    random_state=42)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=["NOBLINK", "BLINK"]))

cv_scores = cross_val_score(clf, X_scaled, y, cv=3)
print(f"Mean accuracy: {cv_scores.mean():.3f}")

joblib.dump(clf, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
print("Saved model.pkl and scaler.pkl!")