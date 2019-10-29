import pandas as pd
import numpy as np 
import env

from sklearn.model_selection import train_test_split

# ACQUIRING DATA
def get_db_url(db):
    """
    Produces a url from env credentials
    >> Input:
    database
    << Output:
    url
    """
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'

def get_sql_telco():
    """
    Queries from telco database.
    """
    query = '''
    SELECT *
    FROM customers
    ''' 
    df = pd.read_sql(query, get_db_url("telco_churn"))
    return df

def remove_whitespaces(df):
    """
    Removes all white spaces in each observation of each "object" type column
    """
    dlist = df.columns
    for col in dlist:
        if df[col].dtype == "object":
            df[col] = df[col].str.strip()
    return df

# def split_my_data(X, y, train_ratio=0.7):
#     """
#     Queries from zillow database with the following specs:
#     - Fields: Parcel ID, Calculated Finished Square Footage, No. of Bathrooms, No. of Bedrooms, Last Transaction Date, Property Value
#     >> Input:
#     Data frame with X
#     Data frame with y
#     Ratio of resulting train data
#     << Output:
#     X_train
#     X_test
#     y_train
#     y_test
#     """
#     # Use when X and y data frames are available, and split train and test for modeling
#     X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_ratio, random_state=123)
#     return X_train, X_test, y_train, y_test