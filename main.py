def cetak_nama(nama=''):
  # Tulis kode fungsi cetak_nama di bawah ini
  
  # Jika nama sama dengan null maka 
  if nama == "":
    # Akan mencetak Tidak ada nama yang dicetak
    print('Tidak ada nama yang dicetak')
  # Jika nama tidak sama dengan null maka akan membuat fungsi perulangan
  else:
    # Variabel pNama menampung nilai panjang dari nama menggunakan fungsi len, + 1 yang artinya untuk menambah nama=pNama sebelum nama menggunakan akhiran !
    pNama = len(nama) + 1
    # Memulai dari huruf awal
    mulai = 0
    # Mulai perulangan, mulai kurang dari pNama yang artinya mulai hitung nama dari awal sampai sebelum huruf nama terakhir
    while mulai < pNama:
      # Melakukan penambahan pada setiap baris
      mulai += 1
      # Jika mulai = pNama maka
      if mulai == pNama:
        # Akan mencetak nama hingga seluruh nama dan pada baris akhir nama akan ditambah karakter !
        print (nama[0:mulai] + "!")
      else:
        # Akan mencetak nama hingga seluruh nama
        print (nama[0:mulai])

def hitung_kesamaan(kata1, kata2):
  # Tulis kode fungsi hitung_kesamaan di bawah ini
  
  # Variabel r untuk memulai dari awal kata
  r = 0
  # Memulai perulangan dari 0 sampai panjang kata1
  for i in range(0, len(kata1)):
    # Jika i lebih dari sama dengan panjang kata2 maka
    if i >= len(kata2):
      # diberhentikan
      break
    # Selain lebih dari sama dengan panjang kata2
    else:
      # Jika kata1 sama dengan kata2 yang sudah dipisahkan huruf per hurufnya maka
      if kata1[i] == kata2[i]:
        # r akan melakukan looping
        r += 1
  # Membalikan variabel r
  return r

def hitung(bil1, bil2, operator='+'):
  # Tulis kode fungsi hitung() di bawah ini
  
  #Jika operator -
  if operator == '-':
    #Maka bil1 dikurang bil2
    r = bil1 - bil2

  #Jika operator *
  elif operator == '*':
    #Maka bil1 dikali bil2
    r = bil1 * bil2

  # Jika tidak ada parameter operator
  else:
    #Maka secara default bil1 ditambah bil2
    r = bil1 + bil2
    
  return r
  #Membalikan nilai



# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya
# (untuk fungsi hitung_kesamaan() dan fungsi hitung()).
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  print("Hasil cetak_nama('Mawar'):")
  cetak_nama("Mawar")
  print()
  print("Hasil cetak_nama(''):")
  cetak_nama("")
  print()
  r = hitung_kesamaan('python', 'path')
  print(f"hitung_kesamaan('python', 'path') = {r} \t(solusi: 3)")
  r = hitung_kesamaan('masak', 'cuci')
  print(f"hitung_kesamaan('masak', 'cuci') = {r} \t(solusi: 0)")
  r = hitung_kesamaan('python', '')
  print(f"hitung_kesamaan('python', '') = {r} \t\t(solusi: 0)")
  print()
  r = hitung(4, 8)
  print(f'hitung(4, 8) = {r} \t\t(solusi: 12)')
  r = hitung(4, 8, '-')
  print(f"hitung(4, 8, '-') = {r} \t(solusi: -4)")
  r = hitung(4, 8, '*')
  print(f"hitung(4, 8, '*') = {r} \t(solusi: 32)")

if __name__ == '__main__':
  test()