showroom = set()
showroom.add("430 Scuderia Spyder 16M")
showroom.add("M3 CRT")
showroom.add("CLK DTM")
showroom.add("MC12")
print(showroom)

showroom.add("M3 CRT")
print(showroom)

newCars = set()
newCars.add("Shelby GT350")
newCars.add("F12 TDF")
showroom.update(newCars)
print(showroom)

showroom.discard("Shelby GT350")
print(showroom)


junkyard = set()
junkyard.add("Shelby GT500")
junkyard.add("CLK DTM")
junkyard.add("F40")
print(junkyard)

print(showroom.intersection(junkyard))

print(showroom.union(junkyard))

junkyard.discard("Shelby GT500")
print(junkyard)
print(showroom.union(junkyard))
