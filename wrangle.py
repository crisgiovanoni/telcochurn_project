
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

def get_sql_zillow():
    """
    Queries from zillow database with the following conditions:
    - Single-unit properties
    - 
    >> Input:
    database
    << Output:
    url
    """
    query = '''
    SELECT prop.parcelid, calculatedfinishedsquarefeet, bathroomcnt, bedroomcnt, transactiondate, taxvaluedollarcnt
    FROM properties_2017 as prop
    JOIN predictions_2017 as pred
	    USING(parcelid)
    JOIN propertylandusetype as usetype
	    ON prop.propertylandusetypeid = usetype.propertylandusetypeid
	    AND prop.propertylandusetypeid in (261,262,263,264,265,268,269,273,275,276)
    ''' 
    df = pd.read_sql(query, get_db_url("zillow"))
    return df