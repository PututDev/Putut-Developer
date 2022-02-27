#Program Kalkulator Python
#Copyright @ 2020 by Putut Dev

print ("Created By Putut Dev")


print("====== Silahkan pilih menu =======")

print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Pembagian")
print("4.perkalian")

p = int(input("Masukan Nomor pilihan menu 1/2/3/4:"))
bp = int(input("Masukan bilangan pertama :"))
bk = int(input("Masukan bilangan kedua :"))

if p ==1:
   tambah = bp+bk
   print(bp,"+",bk,"=",tambah)

elif p ==2:
       kurang= bp-bk
       print(bp,"-",bk,"=",kurang)
    
elif p ==3:
      bagi = bp/bk
      print(bp,"/",bk,"=",bagi)
        
elif p ==4:
      kali = bp*bk
      print(bp,"*",bk,"=",kali)







