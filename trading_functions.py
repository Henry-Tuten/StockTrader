import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def place_buy_order(symbol, quantity):
    # API credentials
    API_KEY = os.getenv('API_KEY')
    REDIRECT_URI = os.getenv('REDIRECT_URI')
    ACCOUNT_ID = os.getenv('ACCOUNT_ID')
    # Authentication
    auth_url = 'https://auth.tdameritrade.com/auth'
    auth_payload = {
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'client_id': API_KEY + '@AMER.OAUTHAP'
    }
    auth_response = requests.get(auth_url, params=auth_payload)
    auth_response.raise_for_status()
    auth_code = auth_response.url.split('code=')[1]

    # Access Token
    token_url = 'https://api.tdameritrade.com/v1/oauth2/token'
    token_payload = {
        'grant_type': 'authorization_code',
        'access_type': 'offline',
        'code': auth_code,
        'client_id': API_KEY,
        'redirect_uri': REDIRECT_URI
    }
    token_response = requests.post(token_url, data=token_payload)
    token_response.raise_for_status()
    access_token = token_response.json()['access_token']

    # Buy order
    buy_url = f'https://api.tdameritrade.com/v1/accounts/{ACCOUNT_ID}/orders'
    buy_payload = {
        'orderType': 'LIMIT',
        'session': 'NORMAL',
        'duration': 'DAY',
        'orderStrategyType': 'SINGLE',
        'orderLegCollection': [
            {
                'instruction': 'BUY',
                'quantity': quantity,
                'instrument': {
                    'symbol': symbol,
                    'assetType': 'EQUITY'
                }
            }
        ],
        'orderPrice': 150.0,  # Replace with the desired purchase price
    }
    headers = {'Authorization': f'Bearer {access_token}'}
    buy_response = requests.post(buy_url, json=buy_payload, headers=headers)
    buy_response.raise_for_status()

    # Print the response
    print(buy_response.json())


# Load environment variables from .env file
load_dotenv()

def place_buy_order(symbol, quantity):
    # API credentials
    api_key = os.getenv('API_KEY')
    redirect_uri = os.getenv('REDIRECT_URI')
    account_id = os.getenv('ACCOUNT_ID')

    # Code for placing the buy order (same as before)
    # ...


def place_sell_order(symbol, quantity):
    # API credentials
    api_key = os.getenv('API_KEY')
    redirect_uri = os.getenv('REDIRECT_URI')
    account_id = os.getenv('ACCOUNT_ID')

    # Sell order
    sell_url = f'https://api.tdameritrade.com/v1/accounts/{account_id}/orders'
    sell_payload = {
        'orderType': 'LIMIT',
        'session': 'NORMAL',
        'duration': 'DAY',
        'orderStrategyType': 'SINGLE',
        'orderLegCollection': [
            {
                'instruction': 'SELL',
                'quantity': quantity,
                'instrument': {
                    'symbol': symbol,
                    'assetType': 'EQUITY'
                }
            }
        ],
        'orderPrice': 0.0,  # Replace with the desired sell price
    }
    headers = {'Authorization': f'Bearer {api_key}'}
    sell_response = requests.post(sell_url, json=sell_payload, headers=headers)
    sell_response.raise_for_status()

    # Print the response
    print(sell_response.json())

def update_and_predict(new_data):
    # Append the new data to the master dataset
    updated_data = pd.concat([master_data, new_data])

    # Split the updated data into features (X) and target variable (y)
    X_updated = updated_data[['Feature1', 'Feature2', 'Feature3']]  # Replace with your actual feature columns
    y_updated = updated_data['Target']  # Replace with your actual target column

    # Retrain the model with the updated data
    model.fit(X_updated, y_updated)

    # Make predictions on the new data
    new_predictions = model.predict(new_data[['Feature1', 'Feature2', 'Feature3']])  # Replace with your actual feature columns

    return new_predictions