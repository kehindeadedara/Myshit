import binascii
def text_to_bits(text, encoding='ascii', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


word = 'word'

neword = (text_to_bits(word))

print(len(neword))