import csv


class Card:
    def __init__(self, path=None):
        self.path = path
        self.banksDatabase = self.read_csv()


    def check_card_data(self, cardNum):
        """
        Check main paramaters of card number:
        length must be >=16 and <=20
        card number must contain only digits
        """

        cardValidation = True
        message = "Validation OK"
        code = 200

        if cardNum.isdigit():
            if not 16<=len(str(cardNum))<=20:
                cardValidation = False
                message = f"Card number length is incorrect. Please check it. Card number must be 16-20 digits. Your card number has {len(str(cardNum))} digits"
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

        if not checkResult["result"]: #if validation is not successfull, return error message and code 500
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
            response = {
                "message": {"card data": "Unknown card"},
                "code": 500
            }

        return response["message"], response["code"]


    def read_csv(self):

        """Open bank datafile and return it as a dict"""

        bankDb = list()

        try:
            with open(self.path, encoding="utf8") as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    bankDb.append(row)

            return bankDb

        except Exception as error:
            print(f"error during load binListFile: {error}")