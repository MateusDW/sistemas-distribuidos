import urllib.request
import time

start_time = time.time()

fp = urllib.request.urlopen("http://localhost:1234/")

final_time = time.time()

latency = (final_time - start_time) / 2
print("Latência = %s segundos" % latency)

encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

print(decodedContent)

fp.close()