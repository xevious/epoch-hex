import time

END_EPOCH = 2147483647

while True:
    now = int(time.time())
    remaining = END_EPOCH - now
    print(f"{hex(remaining)}", end='\r', flush=True)
    time.sleep(1)
