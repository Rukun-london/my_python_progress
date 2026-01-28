#kilometer to miles conversion


print(f" Miles to Kilometer conversion")
times=int(input("conversion table range: "))
print(f"+----------|-----------+")
print(f"|   Miles  | Kilometer |")
print(f"+----------|-----------+")
for miles in range(times):
    #kilo=float(input("Enter distance in  kilometer: "))
    kilo = miles * 1.609
    
    print(f"|{miles:>3} miles | {kilo:>6.2f} km |")
print(f"+----------|-----------+")