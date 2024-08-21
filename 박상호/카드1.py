from collections import deque
N = int(input())
newcard_lst = []

card_lst = [i for i in range(1, N+1)]

de_card_lst = deque(card_lst)

for _ in range(N-1):
    newcard_lst.append(de_card_lst[0])
    de_card_lst.popleft()
    de_card_lst.append(de_card_lst[0])
    de_card_lst.popleft()

print(*newcard_lst, *de_card_lst)