from sklearn.model_selection import train_test_split, GridSearchCV
from skimage.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

x_train, x_tset, y_train, y_test = train_test_split(X, y)


vectorizer = TfidfVectorizer()
clf = MultinomialNB()
pipeline = Pipeline([
		('vect', vectorizer),
		('clf', clf)])

parameters = {
	"vect__max_features":(5000, None),
	"vect__ngram_range":((1,1), (1,2)),
	"vect__use_idf":(True, False),
	"vect__smooth_idf":(True, False),
	"vect__sublinear_tf":(True, False),
	"vect__norm":("11","12",None),
	"clf__alpha":(1.0, 2.0)
}

grid_search = GridSearchCV(pipeline, parameters,
							scoring='accuracy', cv=3,
							n_jobs=-1, verbose=1)

grid_search.fit(x_train, y_train)
best_param = grid_search.best_estimator_.get_params()
print(best_param)


print('Accuracy: {}'.format(accuracy_score(x_test, y_test)))