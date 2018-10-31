"""Stack Exchange - User Reputation Prediction."""

from sklearn.model_selection import train_test_split

def data_loader():
    """Data loader."""
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=233)
    return x_train, x_test, y_train, y_test