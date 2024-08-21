import sys
sys.stdin = open("input.txt", "r")

N = int(input())

card = [i for i in range(1, N+1)]
queue = []      # 버린카드 담는 큐

while len(card) > 1:
    queue.append(card.pop(0))
    card.append(card.pop(0))

print(*queue, card[0])