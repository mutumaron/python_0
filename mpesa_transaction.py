class MpesaTransaction:
    def __init__(self,transaction_id,amount):
        self.transaction_id=transaction_id
        self.amount=amount
    def process_transaction(self):
        raise NotImplementedError("subclass to use this")
class DepositTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Deposit transaction with ID {self.transaction_id} Processed amount {self.amount}")
class WithdrawTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Withdraw transaction with ID {self.transaction_id} Processed amount {self.amount}")
class PaymentTransaction(MpesaTransaction):
    def __init__(self,transaction_id,amount,recipient):
        super().__init__(transaction_id,amount)
        self.recipient=recipient
    def process_transaction(self):
        print(f"Payment transaction with ID {self.transaction_id} processed amount {self.amount} Recipient{self.recipient}")

deposit=DepositTransaction("456",2000)
deposit.process_transaction()

withdraw=WithdrawTransaction("567",7000)
withdraw.process_transaction()


payment=PaymentTransaction("124",2000," Ronny")
payment.process_transaction()
