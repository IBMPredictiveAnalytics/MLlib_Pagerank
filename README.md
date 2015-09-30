# MLlib-PageRank
The scenario here is to perform analysis on the social graph using data on email exchanges.  We use a small extract from the enron corpus (see enron.csv) listing the source and destination of e-mails.  We use the pagerank algorithm to rank enron employees where an email from person A to person B is seen as A in some way endorsing B. Estimating the relative importance of individuals within a social network is a key step for a number of applications including fraud investigation and
marketing.

PageRank measure the importance of each vertex in a graph, assuming an edge from u to v represents an endorsement of v's importance by u. 


![Map](https://raw.githubusercontent.com/IBMPredictiveAnalytics/MLlib-Pagerank/master/Screenshot/Illustration1.png)
 
 - Learn more about [Spark GraphX][25]
 - Learn more about [PageRank Algorithm][26]

---
Requirements
----
- IBM SPSS Modeler v17.1
- IBM SPSS Analytic Server 2.1

More information here: [IBM Predictive Extensions][2]

---
Installation instructions
----
1. Download the extension: [Download][3] 
2. Close IBM SPSS Modeler. Save the .cfe file in the CDB directory, located by default on Windows in "C:\ProgramData\IBM\SPSS\Modeler\17.1\CDB" or under your IBM SPSS Modeler installation directory.
3. Restart IBM SPSS Modeler, the node will now appear in the Model palette.


---
License
----

[Apache 2.0][1]


Contributors
----
 -  Nial McCarrol
- Armand Ruiz ([armand_ruiz](https://twitter.com/armand_ruiz))


[1]: http://www.apache.org/licenses/LICENSE-2.0.html
[2]:https://developer.ibm.com/predictiveanalytics/downloads/#tab2
[3]:https://github.com/IBMPredictiveAnalytics/MLlib-Pagerank/raw/master/Source%20code/SparkPageRank.cfe
[4]:https://cran.r-project.org/web/packages/RCurl/
[5]:https://github.com/IBMPredictiveAnalytics/Get-Coordinates-Esri/raw/master/Documentation/Geocoding-SPSSModelerExtension.pdf
[6]:https://github.com/IBMPredictiveAnalytics/Get-Coordinates-Esri/tree/master/Example
[10]:https://developer.ibm.com/predictiveanalytics/2015/03/11/tweets-during-esri-dev-summit-and-bnp-paribas-open/

[25]:https://spark.apache.org/docs/1.1.0/graphx-programming-guide.html
[26]:https://spark.apache.org/docs/1.1.0/graphx-programming-guide.html#pagerank

