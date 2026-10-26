#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erteleme Sanatı Ustası
=====================
Bu script, herhangi bir görevi sonsuza kadar ertelemek için
mükemmel, bilimsel ve tamamen absürt bahaneler üretir.
Gerçekten çalışır. Garantili.
"""

import random
import time

bahaneler = [
    "Kuantum belirsizliği prensibine göre bu görevin yapılıp yapılmayacağı henüz gözlemlenmedi.",
    "Evren genişliyor, ben de genişliyorum. Görev beklemek zorunda.",
    "Kedi şu anda klavyenin üstünde uyuyor. Doğa kanunu ihlal edilemez.",
    "Bu görevi yaparsam paralel evrendeki versiyonum çok kıskanır.",
    "Astrolojiye göre Merkür retroda. Hiçbir şey yazılmamalı.",
    "Kahve bitmiş. Kahve olmadan insan değil, sadece bir memeliyim.",
    "Görevi ertelemek aslında onu daha önemli hale getirir. Felsefe böyle der.",
    "Şu an evrenin en önemli işi, bu cümleyi okuman. Görev sonra.",
    "Eğer şimdi yaparsam, gelecekteki ben çok sıkılır. Ona yazık.",
    "Bilimsel olarak kanıtlandı: Ertelemek ömrü uzatır. (Kaynak: Ben)"
]

def ertele(gorev="bu görevi"):
    print(f"\n🎭 Erteleme Sanatı Ustası Devrede! 🎭")
    print(f"Görev: {gorev}")
    print("Analiz ediliyor...", end="", flush=True)
    for _ in range(3):
        time.sleep(0.7)
        print(".", end="", flush=True)
    print("\n")
    bahane = random.choice(bahaneler)
    print(f"✨ MÜKEMMEL BAHANE: {bahane}")
    print("\n👍 Görev başarıyla ertelendi. Tebrikler, bir adım daha özgürsün.")
    print("\nTekrar çalıştırmak için: python3 erteleme_ustasi.py")

if __name__ == "__main__":
    import sys
    gorev = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "hayattaki tüm sorumluluklarımı"
    ertele(gorev)
