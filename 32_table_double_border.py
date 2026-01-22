#kilometer to miles conversion
print(f" Miles to Kilometer conversion")
times=int(input("conversion table range: "))
print(f"╔═══════════╦═══════════╗")
print(f"║   Miles   ║ Kilometer ║")
print(f"╠═══════════╬═══════════╣")

for miles in range(times):
    #kilo=float(input("Enter distance in  kilometer: "))
    kilo = miles * 1.609
    
    print(f"║{miles:>3} miles  ║ {kilo:>6.2f} km ║")
print(f"╚═══════════╩═══════════╝")

'''
box drawing Characters
Hold Alt and type the number on the numeric keypad.

Character	Alt Code
╔	Alt + 201
╗	Alt + 187
╚	Alt + 200
╝	Alt + 188
═	Alt + 205
║	Alt + 186
╦	Alt + 203
╩	Alt + 202
╬	Alt + 206
╠	Alt + 204
╣	Alt + 185'''