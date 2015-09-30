
import spss.pyspark.runtime

from pyspark.sql.types import StringType, IntegerType, DoubleType, StructField, StructType

source_field = '%%source_field%%'
dest_field = '%%dest_field%%'
iterations = %%iteration_count%%
damping = %%damping_factor%%

ascontext = spss.pyspark.runtime.getContext()

sqlCtx = ascontext.getSparkSQLContext()

out_schema = StructType([
    StructField("ID", StringType(), nullable=True),
    StructField("Rank", DoubleType(), nullable=True)
    ])

ascontext.setSparkOutputSchema(out_schema)

if not ascontext.isComputeDataModelOnly():
    df = ascontext.getSparkInputData()
    from_to = df.rdd.map(lambda x: (getattr(x,source_field),getattr(x,dest_field))).distinct() # (from,to)

    def computeContribs(urls, rank):
        num_urls = len(urls)
        for url in urls:
            yield (url, rank / num_urls)

    links = from_to.mapValues(lambda x:[x]).reduceByKey(lambda x,y: x+y) # links: (from,[to,to,to...])

    N = links.count()

    ranks = links.map(lambda (url, neighbors): (url, 1.0/float(N))) # ranks: (from,rank)

    for iteration in xrange(0,iterations):
        contribs = links.join(ranks).flatMap(
                lambda (url, (urls, rank)): computeContribs(urls, rank))  # contribs: (to, contribution_from)

        ranks = contribs.reduceByKey(lambda x,y:x+y).mapValues(lambda rank: rank * damping + (1-damping)/N)

    outdf = sqlCtx.createDataFrame(ranks,out_schema)

    ascontext.setSparkOutputData(outdf)

    

