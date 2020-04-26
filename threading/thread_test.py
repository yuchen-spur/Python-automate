import subprocess
ssrProc=subprocess.Popen('E:\ShadowsocksR_VPN\ShadowsocksR-dotnet4.0.exe')

print(ssrProc.poll())
#返回None为正在进行

subprocess.Popen(['start', 'hello.txt'], shell=True)
