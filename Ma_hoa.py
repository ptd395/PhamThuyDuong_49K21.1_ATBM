PLAIN_TEXT = "PhamThuyDuong"  
K = 21                       

ket_qua = []
for ch in PLAIN_TEXT:
    if 'A' <= ch <= 'Z':
        ma = (ord(ch) - ord('A') + K) % 26 + ord('A')
        ket_qua.append(chr(ma))
    elif 'a' <= ch <= 'z':
        ma = (ord(ch) - ord('a') + K) % 26 + ord('a')
        ket_qua.append(chr(ma))
    else:
        ket_qua.append(ch)

cipher = ''.join(ket_qua)

print("Plaintext:", PLAIN_TEXT)
print("K:", K)
print("Mã hóa theo Ceasar:", cipher)

