# Установка требуемых модулей
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, lit, row_number, rank
#from pyspark.sql.window import Window
from pyspark.sql import functions as F

# Установка сессии spark
spark = SparkSession.builder.appName('RateOdd').getOrCreate()

# Объявляем поток чтения из RATE источника
df_input = spark.readStream.format("rate").option("rowsPerSecond", 3).load()

# Объявляем поток записи
odd_sum_query = df_input \
    .filter(col('value') % 2 != 0) \
    .groupBy(F.window("timestamp", "1 seconds")) \
    .sum('value') \
    .withColumnRenamed('sum(value)', 'sum_odd') \
    .writeStream \
    .outputMode("update") \
    .queryName("aggregates") \
    .format("memory") \
 \
    # Запускаем поток
odd_sum_query.start().awaitTermination(15)

spark.sql("select * from aggregates").show(50, truncate=False)

spark.stop()
