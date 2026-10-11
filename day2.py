farmer = input("Farmer ko naam: ")
litre = float(input("Dudh (litre): "))
rate = float(input("Rate per litre: "))

total = litre * rate
print("jamma rakam:", total)

paid = float(input("Tireko rakam: "))
baaki = total - paid
print("Baaki:", baaki)

if baaki > 0:
    print("Status: Baaki cha")
else:
    print("Status: Paid")
