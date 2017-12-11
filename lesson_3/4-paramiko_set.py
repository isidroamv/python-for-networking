import paramiko
import time

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
ssh.connect(hostname="0.1.2.3", port=22, username= "user", password= "pass", look_for_keys=False, allow_agent=False)
remote_conn = ssh.invoke_shell() #invoke_shell module gives us access to talk to the device via the cli

time.sleep(2)
remote_conn.send('configure terminal')
remote_conn.send('\n')
time.sleep(2)
remote_conn.send('hostname test-sw')
remote_conn.send('\n')
time.sleep(2)

#print output
output = remote_conn.recv(65535)

# Close connection
remote_conn.close()
print("output: " + output)
