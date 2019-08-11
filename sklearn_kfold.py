from sklearn.model_selection import KFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

kfold = KFold(n_splits=10, shuffle=True)
train_test_indices = kfold.split(documents)

kfold_acc = []
for train_idx, test_idx in train_test_indices:
	train_doc = documents[train_idx]
	train_label = labels[train_idx]
	test_doc = documents[test_idx]
	test_label = labels[test_idx]

	clf = MultinomialNB()
	clf.fit(train_doc, train_label)

	test_pred = clf.predict(test_doc)

	acc = accuracy_score(test_pred, test_label)
	kfold_acc.append(acc)

print("Average Accuracy: {}".format(np.mean(kfold_acc)))
print("Std Dev: {}".format(np.std(kfold_acc)))