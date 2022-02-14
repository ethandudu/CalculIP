import ipaddress,sys 

try: 
    ip = sys.argv[1]
except IndexError: 
    print("Merci de préciser l'adresse ip  et le masque de sous-réseau dans la ligne de commande")
    print("FORMAT ACCEPTÉ: 192.168.0.1/24")
    sys.exit()


class CalculatorIP:
    def __init__(self): 
        self.subnet()
    
    def subnet(self): 
        try:
            first = list(ipaddress.ip_network(ip).hosts())[0]
            last = list(ipaddress.ip_network(ip).hosts()) [-1]
            netmask = ipaddress.IPv4Interface(ip).netmask
            hostmask = ipaddress.IPv4Interface(ip).hostmask 
            broadcast = ipaddress.IPv4Network(ip).broadcast_address
        except ValueError:
            print("Format non accepté")
        print(f"first: {first} | last: {last} | netmask: {netmask} | hostmask: {hostmask} | broadcast: {broadcast}")        

    def host(self):
        liste = list(ipaddress.ip_network(ip).hosts())
        for i in liste: 
            print(i)

    def binaire(self): 
        try: 
            print("Binaire: {:b}".format(ipaddress.IPv4Address(ip)))
        except ipaddress.AddressValueError:
            print("Merci d'enlever le '/' et le nombre qui le suis svp")
    

