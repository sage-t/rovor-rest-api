class RovorConfig:
  
  def __init__(self):
    self.db_loc = 'db/rovor-api.sqlite'
    self.deals_columns = 'start_airport, end_airport, price, outbound_date, inbound_date, link'