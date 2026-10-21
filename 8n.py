def narxlarni_ol(narx_matnlari):
    natija = []

    for matn in narx_matnlari:
        try:
            narx = int(matn)
            natija.append(narx)
        except ValueError:
            print("Noto'g'ri narx:", matn)

    return natija


print(narxlarni_ol(["12000", "x", "5000"]))
print(narxlarni_ol([]))