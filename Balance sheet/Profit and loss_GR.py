# Python 3.8.5
# Υπολογισμός κέρδους και ζημιάς με βάση τον τύπο των διαδοχικών ισολογισμών.
# Τύπος: Αποτέλεσμα = Τελικό Κεφάλαιο - Αρχικό Κεφάλαιο - Εισφορές Επιχειρηματία + Απολήψεις Επιχειρηματία.

eis = float(input("Εισφορές: "))
while eis < 0:
    print ("Ο αριθμός είναι αρνητικός."
"\n" + "Προσπαθήστε ξανά!")
    eis = float(input("Εισφορές: "))
apo = float(input("Απολήψεις: "))
while apo < 0:
    print ("Ο αριθμός είναι αρνητικός."
"\n" + "Προσπαθήστε ξανά!")
    apo = float(input("Απολήψεις: "))
arx = float(input("Αρχικό κεφάλαιο: "))
tel = float(input("Τελικό κεφάλαιο: "))
x = tel - arx - eis + apo
if x > 0:
    print ("Το κέρδος είναι:", round(x, 2))
elif x < 0:
    print ("Η ζημιά είναι:", round(x, 2))
else:
    print ("Το αποτέλεσμα είναι:", x)
