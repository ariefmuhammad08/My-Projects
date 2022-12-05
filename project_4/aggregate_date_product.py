from mrjob.job import MRJob
import psycopg2 as pg

# agregat quantity berdasarkan year dan productid
class AggregateQuantity(MRJob):
    def mapper(self, _, line):
        item= line.strip().split(',')
        year= item[1][-4:]
        yield (year, item[3]),int(item[4])   
        
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    AggregateQuantity.run()