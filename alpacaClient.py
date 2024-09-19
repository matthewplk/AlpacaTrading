# from alpaca.trading.client import TradingClient
# from alpaca.trading.requests import GetAssetsRequest
# from alpaca.trading.enums import AssetClass

# trading_client = TradingClient(PUBLIC_KEY, PRIVATE_KEY)

# #Get account information.
# account = trading_client.get_account()

# if account.trading_blocked:
#     print('Account is currently restricted from trading.')

# search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
# assets

# print('${} is available as buying power.'.format(account.buying_power))

# #Check our current balance vs. our balance at the last market close.
# balance_change = float(account.equity) - float(account.last_equity)
# print(f'Today\'s portfolio balance change: ${balance_change}')
