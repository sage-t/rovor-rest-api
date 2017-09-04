# Crawler response object
class CrawlerResponse:

  def __init__(self, price, outbound, inbound, start_airport, end_airport, website):
    self.price          = price
    self.outbound       = outbound
    self.inbound        = inbound
    self.start_airport  = start_airport
    self.end_airport    = end_airport
    self.website        = website

  def __str__(self):
    return "(price: ${}, outbound: {}, inbound: {}, start airport: {}, end airport: {}, website: {})".format(
        self.price, self.outbound, self.inbound, self.start_airport, self.end_airport, self.website)
