import sys
from sklearn.datasets import make_blobs
import pandas as pd
import dataframe as dataframe
import numpy as np
import psycopg2 as pg
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pandas.io.sql as psql
from pandas import DataFrame

param_dic = {
    "host"      : "localhost",
    "database"  : "K-means",
    "user"      : "postgres",
    "password"  : "911"

}

# connection = pg.connect("host=localhost dbname=K-means user=postgres password=911 "

import pandas as pd

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = pg.connect(**params_dic)

    except (Exception, pg.DatabaseError) as error:
        print(error)
        sys.exit(1)
    return conn


def single_insert(conn, insert_req):
    """ Execute a single INSERT request """
    cursor = conn.cursor()
    try:
        cursor.execute(insert_req)
        conn.commit()
    except (Exception, pg.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()


# Connecting to the database
conn = connect(param_dic)
Data = {'x1': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
        'x2': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]}

# df = DataFrame(Data,columns=['x1','x2'])
# data = pd.read_csv ('/Users/ethanb/Downloads/1909_3300_bundle_archive/NYPD_Complaint_Data_Historic.csv')
df = pd.DataFrame(Data, columns= ['x1','x2'])
# Inserting each row
print(df['x1'][0])
print(df['x2'][0])
for i in df.index:

                query = """
                INSERT into coordinates.km_data(x1, x2) values(%s,%s);
                """ % (df['x1'][i],df['x2'][i])
                # print(query)
                single_insert(conn, query)



# features, target = make_blobs(n_samples = 1000000,
#                   # two feature variables,
#                   n_features = 2,
#                   # four clusters,
#                   centers = 4,
#                   # with .65 cluster standard deviation,
#                   cluster_std = 3.5,
#                   # shuffled,
#                   shuffle = True)
#
# print(type(features))
#
# dataset = pd.DataFrame({'x1': features[:, 0], 'x2': features[:, 1]})
# for i in dataset.index:
#
#                 query = """
#                 INSERT into coordinates.km_data2(x1, x2) values(%s,%s);
#                 """ % (dataset['x1'][i],dataset['x2'][i])
#                 single_insert(conn, query)
#                 # print(query)
#
#
# print(dataset)
# dataset.to_sql('km_data',conn, index=False, if_exists="append", schema="coordinates")
# cursor = conn.cursor()
# for row in df.itertuples():
#     cursor.execute('''
#                 INSERT INTO coordinates.km_data(x1, x2)
#                 VALUES (?,?)
#                 ''',
#                 row.Latitude,
#                 row.Longitude
#                 )
# conn.commit()

# Close the connection
conn.close()


