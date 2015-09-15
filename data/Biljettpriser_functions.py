# -*- coding: utf-8 -*-

def priskoll(age):
    age = int(age)   # Omvandlar input str till int
    if age in range(18,65): # Returnerar 20 kr i biljettpris då användare är mellan 18-64 år gammal.
        return 20
    elif age in range(0,131): # Returnerar 15 kr i biljettpris till alla övriga användare. Användaren måste vara mellan 0-130 år.
        return 15
    else:
        return "err" # Returnerar variabel som behandlas som felkod som ger information om att användaren har angivit ålder som inte är mellan 0-130 år.