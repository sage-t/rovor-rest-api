from abc import ABCMeta, abstractmethod

class CrawlerInterface:
  __metaclass__ = ABCMeta

  @abstractmethod
  def discover(self, time):
    """discover deals from the site, not caring about date/destinations"""
    return

  @abstractmethod
  def run(self, alert):
    """run the crawler with the specified alert data and return a crawler response"""
    return
