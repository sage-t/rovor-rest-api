# Provides the next alert to run
from test.fake_alerts import fake_alerts

class AlertIterator:
  
  def __init__(self):
    # TODO: make list ordered by first to be run first
    self.alerts = fake_alerts()

  def iterator(self):
    i = 0
    while True:
      yield self.alerts[i]
      i = (i + 1) % len(self.alerts)
