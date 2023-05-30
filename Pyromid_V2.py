import os, random, codecs, time, threading
from bit.format import bytes_to_wif
from bit import Key


def _HexGen(size):
    key = ""
    for i in range(size):
        k = str(random.choice("0123456789abcdef"))
        key += f"{k}"
    return key


def _HexToWif(Hex):
    byteHex = codecs.decode(Hex, 'hex')
    wifCompressed = bytes_to_wif(byteHex, compressed=True)
    wifUnCompressed = bytes_to_wif(byteHex, compressed=False)
    return wifCompressed, wifUnCompressed


def _WifToAddr(WifCompressed, WifUnCompressed):
    BitCompressed = Key(WifCompressed)
    BitUnCompressed = Key(WifUnCompressed)
    return BitCompressed.address, BitUnCompressed.address

def _LoadTargetFile(FileName):
    tgt = [i.strip() for i in open(FileName).readlines()]
    return set(tgt)


def MainCheck():
    global z, wf
    target_file = 'richAddr.txt'
    Target = _LoadTargetFile(FileName=target_file)
    z = 0
    wf = 0
    lg = 0
    while True:
        z += 1
        Private_Key = _HexGen(64)
        WifCompressed, WifUncompressed = _HexToWif(Hex=Private_Key)
        CompressAddr, UnCompressAddr = _WifToAddr(WifCompressed, WifUncompressed)
        lct = time.localtime()
        if str(CompressAddr) in Target or str(UnCompressAddr) in Target:
            wf += 1
            open('Found.txt', 'a').write(f'Compressed Address: {CompressAddr}\n'
                                         f'UnCompressed Address: {UnCompressAddr}\n'
                                         f'Private Key: {Private_Key}\n'
                                         f'WIF (Compressed): {WifCompressed}\n'
                                         f'WIF (UnCompressed): {WifUncompressed}\n')

        elif int(z % 100000) == 0:
            lg += 100000
            print(f"Generated: {lg} (SHA-256 - HEX) ...")
        else:
            tm = time.strftime("%Y-%m-%d %H:%M:%S", lct)
            print(f"[{tm}][Total: {z} Check: {z * 2}] #Found: {wf} ", end="\r")


MainCheck()


if __name__ == '__main__':

    t = threading.Thread(target=MainCheck)
    t.start()
    t.join()
