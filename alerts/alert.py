# alert object

class Alert:

  def __init__(self, id, outbound_start, outbound_end, inbound_start, inbound_end, start_airports,
                end_airports):
    self.id             = id
    self.active         = True
    self.best_price     = -1
    self.outbound_start = outbound_start
    self.outbound_end   = outbound_end
    self.inbound_start  = inbound_start
    self.inbound_end    = inbound_end
    self.start_airports = start_airports
    self.end_airports   = end_airports

  def __str__(self):
    return """[Alert {}]
---------------------------
active:         {}
best price:     {}
outbound start: {}
outbound end:   {}
inbound start:  {}
inbound end:    {}
start aiports:  {}
end airports:   {}
---------------------------
""".format(self.id, self.active, self.best_price, self.outbound_start, self.outbound_end, 
            self.inbound_start, self.inbound_end, self.start_airports, self.end_airports)
