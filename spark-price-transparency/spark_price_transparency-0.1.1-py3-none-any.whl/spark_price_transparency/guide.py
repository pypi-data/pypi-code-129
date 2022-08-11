from pyspark.sql.session import SparkSession

class Guide():

    spark: SparkSession
    Writer: None
    Reader: None
    Schema: None

    def __init__(self, spark):
        self.spark = spark
        self.x = 10
