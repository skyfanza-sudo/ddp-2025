import Bangunruang1 as br
import Bangundatar2 as bd

print("----BANGUN RUANG-----")
print(f"Volume Kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"Volume balok adalah {br.balok(3,4,5)}")
print(f"Volume Prisma SegitigA adalah {br.prisma(0.5,3,5)}")
print(f"Volume tabung adalah {br.tabung(0.5,7)}")
print(f"Volume kerucut adalah {br.kerucut(3,7)}")

print("----BANGUN DATAR-----")
print(f"Volume persegi dengan sisi 3 adalah {bd.persegi(3)}")
print(f"Volume persegi_panjang adalah {bd.persegi_panjang(3,5)}")
print(f"Volume  Segitiga adalah {bd.segitiga(3,5)}")
print(f"Volume lingkaran adalah {bd.lingkaran(7)}")
print(f"Volume jajargenjang adalah {bd.jajargenjang(3,7)}")