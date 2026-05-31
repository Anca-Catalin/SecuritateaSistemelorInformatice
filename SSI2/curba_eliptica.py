class CurbaEliptica:
    def __init__(self, a, b, p):
        if (4 * a**3 + 27 * b**2) % p == 0:
            raise ValueError("Curba este singulara!")
        self.a = a
        self.b = b
        self.p = p

    def __str__(self):
        return f"y^2 = x^3 + {self.a}x + {self.b}  (mod {self.p})"

    def contine_punct(self, x, y):
        stanga  = (y * y) % self.p
        dreapta = (x**3 + self.a * x + self.b) % self.p
        return stanga == dreapta

    def aduna_puncte(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2 and (y1 + y2) % self.p == 0:
            return None
        if P != Q:
            panta = (y2 - y1) * pow(x2 - x1, -1, self.p) % self.p
        else:
            panta = (3 * x1**2 + self.a) * pow(2 * y1, -1, self.p) % self.p
        x3 = (panta**2 - x1 - x2) % self.p
        y3 = (panta * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def multiplica_punct(self, k, P):
        rezultat = None
        temp = P
        while k > 0:
            if k % 2 == 1:
                rezultat = self.aduna_puncte(rezultat, temp)
            temp = self.aduna_puncte(temp, temp)
            k //= 2
        return rezultat

    def puncte_pe_curba(self):
        puncte = []
        for x in range(self.p):
            for y in range(self.p):
                if self.contine_punct(x, y):
                    puncte.append((x, y))
        return puncte


a, b, p = 2, 3, 97
curba = CurbaEliptica(a, b, p)

print("=" * 55)
print("   CURBA ELIPTICA - Exemplu Educational")
print("=" * 55)

print(f"\nCurba definita: {curba}")
print(f"Parametri: a={a}, b={b}, p={p}")
print(f"Conditie non-singulara: 4*{a}^3 + 27*{b}^2 = {4*a**3 + 27*b**2} != 0")

print("\n--- Puncte pe curba ---")
puncte = curba.puncte_pe_curba()
print(f"Numar total de puncte: {len(puncte)}")
print(f"Primele 8 puncte: {puncte[:8]}")

# Alegem P si Q astfel incat P + Q sa nu fie punctul la infinit
P = puncte[0]
Q = puncte[2]

print(f"\n--- Operatii pe curba ---")
print(f"P = {P}")
print(f"Q = {Q}")

PplusQ = curba.aduna_puncte(P, Q)
if PplusQ is None:
    print(f"\nP + Q = Punctul la infinit (elementul neutru)")
else:
    print(f"\nP + Q = {PplusQ}")
    print(f"Verificare (pe curba): {curba.contine_punct(*PplusQ)}")

double_P = curba.aduna_puncte(P, P)
print(f"\n2P (dublare) = {double_P}")
print(f"Verificare (pe curba): {curba.contine_punct(*double_P)}")

k = 7
kP = curba.multiplica_punct(k, P)
print(f"\n{k} * P = {kP}")
print(f"Verificare (pe curba): {curba.contine_punct(*kP)}")

print("\n--- Generare chei ECC ---")
G = puncte[0]
cheie_privata = 42
cheie_publica = curba.multiplica_punct(cheie_privata, G)

print(f"Punct generator G  = {G}")
print(f"Cheie privata  (k) = {cheie_privata}")
print(f"Cheie publica (kG) = {cheie_publica}")
print(f"\nDin kG si G nu se poate calcula k (logaritmul discret).")