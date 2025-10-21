from multiprocessing import Process
import datetime
import time
import random

def worker(name, iterations):
	for i in range(iterations):
		print(f"Worker {name}: iteration {i} - {datetime.datetime.now()}")
		time.sleep(random.random()+1)

if __name__ == '__main__':
	names = ["A","B","C"]
	process = []

	for name in names:
		p = Process(target=worker, args=[name, 5])
		process.append(p)

	for p in process:
		p.start()

	for p in process:
		p.join()

	print("\nProceso principal terminado.")

