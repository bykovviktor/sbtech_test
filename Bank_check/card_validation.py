import csv

from  Config.variables import *



class Card:
    def __init__(self):
        self.banksDatabase = list()
        self.read_csv()

    def check_card_data(self, cardNum):
        """
        Check main paramaters of card number:
        length must be >=16 and <=20
        card number must contain only digits
        """

        cardValidation = True
        message = ""
        code = 200
        if cardNum.isdigit():
            print (len(cardNum))
            if len(str(cardNum)) < 16 or len(str(cardNum)) > 20:
                cardValidation = False
                message = f"Card number length is incorrect. Please check"
                code = 500
        else:
            cardValidation = False
            message = f"Card number must contain digits only"
            code = 500

        response = {"message": message, "code": code, "result": cardValidation}

        return response


    def get_bank_data(self, cardNum):
        """getting data from file/variable by card number. This function
        validate card number and tries to find it in database.
        """
        checkResult = self.check_card_data(cardNum)
        binCode = cardNum[0:6]
        if not checkResult["result"]:
            return checkResult["message"], checkResult["code"]

        bankData = list()

        for row in self.banksDatabase:
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


    def read_csv(self):
        #try:
        with open(binlistFile, encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                try:
                    self.banksDatabase.append(row)
                except Exception as error:
                    break

        #except Exception as error:
        #    print(f"error during load binListFile: {error}")
