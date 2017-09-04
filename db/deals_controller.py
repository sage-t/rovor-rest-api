from db_controller import DBController
from rovor_config import RovorConfig
from crawlers.crawler_response import CrawlerResponse
from datetime import datetime

# Controller for the 'deals' table
class DealsController:

  def __init__(self):
    self.table = 'deals'
    self.config = RovorConfig()

  def getOneWays(self, start_airport, end_airport, date):
    conn = DBController().getConnection()
    c = conn.cursor()

    responses = []
    try:
      c.execute("SELECT * FROM {} WHERE inbound_date='None' AND \
                                        outbound_date='{}' AND \
                                        start_airport='{}' AND \
                                        end_airport='{}' \
                                        ORDER BY price"\
        .format(self.table, date, start_airport, end_airport))

      for row in c.fetchall():
        responses.append(CrawlerResponse(
          row[2], 
          datetime.strptime(row[3], "%Y-%m-%d").date(),
          None,
          row[0],
          row[1],
          row[5]
        ))
    except Exception as e:
      print "Error getting getting one way flights from DB: " + str(e)
    
    return responses

  def getRoundTrips(self, alert):
    pass

  def deleteOutdated(self, date):
    pass

  def putCrawlerResponses(self, responses):
    for response in responses:
      self.putCrawlerResponse(response)

  def putCrawlerResponse(self, response):
    conn = DBController().getConnection()
    c = conn.cursor()

    try:
      c.execute("INSERT INTO {} ({}) VALUES ('{}', '{}', {}, '{}', '{}', '{}')".\
              format(
                self.table,
                self.config.deals_columns,
                response.start_airport,
                response.end_airport,
                response.price,
                response.outbound,
                response.inbound,
                response.website
              ))
    except Exception as e:
      print('ERROR: Failed to insert a crawler response:\n' + str(e))
    conn.commit()
    conn.close()