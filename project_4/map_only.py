from mrjob.job import MRJob
import psycopg2 as pg


class FilterProduct(MRJob):
    # koneksi ke postgres
    def mapper_init(self):
        self.conn= pg.connect(database='postgres', user='postgres', password='postgres', host='localhost', port='5432')

    # map produk yang memeliki price diatas 10
    def mapper(self, _, line):
        self.cur= self.conn.cursor()
        item= line.strip().split(',')
        if int(item[3])> 10:
            self.cur.execute('insert into product (product_id, product_name, product_category, price) values(%s,%s,%s,%s)', (item[0],item[1],item[2],item[3]))

    # input hasil map ke database
    def mapper_final(self):
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    FilterProduct.run()