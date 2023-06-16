#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


# In[2]:


import pandas as pd
import pyspark 
import pymongo
import numpy as np
from pyspark.sql import SparkSession
from os.path import join


# In[3]:


from pyspark.sql import SparkSession


# In[4]:


import pymongo


# In[5]:


# client = pymongo.MongoClient()


# In[6]:


from pyspark.sql.types import *


# In[7]:



spark = SparkSession     .builder     .appName("Python Spark SQL basic example")     .config("spark.jars.packages", "org.postgresql:postgresql:42.2.10")     .getOrCreate()


# In[9]:


# df = spark.read     .format("jdbc")     .option("url", "jdbc:postgresql://localhost:5434/Bank")     .option("dbtable", "account")     .option("user", "lllevchenko")     .option("password", "1234")     .option("driver", "org.postgresql.Driver")     .load()

# df.printSchema()


# In[12]:


# df = spark.read     .format("jdbc")     .option("url", "jdbc:postgresql://localhost:5434/Bank")     .option("dbtable", "calls")     .option("user", "lllevchenko")     .option("password", "1234")     .option("driver", "org.postgresql.Driver")     .load()

# df.printSchema()


# In[ 13]:

studentDf = spark.createDataFrame([
	Row(id=1,name='vijay',marks=67),
	Row(id=2,name='Ajay',marks=88),
	Row(id=3,name='jay',marks=79),
	Row(id=4,name='vinay',marks=67),
])

studentDf.select("id","name","marks").write.format("jdbc")\
    .option("url", "jdbc:postgresql://localhost:5434/Bank") \
    .option("driver", "org.postgresql.Driver").option("dbtable", "students") \
    .option("user", "lllevchenko").option("password", "1234").save()


