import os
liste = os.listdir("Egzersiz/")
import subprocess
for item in liste:
    subprocess.run(("python",f"Egzersiz/{item}/02_02_str.py"))