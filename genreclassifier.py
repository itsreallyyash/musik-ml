import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import cross_val_score
from imblearn.over_sampling import SMOTE
from collections import Counter
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_curve, roc_auc_score
from collections import Counter

data = pd.read_csv("ultimate.csv")
print(data.head())

print(data.isnull().sum())

sns.countplot(x='genre', data=data)
plt.title('Distribution of Genres')
plt.show()

print(data.columns)

# Separate features (X) and target variable (y)
X = data[['Danceability', 'Energy', 'Acousticness', 'Instrumentalness', 'Tempo']]
y = data['genre']

# Convert features to numeric type using .loc
X.loc[:, 'Danceability'] = pd.to_numeric(X['Danceability'], errors='coerce')
X.loc[:, 'Energy'] = pd.to_numeric(X['Energy'], errors='coerce')
X.loc[:, 'Acousticness'] = pd.to_numeric(X['Acousticness'], errors='coerce')
X.loc[:, 'Instrumentalness'] = pd.to_numeric(X['Instrumentalness'], errors='coerce')
X.loc[:, 'Tempo'] = pd.to_numeric(X['Tempo'], errors='coerce')

# Drop rows with NaN values (if any)
X = X.dropna()

# Apply SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Display the class distribution after SMOTE
print("Class distribution after SMOTE:", Counter(y_resampled))

plt.figure(figsize=(8, 5))
sns.countplot(y=y_resampled)
plt.title('Class Distribution after SMOTE')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()

# Number of samples in the resampled dataset
num_samples_resampled = X_resampled.shape[0]

# Number of features in the resampled dataset
num_features_resampled = X_resampled.shape[1]

# Distribution of classes in the resampled dataset
class_distribution_resampled = Counter(y_resampled)

print("Number of samples in the resampled dataset:", num_samples_resampled)
print("Number of features in the resampled dataset:", num_features_resampled)
print("\nDistribution of classes in the resampled dataset:")
print(class_distribution_resampled)

# Instantiate the classifiers
classifiers = {
    'Random Forest': RandomForestClassifier(),
    'Gradient Boosting': GradientBoostingClassifier(),
    'K-Nearest Neighbors': KNeighborsClassifier()
}

# Train and evaluate each classifier
for name, clf in classifiers.items():
    # Train the classifier
    clf.fit(X_resampled, y_resampled)

    # Predict the classes
    y_pred = clf.predict(X_resampled)

    # Calculate accuracy
    accuracy = accuracy_score(y_resampled, y_pred)

    # Calculate F1 score
    f1 = f1_score(y_resampled, y_pred, average='weighted')

    # Calculate probabilities for ROC curve (only for classifiers supporting probability estimates)
    if hasattr(clf, 'predict_proba'):
        y_prob = clf.predict_proba(X_resampled)
        # Calculate ROC curve and AUC score for each class separately (OvR strategy)
        fpr = dict()
        tpr = dict()
        auc = dict()
        for i in range(len(clf.classes_)):
            fpr[i], tpr[i], _ = roc_curve(y_resampled == clf.classes_[i], y_prob[:, i])
            auc[i] = roc_auc_score(y_resampled == clf.classes_[i], y_prob[:, i])

        # Plot ROC curve for each class
        plt.figure()
        for i in range(len(clf.classes_)):
            plt.plot(fpr[i], tpr[i], label='ROC curve (area = %0.2f) for class %s' % (auc[i], clf.classes_[i]))
        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curve - ' + name)
        plt.legend(loc="lower right")
        plt.show()
    else:
        print("ROC curve and AUC score are not available for", name)

    # Print results
    print("Classifier:", name)
    print("Accuracy:", accuracy)
    print("F1 Score:", f1)
    print()

classifier = RandomForestClassifier()

cv_scores = cross_val_score(classifier, X_resampled, y_resampled, cv=5, scoring='accuracy')

print("Cross-Validation Scores:", cv_scores)
print("Mean CV Accuracy:", np.mean(cv_scores))