from datetime import date

nama_lengkap= str(input('Masukan nama lengkap: '))
nama_panggilan= str(input('Masukan nama panggilan: '))
npm = int(input('Masukan Nomor Pokok Mahasiswa : '))
tl = str(input('Masukan tempat lahir : '))
tgl = int(input('Masukan tanggal lahir : '))
tlp = int(input('Masukan nomor telepon : '))
alamat = str(input('Masukan alamat : '))
umur = 20

print('Assalamualaikum')
print('My Name is ', nama_lengkap, ',but you can call me', nama_panggilan,'. My NPM is', npm, '.\nI was born in',tl, 'and i am',umur, 'years old.\nI am very glad if you want to invite my house in', alamat, '. \nSo, dont forget to call me before with number', tlp,)
print('Thank you.')