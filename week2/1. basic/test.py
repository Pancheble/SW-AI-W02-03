from collections import deque
jobs = ["문서A", "문서B", "문서C"]

queue = deque(jobs)
processed = []

while queue:
    processed.append(queue.popleft())
print(processed)