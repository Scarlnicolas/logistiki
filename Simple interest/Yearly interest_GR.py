# Python 3.8.5
# Εύρεση απλού τόκου σε έτη, εξάμηνα και τρίμηνα.

capital = float(input("Κεφάλαιο: "))
# Παράδειγμα: επιτόκιο 0.15 αντί για 15%.
interest_rate = float(input("Επιτόκιο: "))
# Παράδειγμα 1: 2 έτη και έξι μήνες --> 2 * 2 + 1 = 5 εξάμηνα --> χρονικά διαστήματα: 5.
# Παράδειγμα 2: 4 έτη --> Χρονικά διαστήματα: 4.
time = int(input("Χρονικά διαστήματα: ")) 
interest = capital * time * interest_rate
print ("Ο τόκος του κεφαλαίου είναι:", round(interest,2))
