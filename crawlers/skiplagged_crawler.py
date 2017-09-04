from crawler_interface import CrawlerInterface
from crawler_response import CrawlerResponse
from datetime import date, datetime, timedelta
from eventlet.timeout import Timeout
from db.deals_controller import DealsController
import requests

class SkiplaggedCrawler(CrawlerInterface):

  # browse and record flight deals for specified time in seconds
  def discover(self, time):
    responses = []
    with Timeout(time, False):
      try:
        raw_json = requests.get('http://skiplagged.com/api/deals.php').json()

        for deal in raw_json['deals']:
          date = datetime.strptime(deal['depart_date'], "%Y-%m-%d").date()
          responses.append(CrawlerResponse(
            int(deal['price']) / 100,
            date,
            None,
            deal['src_code'],
            deal['dst_code'],
            "https://skiplagged.com/flights/{}/{}/{}".format(deal['src_code'], deal['dst_code'], date)
          ))
      except Exception as e:
        print "Warning: Error while discovering deals on skiplagged: " + str(e)

    # TODO: remove duplicates
    return responses

  def run(self, alert):
    # determine cheapest one way days for each

    outbound_flights = self.findOneWayFlights(
                        alert.start_airports, 
                        alert.end_airports, 
                        alert.outbound_start, 
                        alert.outbound_end
                      )

    inbound_flights = self.findOneWayFlights(
                        alert.end_airports,
                        alert.start_airports, 
                        alert.inbound_start, 
                        alert.inbound_end
                      )

    deals_controller = DealsController()
    deals_controller.putCrawlerResponses(outbound_flights)
    deals_controller.putCrawlerResponses(inbound_flights)

    # find the cheapest matching inbound/outbound one-way tickets
    flight_pairs = []
    for outbound_flight in outbound_flights:
      for inbound_flight in inbound_flights:
        if outbound_flight.start_airport != inbound_flight.end_airport:
          continue
        if outbound_flight.end_airport != inbound_flight.start_airport:
          continue

        price = outbound_flight.price + inbound_flight.price
        size = len(flight_pairs)
        for i in range(len(flight_pairs)):
          flight_pair = flight_pairs[i]
          if price < flight_pair[0].price + flight_pair[1].price:
            flight_pairs.insert(i, (outbound_flight, inbound_flight))
            break

        if size == len(flight_pairs):
          flight_pairs.append((outbound_flight, inbound_flight))

    # search the cheapest pairs
    responses = []
    for flight_pair in flight_pairs[:5]:
      json = requests.get(
        "https://skiplagged.com/api/search.php?from={}&to={}&depart={}&return={}&format=v2".format(
          flight_pair[0].start_airport,
          flight_pair[0].end_airport,
          flight_pair[0].outbound.strftime("%Y-%m-%d"), 
          flight_pair[1].outbound.strftime("%Y-%m-%d")
        )
      ).json()

      prices = []
      for i in json['itineraries']['outbound']:
        prices.append(i['min_round_trip_price'])

      responses.append(CrawlerResponse(
        min(prices) / 100,
        flight_pair[0].outbound,
        flight_pair[1].outbound,
        flight_pair[0].start_airport,
        flight_pair[0].end_airport,
        "https://skiplagged.com/flights/{}/{}/{}/{}".format(
          flight_pair[0].start_airport,
          flight_pair[0].end_airport,
          flight_pair[0].outbound.strftime("%Y-%m-%d"), 
          flight_pair[1].outbound.strftime("%Y-%m-%d")
        )
      ))

    return sorted(responses, key=lambda response: response.price)

  # return list of one way flights sorted by cheapest -> most expensive
  def findOneWayFlights(self, start_airports, end_airports, start_date, end_date):
    deals_controller = DealsController()
    # Gather all one way flights from start airport
    outbound_dates = [ start_date + timedelta(n) for n in range(int ((end_date - start_date).days))]
    one_way_flights = []
    for start_airport in start_airports:
      for end_airport in end_airports:
        for out_date in outbound_dates:
          db_flights = deals_controller.getOneWays(
            start_airport, end_airport, out_date.strftime("%Y-%m-%d")
          )

          if len(db_flights) == 0:
            json = requests.get("http://skiplagged.com/api/search.php?from={}&to={}&depart={}&return=&format=v2".format(
              start_airport, end_airport, out_date.strftime("%Y-%m-%d")
            )).json()
            # print page.text.encode("utf-8")
            # print raw_json
            prices = []
            for i in json['itineraries']['outbound']:
              prices.append(i['one_way_price'])

            one_way_flights.append(CrawlerResponse(
              min(prices),
              out_date,
              None,
              start_airport,
              end_airport,
              "https://skiplagged.com/flights/{}/{}/{}".format(
                start_airport, end_airport, out_date.strftime("%Y-%m-%d")
              )
            ))

          else:
            one_way_flights.append(db_flights[0])

    return sorted(one_way_flights, key=lambda response: response.price)
