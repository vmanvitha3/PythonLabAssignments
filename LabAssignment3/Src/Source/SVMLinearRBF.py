#Importing the libraries
from sklearn import datasets
from sklearn import svm

#Load iris dataset

iris = datasets.load_iris()
X = iris.data
y = iris.target

#Splitting the dataset into training (80%) and testing set(20%)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=3)

#Using Linear Kernel

print("***************************************************************")
print("                       SVM using linear kernel")
print("***************************************************************")
clf_linear = svm.SVC(kernel='linear')
clf_linear.fit(X_train, y_train)
y_pred_linear = clf_linear.predict(X_test)

#Printing confusion matrix and accuracy score
from sklearn.metrics import confusion_matrix,accuracy_score
cmatrix_linear = confusion_matrix(y_test,y_pred_linear)
print("Confusion Matrix:\n",cmatrix_linear)
accScore_linear = accuracy_score(y_test,y_pred_linear)
print("Accuracy of Linear Model is ",accScore_linear,"%")

#Using 'rbf' kernel
print("***************************************************************")
print("                       SVM using rbf kernel")
print("***************************************************************")

rbf_model = svm.SVC(kernel='rbf')
rbf_model.fit(X_train, y_train)
y_pred_rbf = rbf_model.predict(X_test)

#Printing confusion matrix and accuracy score
from sklearn.metrics import confusion_matrix,accuracy_score
cmatrix_rbf = confusion_matrix(y_test,y_pred_rbf)
print("Confusion Matrix:\n",cmatrix_rbf)
accScore_rbf = accuracy_score(y_test,y_pred_rbf)
print("Accuracy of rbf Model is ",accScore_rbf,"%")
print("***************************************************************")

#Check which model is better
if accScore_linear<accScore_rbf:
    print("rbf is a better model")
elif accScore_linear>accScore_rbf:
    print("Linear is a better model")
else:
    print("Both has same accuracy. You can choose any model")