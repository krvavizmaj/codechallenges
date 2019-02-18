def bankRequests(accounts, requests):
    for i,transaction in enumerate(requests):
        parts = transaction.split()
        if parts[0] == "deposit":
            if int(parts[1]) > len(accounts):
                return [-(i+1)]
            accounts[int(parts[1]) - 1] += int(parts[2])
        elif parts[0] == "transfer":
            if int(parts[1]) > len(accounts) or int(parts[2]) > len(accounts) or accounts[int(parts[1]) - 1] < int(parts[3]):
                return [-(i+1)]
            accounts[int(parts[1]) - 1] -= int(parts[3])
            accounts[int(parts[2]) - 1] += int(parts[3])
        elif parts[0] == "withdraw":
            if int(parts[1]) > len(accounts) or accounts[int(parts[1]) - 1] < int(parts[2]):
                return [-(i+1)]
            accounts[int(parts[1]) - 1] -= int(parts[2])

    return accounts

accounts = [20, 1000, 500, 40, 90]
requests = ["deposit 3 400", "transfer 1 2 30", "withdraw 4 50"]
print(bankRequests(accounts, requests))