urunlerDizisi = []
adet = int(input("Kaç adet ürün eklemek istiyorsunuz: "))
i = 0
while (i < adet):
    urunAdi = input("Ürün adı: ")
    urunFiyati = input("Ürün fiyatı: ")
    urunlerDizisi.append({
        "ad": urunAdi,
        "fiyat": urunFiyati
    })
    i += 1
for urun in urunlerDizisi:
    print(f"Ürün adı: {urun['ad']} - Ürün fiyatı: {urun['fiyat']}")