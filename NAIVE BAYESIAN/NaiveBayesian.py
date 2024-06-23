import pandas as pd
from collections import defaultdict

# Load Data from CSV
data = pd.read_csv('PlayTennis.csv')

# Obtain features (X) and target variable (y)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Calculate P(A) - Probability of each class
conceptProbs = y.value_counts(normalize=True).to_dict()
countConcept = y.value_counts().to_dict()
print("\nP(A) : ", conceptProbs, "\n")

# Calculate P(X/A) - Conditional probabilities and P(X) - Marginal probabilities
AttrConcept = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
probability_list = defaultdict(lambda: defaultdict(float))

for column in X.columns:
    for val in X[column].unique():
        for c in y.unique():
            count = len(data[(X[column] == val) & (y == c)])
            AttrConcept[column][val][c] = count / countConcept[c]
        probability_list[column][val] = len(data[X[column] == val]) / len(data)

print("P(X/A) : ", dict(AttrConcept), "\n")
print("P(X) : ", dict(probability_list), "\n")

# Test function
def test(examples, X, conceptProbs, AttrConcept, probability_list):
    misclassification_count = 0
    for ex in examples:
        px = {c: conceptProbs[c] for c in conceptProbs}
        for c in px:
            for col, val in zip(X.columns, ex[:-1]):
                if val in AttrConcept[col]:
                    px[c] *= AttrConcept[col][val][c] / probability_list[col][val]
        
        print(px)
        classification = max(px, key=px.get)
        print("Classification :", classification, "Expected :", ex[-1])
        if classification != ex[-1]:
            misclassification_count += 1
    misclassification_rate = misclassification_count * 100 / len(examples)
    accuracy = 100 - misclassification_rate
    print("Misclassification Count={}".format(misclassification_count))
    print("Misclassification Rate={}%".format(misclassification_rate))
    print("Accuracy={}%".format(accuracy))

# Convert DataFrame to numpy array for testing
examples = data.values
test(examples, X, conceptProbs, AttrConcept, probability_list)