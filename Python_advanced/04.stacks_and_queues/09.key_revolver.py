from collections import deque

bullet_price = int(input())
size = int(input())
current_size = 0
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
prize = int(input())

while len(bullets) > 0 and len(locks) > 0:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    prize -= bullet_price

    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)

    current_size += 1
    if current_size == size and len(bullets) > 0:
        print("Reloading!")
        current_size = 0

if len(locks) <= 0:
    print(f"{len(bullets)} bullets left. Earned ${prize}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
