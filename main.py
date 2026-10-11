print("Namaste, Manish Dairy!")

farmer = "Ram"
litre = 15
rate = 88

print(farmer)
print(litre)
print(rate)

total = litre * rate
print("jamma rakam:", total)

total =840
paid = 300
baaki = total - paid

if baaki > 0:
    print("baaki cha: Rs", baaki)
else:
    print("pura tirisakiyo")

total = 840
paid = 300

if paid >= total:
    print("status: Paid")
elif paid > 0:
    print("Status: partial")
else:
    print("Status: Unpaid")