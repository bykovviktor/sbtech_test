from quart import Quart, jsonify, request
import time

from Bank_check.card_validation import Card

import logging
import os



class BankCheckRunner:
    def __init__(self, host, port):
        self.app = None
        self.port = port
        self.host = host
        self.card = Card()

        self.init_quart()


    def init_quart(self):
        self.app = Quart(self.__class__.__name__)

        @self.app.route('/', methods=['GET'])
        async def hello():
            check_time = time.strftime("%Y-%m-%d %H:%M:%S")
            return '<b>' + check_time + '</b>' + ' : Hello. This is ' + self.__class__.__name__

        @self.app.route('/card/<cardNum>', methods=['GET'])
        async def check_cardnum(cardNum):
            validation = self.card.get_bank_data(cardNum)
            return validation


    def run(self):
        self.app.run(host=self.host, port=self.port)
        return


if __name__ == '__main__':
    app = BankCheckRunner(host='0.0.0.0', port=8080)
    app.run()
