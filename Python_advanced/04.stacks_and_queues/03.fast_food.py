from _collections import deque

total_food = int(input())
food_queue = deque(map(int, input().split()))

biggest_order = max(food_queue)
print(biggest_order)
current_order = food_queue.popleft()
isCompleted = False

while total_food >= current_order:
    total_food -= current_order

    if len(food_queue) == 0:
        print("Orders complete")
        isCompleted = True
        break

    current_order = food_queue.popleft()

if not isCompleted:
    #adding the last order back to the queue
    food_queue.appendleft(current_order)
    print(f"Orders left:", *food_queue, sep=" ")












