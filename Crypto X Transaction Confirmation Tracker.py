import requests
import sys
import colorama
from colorama import Fore, Back, Style

networks = ["Bitcoin", "Ethereum", "Litecoin", "Dogecoin"]

def tracking_msg(id):
    print("Tracking ( " + id + " ).")

def introduction():
    print(Fore.MAGENTA + """
 ███▄    █▓██   ██▓ ▄▄▄          ▄████▄   ▒█████   ██▓ ███▄    █ 
 ██ ▀█   █ ▒██  ██▒▒████▄       ▒██▀ ▀█  ▒██▒  ██▒▓██▒ ██ ▀█   █ 
▓██  ▀█ ██▒ ▒██ ██░▒██  ▀█▄     ▒▓█    ▄ ▒██░  ██▒▒██▒▓██  ▀█ ██▒
▓██▒  ▐▌██▒ ░ ▐██▓░░██▄▄▄▄██    ▒▓▓▄ ▄██▒▒██   ██░░██░▓██▒  ▐▌██▒
▒██░   ▓██░ ░ ██▒▓░ ▓█   ▓██▒   ▒ ▓███▀ ░░ ████▓▒░░██░▒██░   ▓██░
░ ▒░   ▒ ▒   ██▒▒▒  ▒▒   ▓▒█░   ░ ░▒ ▒  ░░ ▒░▒░▒░ ░▓  ░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░▓██ ░▒░   ▒   ▒▒ ░     ░  ▒     ░ ▒ ▒░  ▒ ░░ ░░   ░ ▒░
   ░   ░ ░ ▒ ▒ ░░    ░   ▒      ░        ░ ░ ░ ▒   ▒ ░   ░   ░ ░ 
         ░ ░ ░           ░  ░   ░ ░          ░ ░   ░           ░ 
           ░ ░                  ░                                
""")
    print(Style.RESET_ALL)
introduction()

print(Fore.CYAN + "[ ! ] Hello, This tool lets you track how many confirmations your transaction on the blockchain network has!")
print(Style.RESET_ALL)


print(Fore.LIGHTYELLOW_EX + "Choose your desired network to track: ")
print("")

print("""[ 0 ] Bitcoin
[ 1 ] Ethereum
[ 2 ] Litecoin
[ 3 ] Dogecoin
""")

def main_logic_btc(txid):
    r = requests.get("https://api.blockcypher.com/v1/btc/main/txs/" + txid)
    if r.status_code == 404:
        print("This txid is incorrect or you have chosen the wrong crypto currency!")
        input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
        print(Style.RESET_ALL)
        sys.exit(0)
    confirms = r.json().get('confirmations')
    print("This transaction has ( " + str(confirms) + " ) confirmations.")
    if confirms > 6:
        print(Fore.LIGHTGREEN_EX + "This transaction has been confirmed!")
        print(Style.RESET_ALL)
    else:
        print(Fore.LIGHTMAGENTA_EX + "This transcation is yet to be confirmed!")
        print(Style.RESET_ALL)

def main_logic_eth(txid):
    r = requests.get("https://api.blockcypher.com/v1/eth/main/txs/" + txid)
    if r.status_code == 404:
        print("This txid is incorrect or you have chosen the wrong crypto currency!")
        input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
        print(Style.RESET_ALL)
        sys.exit(0)
    confirms = r.json().get('confirmations')
    print("This transaction has ( " + str(confirms) + " ) confirmations.")
    if confirms > 6:
        print(Fore.LIGHTGREEN_EX + "This transaction has been confirmed!")
        print(Style.RESET_ALL)
    else:
        print(Fore.LIGHTMAGENTA_EX + "This transcation is yet to be confirmed!")
        print(Style.RESET_ALL)

def main_logic_ltc(txid):
    r = requests.get("https://api.blockcypher.com/v1/ltc/main/txs/" + txid)
    if r.status_code == 404:
        print("This txid is incorrect or you have chosen the wrong crypto currency!")
        input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
        print(Style.RESET_ALL)
        sys.exit(0)
    confirms = r.json().get('confirmations')
    print("This transaction has ( " + str(confirms) + " ) confirmations.")
    if confirms > 6:
        print(Fore.LIGHTGREEN_EX + "This transaction has been confirmed!")
        print(Style.RESET_ALL)
    else:
        print(Fore.LIGHTMAGENTA_EX + "This transcation is yet to be confirmed!")
        print(Style.RESET_ALL)

def main_logic_doge(txid):
    r = requests.get("https://api.blockcypher.com/v1/doge/main/txs/" + txid)
    if r.status_code == 404:
        print("This txid is incorrect or you have chosen the wrong crypto currency!")
        input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
        print(Style.RESET_ALL)
        sys.exit(0)
    confirms = r.json().get('confirmations')
    print("This transaction has ( " + str(confirms) + " ) confirmations.")
    if confirms > 6:
        print(Fore.LIGHTGREEN_EX + "This transaction has been confirmed!")
        print(Style.RESET_ALL)
    else:
        print(Fore.LIGHTMAGENTA_EX + "This transacation is yet to be confirmed!")
        print(Style.RESET_ALL)

while True:
    try:
        choice = input("[ > ] ")
        if choice == "0" or choice == "1" or choice == "2" or choice == "3":
            print("")
            print("You have chosen to track a transaction on the " + networks[int(choice)] + " network.")
            txid = input("[ ! ] Please enter the txid of the transaction: ")
            print("")
            tracking_msg(txid)
            if choice == "0":
                main_logic_btc(txid)
            elif choice == "1":
                main_logic_eth(txid)
            elif choice == "2":
                main_logic_ltc(txid)
            elif choice == "3":
                main_logic_doge(txid)
            break
        else:
            print("Invalid option please try again!")
    except NameError:
        print("Input was not a digit - please try again.")

input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
print(Style.RESET_ALL)
