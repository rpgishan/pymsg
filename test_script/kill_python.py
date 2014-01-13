import os


def main():
	cmd = """ps -ef | grep send.py | awk '{print $2}'"""
	for chunk in os.popen(cmd):
		kill = """kill -9 %s""" % chunk 
		os.system(kill)


if __name__ == "__main__":
	main()
