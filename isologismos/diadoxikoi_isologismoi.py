# Python 3.8.5
# Υπολογισμός κέρδους και ζημιάς με βάση τους τύπους των διαδοχικών ισολογισμών.
# Τύπος 1: Αποτέλεσμα = Τελικό Κεφάλαιο - Αρχικό Κεφάλαιο.
# Τύπος 2: Αποτέλεσμα = Τελικό Κεφάλαιο - Αρχικό Κεφάλαιο - Εισφορές Επιχειρηματία + Απολήψεις Επιχειρηματία.

eis = int(input("Δώστε τιμή εισφορών: "))
while eis < 0:
    print ("Η τιμή είναι αρνητική.")
    eis = int(input("Δώστε έγκυρη τιμή εισφορών: "))
apo = int(input("Δώστε τιμή απολήψεων: "))
while apo < 0:
    print ("Η τιμή είναι αρνητική.")
    apo = int(input("Δώστε έγκυρη τιμή απολήψεων: "))
arx = int(input("Δώστε τιμή αρχικού κεφαλαίου: "))
while arx < 0: 
    print ("Η τιμή είναι αρνητική.")
    arx = int(input("Δώστε έγκυρη τιμή αρχικού κεφαλαίου: "))
While arx == 0:
    print("Η τιμή του αρχικού κεφαλαίου είναι: ", arx)
    arx = int(input("Δώστε έγκυρη τιμή αρχικού κεφαλαίου: "))
tel = int(input("Δώστε τιμή τελικού κεφαλαίου: "))
while tel < 0: 
    print ("Η τιμή είναι αρνητική: ")
    tel = int(input("Δώστε έγκυρη τιμή τελικού κεφαλαίου: "))
if eis == 0 and apo == 0:
    x = tel - arx
    if x > 0:
        print ("Κέρδος:", x, "ευρώ")
    elif x < 0:
        print ("Ζημιά:", x, "ευρώ")
    else:
        print ("Δεν υπάρχει κέρδος, ούτε ζημιά.")
else:
    x = tel - arx - eis + apo
    if x > 0:
        print ("Κέρδος:", x, "ευρώ")
    elif x < 0:
        print ("Ζημιά:", x, "ευρώ")
    else:
        print ("Δεν υπάρχει κέρδος, ούτε ζημιά.")
