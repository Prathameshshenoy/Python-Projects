#pip install 'scikit-learn' to use this code

#importing
from sklearn import datasets
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split as tts
wine = datasets.load_wine()
features = wine.data
labels = wine.target
train_feats, test_feats, train_labels, test_labels = tts(features, labels, test_size=0.2)

#classifier 
clf =RandomForestClassifier()

#training section:
clf.fit(train_feats,train_labels)

#predictions:
predictions = clf.predict(test_feats)
print(predictions)

score = 0
s = 0
for i in range(len(predictions)):
    if predictions[i] == test_labels[i]:
        score+= 1
    s = score * 100
print(s/ len(predictions))
