import datetime as dt

class Strategy():
    def __init__(self, portfolio, prices, buy_threshold, sell_threshold):
        self.prices = prices

            #Dictionary {Ticker : [(Date, Price), (Date+1, Price), ...]        }

        self.suggested_moves = {}
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold
        self.apple_price = prices["AAPL"]

        self.apple_price_dict = {}
        for curr_date, curr_price in self.apple_price:
            self.apple_price_dict[curr_date] = curr_price

        self.holding_stock = False
        self.sell_price = 0

    
    def strategize(self, date):
        
        #Asks itself, "Should I buy Apple on this date?"
        print("strategize on", date)

        todays_price = self.apple_price_dict[dt.datetime.strftime(date, "%Y-%m-%d")]
        yesterdays_price = self.apple_price_dict[dt.datetime.strftime(date - dt.timedelta(days = 1), "%Y-%m-%d")]
        self.suggested_moves["AAPL"] = 0

        pctchange = (todays_price / yesterdays_price) - 1

        if self.holding_stock == False:
            #if percentage change is lower than buy percentage but not *100 (eg -0.02)
            if pctchange <= self.buy_threshold:
                self.suggested_moves["AAPL"] = 1
                self.holding_stock = True
                self.sell_price = (todays_price * (1 + self.sell_threshold))

        if self.holding_stock == True:
            if todays_price >= self.sell_price:
                self.suggested_moves["AAPL"] = -1
                self.holding_stock = False

        return self.suggested_moves
