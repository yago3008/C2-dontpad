import subprocess

usuario = subprocess.check_output("whoami", shell=True).decode().strip()
print(usuario)
