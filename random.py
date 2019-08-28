import random

# To create random address


fnames = ['lalu','manu','akhil','nikhil','miras','nihal']
lnames = ['pari','ummanath','vadakke_veettil','thamburan','namboothirippad']

fseries =9895

for i in range(50):


    fname = random.choice(fnames) +" "+  random.choice(lnames)
    phon = random.randint(100000,999999)
    phone = '{}-{} '.format(fseries,phon)
    Email = '{}@gmail.com'.format(fname)
    print(f'{fname} \n{phone} \n{Email}')





