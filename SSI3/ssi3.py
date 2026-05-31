p = 17

def verifica_punct(x, y, p):
    return (2 * y * y) % p == (x**3 + 2*x + 2) % p

def aduna_puncte(P, Q, p):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if P != Q:
        panta = (y2 - y1) * pow(x2 - x1, -1, p) % p
    else:
        panta = (3 * x1**2 + 2) * pow(4 * y1, -1, p) % p
    x3 = (2 * panta**2 - x1 - x2) % p
    y3 = (panta * (x1 - x3) - y1) % p
    return (x3, y3)

puncte = [(x,y) for x in range(p) for y in range(p) if verifica_punct(x, y, p)]

print("=" * 55)
print("   ADUNARE PUNCTE PE CURBA ELIPTICA")
print("=" * 55)
print(f"\nCurba: 2y^2 = x^3 + 2x + 2  (mod {p})")
print(f"\nPunctele de pe curba ({len(puncte)} total):")
print(puncte)

print(f"\n--- Observatie ---")
print(f"P(0,6) pe curba: {verifica_punct(0, 6, p)}  (eroare in enuntul temei)")
print(f"Q(1,9) pe curba: {verifica_punct(1, 9, p)}  (eroare in enuntul temei)")
print(f"Folosim punctele reale P=(0,1) si Q=(3,3)")

P = (0, 1)
Q = (3, 3)

print(f"\n--- Adunare puncte ---")
print(f"P = {P}  ->  pe curba: {verifica_punct(*P, p)}")
print(f"Q = {Q}  ->  pe curba: {verifica_punct(*Q, p)}")

x1, y1 = P
x2, y2 = Q
panta = (y2 - y1) * pow(x2 - x1, -1, p) % p
print(f"\nPanta m = ({y2}-{y1}) * inv({x2}-{x1}, {p}) mod {p} = {panta}")
x3 = (2 * panta**2 - x1 - x2) % p
y3 = (panta * (x1 - x3) - y1) % p
print(f"x3 = 2*m^2 - x1 - x2 = 2*{panta}^2 - {x1} - {x2} mod {p} = {x3}")
print(f"y3 = m*(x1-x3) - y1 = {panta}*({x1}-{x3}) - {y1} mod {p} = {y3}")

rezultat = aduna_puncte(P, Q, p)
print(f"\nP + Q = {rezultat}")
print(f"Verificare rezultat pe curba: {verifica_punct(*rezultat, p)}")