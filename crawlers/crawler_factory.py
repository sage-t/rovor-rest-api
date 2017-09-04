from skiplagged_crawler import SkiplaggedCrawler

class CrawlerFactory:

  def __init__(self):
    self.crawlers = []
    self.crawlers.append(SkiplaggedCrawler())
  
  def discover(self, time):
    responses = []
    time_per = time / len(self.crawlers)
    for crawler in self.crawlers:
      responses.extend(crawler.discover(time))

    return responses

  def crawl(self, alert):
    responses = []
    for crawler in self.crawlers:
      responses.extend(crawler.run(alert))
    
    # TODO: sort responses
    return responses