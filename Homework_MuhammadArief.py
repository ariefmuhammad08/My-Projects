class Hewan:
    nama_latin='hewan'

    def __init__(self,nama,umur):
        self.nama=nama
        self.umur=umur

    def bangun(self):
        return 'bangun'

    @classmethod
    def change_nama_latin(cls,namabaru):
        cls.nama_latin=namabaru

class Kucing(Hewan):

    def __init__(self,nama,umur):
        super().__init__(nama, umur)
        super().change_nama_latin('felis catus')
    
    def bangun(self):
        return 'meow'
       
    def lari(self,kec):
        if kec>10 :
            return 'cepat sekali'
        else :
            return 'lambat'

#contoh
a=Kucing('simba',5)
print(f'{a.nama} ({a.nama_latin}) umurnya {a.umur} tahun')
print(a.bangun())
print(a.lari(12))