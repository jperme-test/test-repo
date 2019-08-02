import os, sys
import subprocess

some_db_sql = "INSERT INTO users VALUES (steve, 1234 steve street)"
print("this should flag the SQL plugin")

os.system("echo 'hello'")
subprocess.popen("echo 'hello'")

print("these should flag the command plugin")

sys.exit(0)
