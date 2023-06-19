from django.shortcuts import render
from polygon import RESTClient
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import environ


env = environ.Env()
environ.Env.read_env() 


client = RESTClient(api_key=env('API_KEY'))

class StockRequest(APIView):
    def post(self, request):
        # Process student data
        ticker = request.data

        # # Determine the requested functionality
        # functionality = request.data.get('functionality')

        # # Call the corresponding function based on the requested functionality
        # if functionality == 'trade':
        #     response_data = self.process_trade(ticker)
        # elif functionality == 'quote':
        #     response_data = self.process_quote(ticker)
        # # elif functionality == 'courses':
        # #     response_data = self.process_courses(ticker)
        # else:
        #     response_data = {'error': 'Invalid functionality specified.'}

        # return Response(response_data)

    def process_trade(self, ticker):
        # Your logic to process trade
        
        trade = client.get_last_trade(ticker=ticker)

        return HttpResponse(trade)

    def process_quote(self, ticker):
        # Your logic to process quote
        quote = client.get_last_quote(ticker=ticker)

        return HttpResponse(quote)

    # def process_courses(self, ticker):
    #     # Your logic to process courses
    #     courses = ...

    #     return courses
