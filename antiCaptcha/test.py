import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', '0a3216b825eb47efe9fb8ef6b4d8cb2b')

solver = TwoCaptcha(api_key)

try:
    result = solver.hcaptcha(
        sitekey='3ceb8624-1970-4e6b-91d5-70317b70b651',
        url='https://testnet.bnbchain.org/faucet-smart',
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))

    