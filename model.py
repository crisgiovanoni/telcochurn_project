import numpy as np
import wrangle # remove later
import prep # remove later

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# df = wrangle.get_sql_telco() # remove later
# df.head()

# df.info()

# df["enc_churn"] = df.churn.apply(prep.yes_no_to_boolean)
# y = df.enc_churn
# X = df[["senior_citizen","tenure","internet_service_type_id"]]
# X.head()

# clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=123)
# clf = clf.fit(X,y)
# yhat = clf.predict(X)

# yhat_proba = clf.predict_proba(X)
# yhat_proba

def model_by_cart(X,y,algorithm='entropy',depth=3):
    clf = DecisionTreeClassifier(criterion=algorithm, max_depth=int(depth), random_state=123)
    clf = clf.fit(X,y)
    yhat = clf.predict(X)
    yhat_proba = clf.predict_proba(X)
    return yhat, yhat_proba, clf
    