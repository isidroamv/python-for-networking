import paramiko
import json
#import logging
#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def interface(ip,user,psw, command):
	with open('result.txt', 'a') as result:
		try:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(hostname=ip, username= user, password= psw, look_for_keys=False, allow_agent=False)
			print ip
			print command
			
			stdin, stdout, stderr = ssh.exec_command(command)
            
			output = stdout.readlines()
			print output
			result.writelines(output)

		except Exception as e:
			print e
			return







def main():
	try:
		config = json.load(open('config.json', 'r'))
		command = 'show run | include hostname'
		ip = ''
		interface(ip, config["user"], config["password"], command)
	except Exception as e:
		print 'Is needed a config file'

if __name__ == "__main__":
	main()

