def ogrenci_yazdir():
    isim = input("öğrencinin isim soy isimini giriniz: ")
    vize = int(input("vize notunu girin:"))
    final = int(input("final notunu giriniz:"))
    basari_notu = vize * 0.4 + final * 0.6
    harf_notu = ""
    if basari_notu >= 85:
        harf_notu = "AA"

    elif basari_notu >= 70:
        harf_notu = "BA"

    elif basari_notu >= 60:
        harf_notu = "BB"

    elif basari_notu >= 50:
        harf_notu = "CB"

    elif basari_notu >= 40:
        harf_notu = "CC"

    else:
        harf_notu = "FF"


    print("Basari notu:{}".format(basari_notu))
    print("{} adli ogrencinin ,bu derste elde ettigi {} harf notu".format(isim, harf_notu))

    with open("notlar.txt", "a") as dosya:
        dosya.writelines(
            "{} adli ogrencinin; basari notu:{} ve bu derste elde ettigi harf notu:{}\n".format(isim, basari_notu,
                                                                                                harf_notu))


kac_ogrenci=int(input("Kaç öğrenci gireceksiniz?"))
for i in range(kac_ogrenci):
   ogrenci_yazdir()