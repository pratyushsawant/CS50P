# amount_due=50
# while amount_due>0:
#     print(f"Amount Due : {amount_due}")
#     coin=int(input("Insert coin: "))
#     if coin in [25,10,5]:
#         amount_due-=coin

# x=abs(amount_due)
# print(f"Change Owed: {x}")

print('Amount Due: 50')

amt_due = 50ye
coin_added = 0

while True:
    insert_coin = int(input('Insert Coin: '))
    if insert_coin in [25, 10,5]:
        amt_due = amt_due - insert_coin
        coin_added = coin_added + insert_coin

    if coin_added >= 50:
        print(f'Change Owed: {coin_added - 50}')
        break
    else:
        print(f'Amount Due: {amt_due}')

