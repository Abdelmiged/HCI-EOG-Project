from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


def train_svm_model(train_signals, labels):
    svm_model = SVC(kernel='rbf', C=15, random_state=42)
    svm_model.fit(train_signals, labels)
    return svm_model


def train_random_forest_model(train_signals, labels):
    random_forest_model = RandomForestClassifier(n_estimators=150, max_depth=10, random_state=42)
    random_forest_model.fit(train_signals, labels)
    return random_forest_model


def train_logistics_regression_model(train_signals, labels):
    logistic_regression_model = LogisticRegression(multi_class='ovr')
    logistic_regression_model.fit(train_signals, labels)
    return logistic_regression_model


def train_decision_tree_model(train_signals, labels):
    decision_tree_model = DecisionTreeClassifier(random_state=42)
    decision_tree_model.fit(train_signals, labels)
    return decision_tree_model


def get_labels(signal):
    counter = 1
    class_label = 0
    sub_signal_length = len(signal) / 5
    labels = []
    for i in range(len(signal)):
        if counter > sub_signal_length:
            counter = 1
            class_label += 1
        counter += 1
        labels.append(class_label)
    return labels
