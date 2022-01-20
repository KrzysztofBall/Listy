import math
print(5//2) #normalne dzielenie bez reszty, szkoda że z pojedynczym znakiem dali to upośledzone z ułamkami a do tego trzeba podwójny znak.
print(round(5//2)) #bezsensowne zaokrąglanie wyniku do liczby całkowitej. Dla n.5 n%2==0 zaokrągla w dół a dla n%2==1 w górę.
print(math.floor(5//2)) #sensowniejsze zaokrąglenie bo zawsze w dół
