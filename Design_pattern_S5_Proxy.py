class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrawn ${amount}. Remaining balance: ${self.balance}"
class ATMProxy:
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def withdraw(self, amount, pin):
        if pin != "1234":  # Fake PIN check for simplicity
            return "Invalid PIN!"
        
        print("ATM Proxy: Verifying your identity...")
        print("ATM Proxy: Processing transaction...")
        
        return self.bank_account.withdraw(amount)
    

if __name__=="__main__":
    # Create a real bank account
    account = BankAccount(balance=1000)

    # Create an ATM proxy to access the account
    atm = ATMProxy(account)

    # Withdraw money using the ATM proxy
    print(atm.withdraw(200, "1234"))
    print(atm.withdraw(100, "0000"))
    print(atm.withdraw(1000, "1234"))


"""Example 2"""
class Internet:
    def connect_to(self, website):
        print(f"Connecting to {website}")

class FirewallProxy:
    blocked_sites = ["facebook.com", "youtube.com", "instagram.com"]

    def __init__(self):
        self.internet = Internet()

    def connect_to(self, website):
        if website in self.blocked_sites:
            print(f"Access to {website} is BLOCKED!")
        else:
            self.internet.connect_to(website)

# Client
proxy = FirewallProxy()
proxy.connect_to("google.com")
proxy.connect_to("facebook.com")