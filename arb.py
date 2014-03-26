import requests, time, datetime

btce_raw = {}
bitfinex_raw = {}
btcsx_raw = {}

btce_raw['btcusd'] = requests.get('https://btc-e.com/api/2/btc_usd/ticker').json()
btce_raw['ltcusd'] = requests.get('https://btc-e.com/api/2/ltc_usd/ticker').json()
btce_raw['ltcbtc'] = requests.get('https://btc-e.com/api/2/ltc_btc/ticker').json()
bitfinex_raw['btcusd'] = requests.get('https://api.bitfinex.com/v1/ticker/btcusd').json()
bitfinex_raw['ltcusd'] = requests.get('https://api.bitfinex.com/v1/ticker/ltcusd').json()
bitfinex_raw['ltcbtc'] = requests.get('https://api.bitfinex.com/v1/ticker/ltcbtc').json()
btcsx_raw['btcusd'] = requests.get('https://btc.sx/api/ticker.php').json()

btce = {}
btce['buy'] = {}
btce['sell'] = {}
bitfinex = {}
bitfinex['buy'] = {}
bitfinex['sell'] = {}
btcsx = {}
btcsx['buy'] = {}
btcsx['sell'] = {}

btce['buy']['btcusd'] = float(btce_raw['btcusd']['ticker']['buy'])
btce['sell']['btcusd'] = float(btce_raw['btcusd']['ticker']['sell'])
btce['buy']['ltcusd'] = float(btce_raw['ltcusd']['ticker']['buy'])
btce['sell']['ltcusd'] = float(btce_raw['ltcusd']['ticker']['sell'])
btce['buy']['ltcbtc'] = float(btce_raw['ltcbtc']['ticker']['buy'])
btce['sell']['ltcbtc'] = float(btce_raw['ltcbtc']['ticker']['sell'])
bitfinex['buy']['btcusd'] = float(bitfinex_raw['btcusd']['ask'])
bitfinex['sell']['btcusd'] = float(bitfinex_raw['btcusd']['bid'])
bitfinex['buy']['ltcusd'] = float(bitfinex_raw['ltcusd']['ask'])
bitfinex['sell']['ltcusd'] = float(bitfinex_raw['ltcusd']['bid'])
bitfinex['buy']['ltcbtc'] = float(bitfinex_raw['ltcbtc']['ask'])
bitfinex['sell']['ltcbtc'] = float(bitfinex_raw['ltcbtc']['bid'])
btcsx['buy']['btcusd'] = float(btcsx_raw['btcusd']['buyprice'])
btcsx['sell']['btcusd'] = float(btcsx_raw['btcusd']['sellprice'])

# print('btce ' + unicode(btce))
# print('bitfinex ' + unicode(bitfinex))

print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

for instrument in btce['buy']:
	buy_price = btce['buy'][instrument]
	sell_price = bitfinex['sell'][instrument]
	# print 'instrument ' + instrument + '\tsell_price: ' + unicode(sell_price) + '\tbuy_price: ' + unicode(buy_price) + '\tsell > buy ' + unicode(sell_price > buy_price)
	if sell_price > buy_price:
		print 'buy ' + instrument + ' on btce for ' + unicode(buy_price) + ' and sell on bitfinex for ' + unicode(sell_price) 

for instrument in bitfinex['buy']:
	buy_price = bitfinex['buy'][instrument]
	sell_price = btce['sell'][instrument]
	# print 'instrument ' + instrument + '\tsell_price: ' + unicode(sell_price) + '\tbuy_price: ' + unicode(buy_price) + '\tsell > buy ' + unicode(sell_price > buy_price)
	if sell_price > buy_price:
		print 'buy ' + instrument + ' on bitfinex for ' + unicode(buy_price) + ' and sell on btce for ' + unicode(sell_price) 

for instrument in btcsx['buy']:
	buy_price = btcsx['buy'][instrument]
	sell_btce = btce['sell'][instrument]
	sell_bitfinex = btce['sell'][instrument]
	if sell_btce > buy_price:
		print 'buy ' + instrument + ' on btcsx for ' + unicode(buy_price) + ' and sell on btce for ' + unicode(sell_btce)
	if sell_bitfinex > buy_price:
		print 'buy ' + instrument + ' on btcsx for ' + unicode(buy_price) + ' and sell on bitfinex for ' + unicode(sell_bitfinex)

for instrument in btcsx['sell']:
	sell_price = btcsx['sell'][instrument]
	buy_btce = btce['buy'][instrument]
	buy_bitfinex = btce['sell'][instrument]
	if sell_price > buy_btce:
		print 'buy ' + instrument + ' on btce for ' + unicode(buy_btce) + ' and sell on btcsx for ' + unicode(sell_price)
	if sell_bitfinex > buy_price:
		print 'buy ' + instrument + ' on bitfinex for ' + unicode(buy_bitfinex) + ' and sell on btcsx for ' + unicode(sell_price)

btce_graph = {}
bitfinex_graph = {}

