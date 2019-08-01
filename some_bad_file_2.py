import os, sys
import subprocess

os.system("echo 'hello'")
subprocess.popen("echo 'hello'")

print("these should flag the command plugin")

sys.exit(0)
