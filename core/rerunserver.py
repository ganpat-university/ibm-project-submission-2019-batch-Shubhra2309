import subprocess
print("RE RUNNING SERVER")
"""# Find the process ID of the Django server running on port 8000
netstat_output = subprocess.check_output(["netstat", "-ano"]).decode("utf-8")
findstr_output = subprocess.check_output(["findstr", "8000"], input=netstat_output.encode("utf-8")).decode("utf-8")
pid = findstr_output.split()[-1]

# Kill the server process
subprocess.call(["taskkill", "/F", "/PID", pid])"""

process = subprocess.Popen(['py', r'C:\Users\dhair\PycharmProjects\DjangoERP\InventoryManagement-Django\manage.py', 'runserver'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print("STDOUT:", stdout.decode("utf-8"))
print("STDERR:", stderr.decode("utf-8"))