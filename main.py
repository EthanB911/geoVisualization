"""
Simple demo of a scatter plot.
"""
import numpy as np
import psycopg2 as pg
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pandas.io.sql as psql

# engine = create_engine('postgresql+psycopg2://postgres:911@localhot/K-means')
# engine = create_engine('postgresql://user@localhost:5432/mydb')

connection = pg.connect("host=localhost dbname=K-means user=postgres password=911 ")
dist = psql.read_sql('set search_path = "coordinates";SELECT Distinct(cluster_id) FROM coordinates.km_data ', connection)
psql.execute('set search_path = "coordinates";Call coordinates.kmeans2(2)', connection)
dist = psql.read_sql('set search_path = "coordinates";SELECT Distinct(cluster_id) FROM coordinates.km_data ', connection)
first = dist['cluster_id'].iloc[0]
second = dist['cluster_id'].iloc[1]
dataframe24 = psql.read_sql('set search_path = "coordinates";SELECT x1, x2 FROM coordinates.km_data where cluster_id='+ str(first), connection)
dataframe23 = psql.read_sql('set search_path = "coordinates";SELECT x1, x2 FROM coordinates.km_data where cluster_id='+ str(second), connection)
clusterCenter1 = psql.read_sql('set search_path = "coordinates";SELECT x1, x2 FROM coordinates.km_clusters ORDER BY id desc limit 1' , connection)
clusterCenter2 = psql.read_sql('set search_path = "coordinates";SELECT x1, x2 FROM coordinates.km_clusters ORDER BY id ASC limit 1' , connection)
x1 = dataframe24[['x1']]
x2 = dataframe24[['x2']]
xx1 = dataframe23[['x1']]
xx2 = dataframe23[['x2']]

print(dist['cluster_id'].iloc[0])
print(clusterCenter1)
print(clusterCenter2)
plt.scatter(x1, x2, color='red')
plt.scatter(xx1, xx2, color='blue')
plt.scatter(clusterCenter1[['x1']], clusterCenter1[['x2']], color='black')
plt.scatter(clusterCenter2[['x1']], clusterCenter2[['x2']], color='black')

plt.show()