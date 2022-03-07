from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
print("Starting process Stemming.....")
factory = StemmerFactory()
stemmer = factory.create_stemmer()

fo = open("C:/Users/Furqan Nazuli/Documents/[DOC] UNSRI/KELAS 1 REG C/SMT.6/[Pilihan] Pemrosesan Bahasa Alami/Tugas 2-Stemming/20.txt", "r", encoding='utf8', errors='ignore')
teks = fo.read()
fo.close()

teks_stem = stemmer.stem(teks)
fw = open("C:/Users/Furqan Nazuli/Documents/Hasil20.txt", "w")
fw.writelines(teks_stem)
fw.close()
print ("Done !!")
