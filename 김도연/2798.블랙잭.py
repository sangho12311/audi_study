N,M = map(int,input().split())
card = list(map(int,input().split()))

card_lst = []
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if M >= (card[i] + card[j] + card[k]):
                card_lst.append(card[i] + card[j] + card[k])

print(max(card_lst))

