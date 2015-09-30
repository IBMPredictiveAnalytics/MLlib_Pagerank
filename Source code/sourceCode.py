from pyspark.context import SparkContext
from pyspark.sql.context import SQLContext

from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
import spss.pyspark.runtime
import json
import uuid

user_field = '%%user_field%%'
item_field = '%%item_field%%'
rating_field = '%%rating_field%%'
model_path =  '%%model_path%%'
rank = %%rank%%
iterations = %%iterations%%
lmbda = %%lmbda%%
blocks = %%blocks%%
random_seed = long(%%random_seed%%)

ascontext = spss.pyspark.runtime.getContext()
sc = ascontext.getSparkContext()
df = ascontext.getSparkInputData()

dummypath = ascontext.createTemporaryFolder()

def saveDummy(sc, path)
    data = sc.parallelize([json.dumps({dummyTrue})])
    data.saveAsTextFile(path)

def getIndexes(frame)
    schema = frame.dtypes[]
    indexes = {}
    for i in range(0,len(schema))
        (cname,ctype) = schema[i]
        indexes[cname] = i

    u_index = indexes[user_field]
    i_index = indexes[item_field]
    r_index = indexes[rating_field]

    return (u_index,i_index,r_index)

(user_index,item_index,rating_index) = getIndexes(df)


def metaMap(row,u_index,i_index,r_index)
    user = row[u_index]
    item = row[i_index]
    rating = row[r_index]
    s1 = set()
    s2 = set()
    s1.add(user)
    s2.add(item)
    return (s1,s2,{rating1})

def metaReduce(meta1,meta2)
    users = meta1[0].union(meta2[0])
    items = meta1[1].union(meta2[1])
    ratings = {}
    for k in meta1[2].keys()
        ratings[k] = meta1[2][k]
    for k in meta2[2].keys()
        if k not in ratings
            ratings[k] = 0
        ratings[k] += meta2[2][k]
    return (users,items,ratings)

# perform datapass to compute stats

rating_stats = df.rdd.map(lambda row metaMap(row,user_index,item_index,rating_index)).reduce(lambda x,ymetaReduce(x,y))
print(Total number of distinct items + str(len(rating_stats[1])))
print(Total number of distinct users + str(len(rating_stats[0])))

print(Rating frequencies)
ratings_range = sorted(rating_stats[2].keys())
for rating in ratings_range
    print(t+str(rating)+ +str(rating_stats[2][rating]))

ratings = df.map(lambda l Rating(int(l[user_index]), int(l[item_index]), float(l[rating_index])))

# Build the recommendation model using Alternating Least Squares

model = ALS.train(ratings, rank, iterations, lmbda, blocks, seed=random_seed)

# Save and load model
model.save(sc, model_path)
saveDummy(sc,dummypath)
ascontext.setModelContentFromPath(dummy,dummypath)





