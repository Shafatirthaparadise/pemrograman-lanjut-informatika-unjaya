
print("Profil Mahasiswa UNJANI Yogyakarta")

def mahasiswa(nama,nim,prodi,hobby):

    print("Nama  : {}".format (nama))
    print("NIM   : {}".format (nim))
    print("Prodi : {}".format (prodi))
    print("Hobby : {}".format (hobby))

pelajar = {'nama':"Shafa tirtha paradise", 'nim':"232102003", 'prodi':"informatika",'hobby':"nangis"}
mahasiswa(**pelajar)
print("Terimakasih...")

