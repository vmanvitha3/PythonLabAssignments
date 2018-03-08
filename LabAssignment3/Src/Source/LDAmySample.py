import matplotlib.pyplot as plt

from sklearn import datasets

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

#Importing the dataset

digits = datasets.load_digits()

X = digits.data
y = digits.target
target_names = digits.target_names

# print("X:\n",X)
# print("Y:\n",y)

#Splitting the dataset into training and testing set

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

#Applying LDA
lda = LinearDiscriminantAnalysis(n_components=9)
X_train = lda.fit_transform(X_train,y_train)
X_test = lda.transform(X_test)

#Fitting logistic regression to the training set

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)

#Predicting the test set results

y_predmodel = classifier.predict(X_test)

#Making the confusion matrix

from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y_test,y_predmodel)
print("Confusion Matrix:\n",cm)

#Finding Accuracy Score
print("Accuracy Score: ")
print(accuracy_score(y_test,y_predmodel))

plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2


#Visualizing test results
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_test[y_predmodel == i, 0], X_test[y_predmodel == i, 1], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of Digits dataset')

plt.show()