
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

print("=== PRAKTIK 4A: SIMULASI ECB ===")

pesan = "AAAAAAAABBBBBBBBAAAAAAAABBBBBBBB"
ukuran_blok = 4

blok_pesan = []
for posisi in range(0, len(pesan), ukuran_blok):
    blok = pesan[posisi:posisi + ukuran_blok]
    blok_pesan.append(blok)

for nomor, blok in enumerate(blok_pesan, 1):
    hasil = blok[::-1] + "|X"
    print("Blok", nomor, ":", blok, "->", hasil)

print("Blok 1 dan 2 sama:", blok_pesan[0] == blok_pesan[1])


print("\n=== PRAKTIK 4B: AES-ECB ASLI ===")

kunci = b"1234567890abcdef"
data = pesan.encode()

pembuat_padding = PKCS7(128).padder()
data_siap = pembuat_padding.update(data) + pembuat_padding.finalize()

mesin_ecb = Cipher(algorithms.AES(kunci), modes.ECB()).encryptor()
hasil_ecb = mesin_ecb.update(data_siap) + mesin_ecb.finalize()

blok_ecb_1 = hasil_ecb[0:16]
blok_ecb_2 = hasil_ecb[16:32]

print("Blok ECB 1:", blok_ecb_1.hex())
print("Blok ECB 2:", blok_ecb_2.hex())
print("Kedua blok sama:", blok_ecb_1 == blok_ecb_2)


print("\n=== PRAKTIK 4C: ECB VS CBC ===")

print("ECB:", hasil_ecb.hex())

iv_pertama = os.urandom(16)
mesin_cbc_1 = Cipher(algorithms.AES(kunci), modes.CBC(iv_pertama)).encryptor()
hasil_cbc_1 = mesin_cbc_1.update(data_siap) + mesin_cbc_1.finalize()

iv_kedua = os.urandom(16)
mesin_cbc_2 = Cipher(algorithms.AES(kunci), modes.CBC(iv_kedua)).encryptor()
hasil_cbc_2 = mesin_cbc_2.update(data_siap) + mesin_cbc_2.finalize()

print("CBC percobaan 1:", hasil_cbc_1.hex())
print("CBC percobaan 2:", hasil_cbc_2.hex())
print("Hasil CBC berbeda:", hasil_cbc_1 != hasil_cbc_2)
print("Blok CBC 1 dan 2 sama:", hasil_cbc_1[0:16] == hasil_cbc_1[16:32])
