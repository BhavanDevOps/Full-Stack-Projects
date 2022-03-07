given_cp=int(input())
given_sp=int(input())

is_profit=  given_sp>given_cp
no_profit_no_loss=(given_sp==given_cp)

if is_profit:
    print("Profit")
elif no_profit_no_loss:
    print("No Profit-No Loss")
else:
    print("Loss")