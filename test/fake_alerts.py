# Produces a list of fake alerts
from datetime import date
from alerts.alert import Alert

def fake_alerts():
  alerts = []

  # alerts.append(Alert(1, date(2017, 11, 10), date(2017, 11, 11), date(2017, 11, 20), 
  #                 date(2017, 11, 21), ['DEN'], ['UIO']))
  # alerts.append(Alert(2, date(2017, 12, 10), date(2017, 12, 11), date(2017, 12, 20), 
  #                 date(2017, 12, 21), ['DEN'], ['ORY']))
  # alerts.append(Alert(3, date(2017, 11, 4), date(2017, 11, 14), date(2017, 11, 15), 
  #                 date(2017, 11, 30), ['DEN'], ['CDG', 'ORY']))
  # alerts.append(Alert(4, date(2017, 12, 21), date(2017, 12, 30), date(2017, 12, 31), 
  #                 date(2018, 1, 7), ['DEN'], ['GUA', 'MEX', 'BOG', 'MDE', 'HAV']))
  alerts.append(Alert(4, date(2017, 12, 21), date(2017, 12, 30), date(2017, 12, 31), 
                  date(2018, 1, 7), ['DEN'], ['GUA']))

  return alerts
