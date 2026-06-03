balance = 5000
withdraw = 2000

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")
