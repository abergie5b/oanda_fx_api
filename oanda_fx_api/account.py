from oanda_fx_api.config import Config
import os


class Account:
    def __init__(self, account=0): 
        self.id = os.getenv('OANDA_FX_USER')  # account id
        self.token = os.getenv('OANDA_FX_KEY')
        
        self.venue = Config.practice_venue  # api endpoint
        self.candles_venue = self.venue + "/v1/candles"
        self.streaming = Config.streaming_venue
        self._id_url = Config.account_url + self.id
        
        self.orders =  self._id_url + '/orders/'
        self.positions = self._id_url + "/positions/"
        self.headers = {'Authorization': 'Bearer %s' % self.token}

    def __str__(self):
        return "[=> %s (%s)" % (self.venue, self.id)

    def __repr__(self):
        return self.__str__()
