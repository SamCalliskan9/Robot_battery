
import random
import time

yerler = ["Laboratuvar", "atölye", "depo", "çatı", "garaj"]

enerji = 100
buldu_mu = False

print("Pyro bataryasını aramaya başladı...\n")

for yer in yerler:
    print(f" {Yer} kontrol ediliyor...")
    time.sleep(1)
    enerji -= 20

    if random.choice([True, False]):
        print(f" Pyro bataryasını {yer} içinde buldu!")
        buldu_mu = True
        break
    else:
        print(f" {yer} içinde batarya yok. Enerji: {enerji}%\n")

if buldu_mu:
    print("\n Görev tamamlandı! Pyro yeniden şari oluyor...")
else:
    print("\n Pyro bataryayı bulamadı... Enerjisi bitti. Yeniden dene!")
