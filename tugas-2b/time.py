from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import time
print("Starting process Stemming.....")
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def convert_seconds(seconds):
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    return days, hours, minutes, seconds

fo = open("C:/Users/Furqan Nazuli/Documents/[DOC] UNSRI/KELAS 1 REG C/SMT.6/[Pilihan] Pemrosesan Bahasa Alami/Tugas 2-Stemming/80.txt", "r", encoding='utf8', errors='ignore')
teks = fo.read()
start = time.time()

teks_stem = stemmer.stem(teks)
waktu = convert_seconds(time.time()-start)
fo.close()
print('waktu proses: {:.0f}:{:.0f}:{:.0f}'.format(waktu[1], waktu[2], waktu[3]))
