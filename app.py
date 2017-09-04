import sys
import time
from alerts.alert_iterator import AlertIterator
from crawlers.crawler_factory import CrawlerFactory
from db.deals_controller import DealsController

def run(argv):
  iterator = AlertIterator().iterator()
  factory = CrawlerFactory()
  deals_controller = DealsController()
  while True:
    alert = iterator.next()
    print(alert)

    # get 
    # print(factory.discover(1))

    # for response in factory.discover(1):
    #   print response
    #   deals_controller.putCrawlerResponse(response)
    
    responses = factory.crawl(alert)
    
    for response in responses:
      print str(response)

    # print responses[0]

    time.sleep(5)
    # crawl with factory
    # update db
    # delete outdated db deals

if __name__ == "__main__":
  run(sys.argv[1:])
