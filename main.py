"""
Simple demo of a scatter plot.
"""
import numpy as np
import psycopg2 as pg
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pandas.io.sql as psql
from pandas import DataFrame
from sklearn.cluster import KMeans


# engine = create_engine('postgresql+psycopg2://postgres:911@localhot/K-means')
# engine = create_engine('postgresql://user@localhost:5432/mydb')

connection = pg.connect("host=localhost dbname=K-means user=postgres password=911 ")
dist = psql.read_sql('set search_path = "coordinates";SELECT Distinct(cluster_id) FROM coordinates.km_data ', connection)
psql.execute('set search_path = "coordinates";Call coordinates.kmeans(6)', connection)
# dist = psql.read_sql('set search_path = "coordinates";SELECT Distinct(cluster_id) FROM coordinates.km_data ', connection)
# first = dist['cluster_id'].iloc[0]
# second = dist['cluster_id'].iloc[1]
# third = dist['cluster_id'].iloc[2]
# dataframe24 = psql.read_sql('set search_path = "coordinates";SELECT x1, x2 FROM coordinates.km_data where cluster_id='+ str(first), connection)
# dataframe23 = psql.read_sql('set search_path = "coordinates";SELECT x1, x2 FROM coordinates.km_data where cluster_id='+ str(second), connection)
# dataframe25 = psql.read_sql('set search_path = "coordinates";SELECT x1, x2 FROM coordinates.km_data where cluster_id='+ str(third), connection)
# clusterCenter1 = psql.read_sql('set search_path = "coordinates";SELECT x1, x2 FROM coordinates.km_clusters where id=' + str(first) , connection)
# clusterCenter2 = psql.read_sql('set search_path = "coordinates";SELECT x1, x2 FROM coordinates.km_clusters where id=' + str(second) , connection)
# clusterCenter3 = psql.read_sql('set search_path = "coordinates";SELECT x1, x2 FROM coordinates.km_clusters where id=' + str(third) , connection)
centres = psql.read_sql('set search_path = "coordinates";SELECT x1, x2 FROM coordinates.km_clusters ', connection)
km_data = psql.read_sql('set search_path = "coordinates";SELECT x1, x2 FROM coordinates.km_data', connection)
# x1 = dataframe24[['x1']]
# x2 = dataframe24[['x2']]
# xx1 = dataframe23[['x1']]
# xx2 = dataframe23[['x2']]
# xxx1 = dataframe25[['x1']]
# xxx2 = dataframe25[['x2']]
#
# print(dist['cluster_id'].iloc[0])
# print(clusterCenter1)
# print(clusterCenter2)
# plt.scatter(x1, x2, color='red')
# plt.scatter(xx1, xx2, color='blue')
# plt.scatter(xxx1, xxx2, color='yellow')
# plt.scatter(clusterCenter1[['x1']], clusterCenter1[['x2']], color='black')
# plt.scatter(clusterCenter2[['x1']], clusterCenter2[['x2']], color='black')
# plt.scatter(clusterCenter3[['x1']], clusterCenter3[['x2']], color='black')

from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


cnt = []
current = []
dfcentres = DataFrame(centres, columns=['x1', 'x2'])
# df = DataFrame(Data, columns=['x', 'y'])
for i in dfcentres.index:
    current.extend([dfcentres['x1'][i] , dfcentres['x2'][i]])
    cnt.append(current)
    current = []



nparr = np.array(cnt)
print(nparr)
# print(centroids)
df = DataFrame(km_data,columns=['x1','x2'])
kmeans = KMeans(n_clusters=3).fit(df)
print(df)
plt.scatter(df['x1'], df['x2'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(nparr[:, 0], nparr[:, 1], c='red', s=50)


plt.show()