import time

class Transaction:
  def __init__(self, manufacturer_id, distributor_id, client_id, amount = None):
    self.manufacturer_id = manufacturer_id
    self.distributor_id = distributor_id
    sel.client_id = client_id
    self.amount = amount
    self.timestampp = int(time.time())

def to_dict(self):
  transaction_dict={
    "ManufacturerID": self.manufacturer_id,
    "DistributorID": self.distributor_id,
    "ClientID": self.client_id,
    "Timestamp": self.timestamp
  }
  if self.amount is not None:
    transaction_dict["Amount"] = self.amount
  return transaction_dict
