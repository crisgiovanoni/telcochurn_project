import pandas as pd
import wrangle
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

# df = get_sql_telco()
# df.head()

# churn = df[["churn"]]
# churn.head()

# a = churn

# le = LabelEncoder()
# encoded = le.fit_transform(churn)
# encoded = pd.DataFrame(encoded, columns=f"enc.{a}")

# encoded.head()

# x = pd.Series(churn.churn == "Yes")
# x.sum()

# encoded.sum() # no. of Yes, churned

def int_encode(df):
    le = LabelEncoder()
    encoded = le.fit_transform(df)
    encoded = pd.DataFrame(encoded)
    return encoded

def yes_no_to_boolean(x):
    """
    0 = No (Stayed), 1 = Yes (Churned)
    """
    return 1 if x == "Yes" else 0

def order_encode(df,category_list):
    enc = OrdinalEncoder(categories=[category_list],dtype=int)
    enc = enc.fit(df)
    enc = enc.transform(df)
    return enc

# ser = df[["multiple_lines"]]
# # type(ser)
# enc = OrdinalEncoder(categories=[["No phone service","No","Yes"]],dtype=int)
# enc.fit(ser)
# df["phone_service"] = enc.transform(ser)
# df.head(20)

# >>> from sklearn.preprocessing import OrdinalEncoder
# >>> enc = OrdinalEncoder()
# >>> X = [['Male', 1], ['Female', 3], ['Female', 2]]
# >>> enc.fit(X)
# ... 
# OrdinalEncoder(categories='auto', dtype=<... 'numpy.float64'>)
# >>> enc.categories_
# [array(['Female', 'Male'], dtype=object), array([1, 2, 3], dtype=object)]
# >>> enc.transform([['Female', 3], ['Male', 1]])
# array([[0., 2.],
#        [1., 0.]])