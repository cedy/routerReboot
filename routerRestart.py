import urllib.request
import urllib.error
import socket
import sys


class modemRestart:
    '''Little class for reboot router ZOOm 5352 \r\n 
    Usage: script.py ip login password \r\n
    Example: script.py 192.168.0.1 admin password'''
    
    def __init__(self, ip, login, password):
        self.ip = ip
        self.login = login
        self.password = password
        
    def singup(self):
        login_data = {"loginUsername" : self.login,
                      "loginPassword" : self.password}
        login_data = urllib.parse.urlencode(login_data).encode('utf8')
        url = "http://{0}/goform/login".format(self.ip)
        #logining
        req = urllib.request.Request(url, login_data)
        try:
            resp = urllib.request.urlopen(req, timeout=3).geturl()
            if resp != "http://{0}/RgConnect.asp".format(self.ip):
                print("Login or password incorrect")
                exit(1)
        except urllib.error.URLError:
            print("Server doesn't respond")
            exit(1)
            
    def reboot(self):
        url = "http://{0}/goform/RgSecurity".format(self.ip)
        reboot_data = {"UserId" : '',
                       "OldPassword" : '',
                       "Password" : '',
                       "PasswordReEnter" : '',
                       "ResRebootYes" : '0x01', 
                       "RestoreFactoryNo" : '0x00', 
                       "RgRouterMode" : 1}
        reboot_data = urllib.parse.urlencode(reboot_data).encode('utf8')
        req = urllib.request.Request(url, reboot_data)
        try:
            urllib.request.urlopen(req, timeout=3)
        except urllib.error.URLError:
            print("Server doesn't respond2")
            exit(1)
        except socket.timeout:
            print("Restarting")
            
            
            
def main():
    if len(sys.argv) != 4:
        print("\r\nUsage: python3 script.py modem_ip login password \r\n\
Example: ./{} 192.168.0.1 admin password\r\n".format(sys.argv[0]))
    else:
        ob = modemRestart(sys.argv[1], sys.argv[2], sys.argv[3])
        ob.singup()
        ob.reboot()
        
if __name__ == '__main__':
    main()
    
    
    
