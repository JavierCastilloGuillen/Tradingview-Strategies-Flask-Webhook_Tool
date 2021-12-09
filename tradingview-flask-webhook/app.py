from flask import Flask, request
import ccxt
import config


app = Flask(__name__)


# Connection to Exchange
exchange = ccxt.binance({
    'apiKey': config.API_KEY, 
    'secret': config.API_SECRET})




# WEBHOOK MESSAGE 
@app.route("/alert", methods=['POST'])

def alerta():
    msg = request.json
    if msg['password'] != config.PASSWORD:
        return { 'code': 'error',
                'message': 'User not authorized'
        }
    print(msg)

    # order = exchange.create_limit_order( msg['ticker'], msg['side'] , 0, msg['close'] , params={})
    
    return {
        'code' : 'Success',
        'msg': msg
    }

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)#, debug=True)
   