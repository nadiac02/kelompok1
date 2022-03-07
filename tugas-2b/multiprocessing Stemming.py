from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import multiprocessing as mp


factory = StemmerFactory()
stemmer = factory.create_stemmer()

def test(kalimat) :
    stemmer.stem(kalimat)

if __name__=='__main__' :

    f = open(f"C:/Users/Furqan Nazuli/Documents/[DOC] UNSRI/KELAS 1 REG C/SMT.6/[Pilihan] Pemrosesan Bahasa Alami/Tugas 2-Stemming/40.txt", "r", encoding='utf8')
    teks = f.read()
    f.close()
    split = teks.split(".")

    x = ""
    y = ""
    z = ""

    for i in range(len(split)) :
        if i < (len(z)/3) :
            x += split[i]
        elif i >= (len(z)/3) and i<((len(z)/3)+((len(z)/3)-1)) :
            y += split[i]
        elif i >= ((len(z)/3)+((len(z)/3)-1)) :
            z += split[i]

    p1 = mp.Process(target=test, args=(x,))
    p2 = mp.Process(target=test, args=(y,))
    p3 = mp.Process(target=test, args=(z,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print(i)