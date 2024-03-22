def toko_buah(buah,*args):

    print ("Toko Buah Koprasi UNJANI Yokyakarta")
    print ("Masukkan banyaknya buah yang dibeli: {}".format (buah))
    for indeks, arg in enumerate(args):
        print("Buah {} : {}".format (indeks+1, arg))

toko_buah(4,"apel","semangka","jeruk","anggur")

