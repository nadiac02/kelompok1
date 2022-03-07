import nltk.tokenize.punkt
file = open('baru.txt', 'r')
baca = file.read()
file.close()
seg_kalimat = nltk.data.load('indonesian.pickle')
teks_kalimat = seg_kalimat.tokenize(baca)
file = open('hasil2_punkt.txt', 'w')
for kalimat in teks_kalimat:
    print(kalimat.strip())
    file.write(str(kalimat))
    file.write('\n')
file.close()
