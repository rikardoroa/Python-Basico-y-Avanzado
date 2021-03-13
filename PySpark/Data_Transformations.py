# Databricks notebook source
from pyspark.sql.functions import*
from pyspark.sql import SparkSession as Sesion
import pyspark.sql as py
import pyspark.sql.types as ptypes
from IPython.display import display, HTML

# COMMAND ----------

class csv_avro_file_basic:
  
  def __init__(self, session = Sesion, order_schema = ptypes.StructType, csv_load = py.dataframe.DataFrame):
    self.session = session.builder.master("spark://192.168.56.1:7077").appName("Proyecto_Final_DataHack").getOrCreate() 
    self.order_schema = order_schema
    self.csv_load = csv_load
    
  def read_schema(self):
    self.order_schema = StructType([
    StructField("order_id",IntegerType(), True),
    StructField("order_date",DateType(), True),
    StructField("order_customer_id", IntegerType(),True),
    StructField("order_status", StringType(), True)       
    ])
    order_schema = self.order_schema 
    
  
  def show_schema(self):
    self.order_schema = order_schema
    spark = self.session
    self.csv_load = spark.read.format("csv").option("header", "true")\
    .schema(self.order_schema)\
    .option("mode", "FAILFAST")\
    .load("/FileStore/tables/part_00000.txt")
    csv_load = self.csv_load
    return csv_load.show()
  
  def write_avro_schema(self):
    csv_load = self.csv_load
    csv_load.write.format("avro").mode("overwrite").save("/FileStore/tables/part_00000.avro")
    return csv_load.show()
    

# COMMAND ----------

load_avro = csv_avro_file_basic()

# COMMAND ----------

load_avro.read_schema()

# COMMAND ----------

load_avro.show_schema()

# COMMAND ----------

load_avro.write_avro_schema()

# COMMAND ----------

display(HTML('<a href="https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/1583121630593485/2798185413299793/1330152028615219/latest.html"> Avro File Basics With Databricks </a>'))

