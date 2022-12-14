import findspark
findspark.init()
from pyspark.sql import SparkSession

# initiate spark
spark = SparkSession \
        .builder \
        .master('local[*]') \
        .appName('dump') \
        .getOrCreate()

# load mysql to dataframe
trainDF = spark.read.format('jdbc').options(
                                    driver='com.mysql.cj.jdbc.Driver',
                                    user='root',
                                    password='mysql',
                                    url='jdbc:mysql://localhost:3306/digitalskola',
                                    dbtable='application_train'
                                    ).load()

testDF = spark.read.format('jdbc').options(
                                    driver='com.mysql.cj.jdbc.Driver',
                                    user='root',
                                    password='mysql',
                                    url='jdbc:mysql://localhost:3306/digitalskola',
                                    dbtable='application_test'
                                    ).load()

# save dataframe to postrges
trainDF.write.mode('ignore').format('jdbc').options(
                                    driver='org.postgresql.Driver',
                                    user='postgres',
                                    password='postgres',
                                    url='jdbc:postgresql://localhost:5432/postgres',
                                    dbtable='application_train'
                                    ).save()

testDF.write.mode('ignore').format('jdbc').options(
                                    driver='org.postgresql.Driver',
                                    user='postgres',
                                    password='postgres',
                                    url='jdbc:postgresql://localhost:5432/postgres',
                                    dbtable='application_test'
                                    ).save()    