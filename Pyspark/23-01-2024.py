# Read CSV file with options - schema
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
path="dbfs:/temp_test_csv"
schema=StructType([
    StructField("Name",StringType(),True),
    StructField("Age",IntegerType(),True),
    StructField("Occupation",StringType(),True)
])
df=spark.read.csv(path,schema=schema)


#Rename the column name
df=df.withColumnRenamed("Occupation","Occupations")



from pyspark.sql.functions import col
df=df.filter((col("Age")>25) & (col("Occupations")=="Engineer"))


#filter with AND/ OR
from pyspark.sql.functions import col
df=df.filter((col("Age")>25) & (col("Occupations")=="Engineer"))
df=df.filter((col("Age")>25) | (col("Occupation")=="Engineer"))


#add the columns as company ('Diiggibyte')
from pyspark.sql.functions import lit
df=df.withColumn("Company", lit("diggibyte"))



#cast the datatype
df.withColumn("Age",col("Age").cast("String"))