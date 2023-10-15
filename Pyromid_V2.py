# install cryptofuzz & colorthon
# pip install cryptofuzz / pip install colorthon
import os, random, time, threading
from cryptofuzz import Convertor
from cryptofuzz.assest import MAX_PRIVATE_KEY
from colorthon import Colors

co = Convertor()

# COLORS CODE --------------------
RED = Colors.RED
GREEN = Colors.GREEN
YELLOW = Colors.YELLOW
CYAN = Colors.CYAN
WHITE = Colors.WHITE
RESET = Colors.RESET
# COLORS CODE -------------------

def getClear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


def KeyGen(size):
	k = "".join(random.choice('0122333444455555666666777777788888888999999999abcdef') for _ in range(size))
	if int(k, 16) < MAX_PRIVATE_KEY:
		return k
	else:
		return KeyGen(size)


def Hex_To_Addr(hexed, compress):
	return co.hex_to_addr(hexed, compress)


def Rich_Loader(FileName):
	return set([i.strip() for i in open(FileName).readlines()])


def getHeader(richFile, loads, found):
	getClear()
	output = f"""
{YELLOW}\t██████╗ ██╗   ██╗██████╗  ██████╗ ███╗   ███╗██╗██████╗ {RESET}
{YELLOW}\t██╔══██╗╚██╗ ██╔╝██╔══██╗██╔═══██╗████╗ ████║██║██╔══██╗{RESET}
{YELLOW}\t██████╔╝ ╚████╔╝ ██████╔╝██║   ██║██╔████╔██║██║██║  ██║{RESET}
{YELLOW}\t██╔═══╝   ╚██╔╝  ██╔══██╗██║   ██║██║╚██╔╝██║██║██║  ██║{RESET}
{YELLOW}\t██║        ██║   ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║██████╔╝{RESET}
{YELLOW}\t╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═════╝ {RESET}
{RED}╔═╗╦═╗╔═╗╔═╗╦═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗{RESET}  {WHITE}╔╦╗╔╦╗╔╦╗╦═╗╔═╗╔═╗ ╔═╗╔═╗╔╦╗{RESET}
{RED}╠═╝╠╦╝║ ║║ ╦╠╦╝╠═╣║║║║║║║╣ ╠╦╝{RESET}  {WHITE}║║║║║║ ║║╠╦╝╔═╝╠═╣ ║  ║ ║║║║{RESET}
{RED}╩  ╩╚═╚═╝╚═╝╩╚═╩ ╩╩ ╩╩ ╩╚═╝╩╚═{RESET}  {WHITE}╩ ╩╩ ╩═╩╝╩╚═╚═╝╩ ╩o╚═╝╚═╝╩ ╩{RESET}
{RED}➜{RESET} {WHITE}Pyromid {RESET}{CYAN}v2 {RESET}Ⓟ{GREEN} Powered By CryptoFuzz - Exclusive MMDRZA.COM{RESET}
{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}
{RED}[{RESET}{WHITE}►{RESET}{RED}]{RESET}{GREEN} Import Rich File :{RESET}{CYAN} {richFile}                {RESET}
{RED}[{RESET}{WHITE}►{RESET}{RED}]{RESET}{GREEN} Method Generated :{RESET}{CYAN} Random Without Repeat.    {RESET}
{RED}[{RESET}{WHITE}►{RESET}{RED}]{RESET}{GREEN} Address Type     :{RESET}{CYAN} Compressed / Uncompressed.{RESET}
{RED}[{RESET}{WHITE}►{RESET}{RED}]{RESET}{GREEN} Max Decimal (HEX):{RESET}{CYAN} {MAX_PRIVATE_KEY}         {RESET}
{RED}[{RESET}{WHITE}►{RESET}{RED}]{RESET}{GREEN} Result Checked   :{RESET}{CYAN} {loads}                   {RESET}
{RED}[{RESET}{WHITE}►{RESET}{RED}]{RESET}{GREEN} Matched Address  :{RESET}{CYAN} {found}                   {RESET}
"""
	print(output)


def MainCheck():
	global z, wf
	target_file = 'Rich.txt'
	Targets = Rich_Loader(target_file)
	z = 0
	wf = 0
	lg = 0
	getHeader(richFile=target_file, loads=lg, found=wf)
	while True:
		z += 1
		privatekey = KeyGen(64)
		# compress address
		CompressAddr = Hex_To_Addr(privatekey, True)
		# uncompress address
		UncompressAddr = Hex_To_Addr(privatekey, False)
		lct = time.localtime()
		if str(CompressAddr) in Targets:
			wf += 1
			open('Found.txt', 'a').write(f"Compressed Address: {CompressAddr}\n"
										 f"Private Key: {privatekey}\n"
										 f"DEC: {int(privatekey, 16)}\n"
										 f"{'-' * 66}\n")
		elif str(UncompressAddr) in Targets:
			wf += 1
			open('Found.txt', 'a').write(f"Uncompressed Address: {CompressAddr}\n"
										 f"Private Key: {privatekey}\n"
										 f"DEC: {int(privatekey, 16)}\n"
										 f"{'-' * 66}\n")
		elif int(z % 100000) == 0:
			lg += 100000
			getHeader(richFile=target_file, loads=lg, found=wf)
			print(f"Generated: {lg} (SHA-256 - HEX) ...")
		else:
			tm = time.strftime("%Y-%m-%d %H:%M:%S", lct)
			print(f"[{tm}][Total: {z} Check: {z * 2}] #Found: {wf} ", end="\r")


MainCheck()

if __name__ == '__main__':
	t = threading.Thread(target=MainCheck)
	t.start()
	t.join()
