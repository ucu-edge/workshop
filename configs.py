class Config:
    def __init__(self, config):
        self._config = config

    def get_property(self, property_name):
        if property_name not in self._config.keys():  # we don't want KeyError
            return None  # just return None if not found
        return self._config[property_name]


class LSTMConfig(Config):

    @property
    def verbose(self):
        return self.get_property('verbose')

    @property
    def epochs(self):
        return self.get_property('epochs')

    @property
    def batch_size(self):
        return self.get_property('batch_size')

    @property
    def loss(self):
        return self.get_property('loss')

    @property
    def optimizer(self):
        return self.get_property('optimizer')
    
    @property
    def layers(self):
        return self.get_property('layers')


class CNNLSTMConfig(Config):
    pass


class ConvLSTMConfig(Config):
    pass
