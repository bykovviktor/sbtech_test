import csv
from  Config.variables import *

class card:
    def __init__(self, cardNum):
        self.cardNum = cardNum

    def check_card_data(self):
        cardValidation = True
        message = ""
        code = 200
        if self.cardNum.isdigit():
            print (len(self.cardNum))
            if len(str(self.cardNum)) < 16 or len(str(self.cardNum)) > 20:
                cardValidation = False
                message = f"Card number length is incorrect. Please check"
                code = 500
        else:
            cardValidation = False
            message = f"Card number must contain digits only"
            code = 500

        response = {"message": message, "code": code, "result": cardValidation}

        return response


    def get_bank_data(self):
        checkResult = self.check_card_data()
        binCode = self.cardNum[0:6]
        if not checkResult["result"]:
            return checkResult["message"], checkResult["code"]

        bankData = list()
        global banksDatabase
        for row in banksDatabase:
            if row["bin"] == binCode:
                bankData.append(row)

        if len(bankData) > 0:
            response = {
                "message": {"card data": bankData},
                "code": 200}
        else:
            print (f"bin code {binCode} not found in database")
            response = {
                "message": f"bin code {binCode} not found in database",
                "code": 500
            }

        return response["message"], response["code"]

global banksDatabase

try:
    banksDatabase = list()
    with open(binlistFile) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            banksDatabase.append(row)

except Exception as error:
    print (f"error during load binListFile: {error}")
