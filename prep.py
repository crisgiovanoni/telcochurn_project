import pandas as pd
import wrangle
from sklearn.preprocessing import LabelEncoder

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
    