from sklearn.datasets import make_blobs
import pandas as pd
import sys
import matplotlib.pyplot as plt
import os
import psycopg2 as pg
import psycopg2.extras as extras

param_dic = {
    "host"      : "localhost",
    "database"  : "K-means",
    "user"      : "postgres",
    "password"  : "911"

}




def execute_many(conn, df, table):
    """
    Using cursor.executemany() to insert the dataframe
    """
    # Create a list of tupples from the dataframe values
    tuples = [tuple(x) for x in df.to_numpy()]
    # Comma-separated dataframe columns
    cols = ','.join(list(df.columns))
    # SQL quert to execute
    query  = "INSERT INTO %s(%s) VALUES(%%s,%%s)" % (table, cols)
    cursor = conn.cursor()
    try:
        cursor.executemany(query, tuples)
        conn.commit()
    except (Exception, pg.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_many() done")
    cursor.close()

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


features, target = make_blobs(n_samples = 80,
                  # two feature variables,
                  n_features = 2,
                  # four clusters,
                  centers = 3,
                  # with 3.5 cluster standard deviation,
                  cluster_std =10,
                  # shuffled,
                  shuffle = True)

print(pd.DataFrame({'x1': features[:, 0], 'x2': features[:, 1]}))

dataset = pd.DataFrame({'x1': features[:, 0], 'x2': features[:, 1]})

print(type(features))
conn = connect(param_dic)


execute_many(conn,dataset, 'coordinates.km_data')

