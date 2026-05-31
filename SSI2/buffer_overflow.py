import ctypes

print("=" * 55)
print("   BUFFER OVERFLOW - Exemplu Educational")
print("=" * 55)

print("\n--- Exemplul 1: Buffer de dimensiune fixa ---")

BUFFER_SIZE = 8
buffer = ctypes.create_string_buffer(BUFFER_SIZE)
print(f"Buffer creat: {BUFFER_SIZE} bytes")
print(f"Continut initial: {buffer.raw}")

buffer.value = b"Hello"
print(f"Date normale scrise OK:  {buffer.raw}")

date_mari = b"StringPreaLungPentruBuffer"
print(f"\nIncerc sa scriu {len(date_mari)} bytes in buffer de {BUFFER_SIZE} bytes...")
try:
    buffer.value = date_mari
    print(f"Rezultat (trunchiat): {buffer.raw}")
    print(">>> Datele au fost taiate la dimensiunea bufferului!")
except Exception as e:
    print(f"Exceptie: {e}")

print("\n--- Exemplul 2: Suprascriere memorie adiacenta ---")

IntArray4 = ctypes.c_int * 4
buffer_mic = IntArray4(0, 0, 0, 0)
valoare_importanta = ctypes.c_int(9999)

print(f"Buffer (4 elemente):    {list(buffer_mic)}")
print(f"Valoare importanta:     {valoare_importanta.value}")

pointer = ctypes.cast(buffer_mic, ctypes.POINTER(ctypes.c_int))
print(f"\nScriu la index [4] — in afara bufferului...")
try:
    pointer[4] = 1337
    print(f">>> Memorie suprascrisa cu valoarea: {pointer[4]}")
    print("    In C, asta poate suprascrie variabile vecine sau adresa de retur!")
except Exception as e:
    print(f"Exceptie: {e}")

print("\n--- Exemplul 3: Simulare logica buffer overflow ---")

buffer_login = bytearray(8)
autorizat = bytearray(b'\x00\x00\x00\x00')

print(f"Buffer input:    {bytes(buffer_login)}")
print(f"Autorizat:       {int.from_bytes(autorizat, 'little')} (0 = NU)")

memorie = bytearray(12)
input_overflow = b"AAAAAAAAAAAAA"
memorie[:len(input_overflow)] = input_overflow[:12]

buffer_login = memorie[:8]
autorizat = memorie[8:12]

print(f"Dupa overflow:      autorizat = {int.from_bytes(autorizat, 'little')}")
if int.from_bytes(autorizat, 'little') != 0:
    print(">>> ACCES ACORDAT prin buffer overflow! (autorizat != 0)")
