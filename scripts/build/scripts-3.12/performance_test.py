import timeit
from onlinebanking_system.banking import BankingSystem

def performance_test():
    bank = BankingSystem()
    for i in range(10000):
        bank.register_user(f"user{i}", "1234")

    start_time = timeit.default_timer()
    bank.deposit(1000)
    elapsed = timeit.default_timer() - start_time
    print(f"Time to deposit: {elapsed:.5f} seconds")

if __name__ == "__main__":
    performance_test()
