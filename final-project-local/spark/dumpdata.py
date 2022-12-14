import findspark
findspark.init()
from pyspark.sql import SparkSession 

# initiate spark
spark = SparkSession \
        .builder \
        .master('local[*]') \
        .appName('dump') \
        .getOrCreate()

# read data
trainDF = spark.read. \
  format('csv'). \
  option('inferSchema','true'). \
  option('header','true'). \
  load('/e/final-project-local/spark/dataset/application_train.csv')

testDF = spark.read. \
  format('csv'). \
  option('inferSchema','true'). \
  option('header','true'). \
  load('/e/final-project-local/spark/dataset/application_test.csv')

#insert data to mysql
trainDF.write.mode('ignore').format('jdbc').options(
                                    driver='com.mysql.cj.jdbc.Driver',
                                    user='root',
                                    password='mysql',
                                    url='jdbc:mysql://localhost:3306/digitalskola',
                                    dbtable='application_train'
                                    ).save()

testDF.write.mode('ignore').format('jdbc').options(
                                    driver='com.mysql.cj.jdbc.Driver',
                                    user='root',
                                    password='mysql',
                                    url='jdbc:mysql://localhost:3306/digitalskola',
                                    dbtable='application_test'
                                    ).save()