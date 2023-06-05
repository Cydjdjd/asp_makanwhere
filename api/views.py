from django.shortcuts import render
import pip._vendor.requests
import googlemaps
import json
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from dotenv.main import load_dotenv

load_dotenv()  # take environment variables from .env


# Retrieves list of restaurants from Google Maps API
class GoogleMapsAPIView(APIView):
    permission_classes = [
        permissions.AllowAny
    ]  # Allow any user (authenticated or not) to access this api
    api_key = os.getenv("G_API_KEY")  # Google Maps API Key
    gmaps = googlemaps.Client(key=api_key)  # Google Maps Client

    def post(self, request):
        location = request.data["location"]  # user location input
        distance = request.data["distance"]  # distance from user location

        if location != "" and distance != "":
            geocode_result = self.gmaps.geocode(
                location
            )  # get lat and lng from location
            lat = geocode_result[0]["geometry"]["location"]["lat"]
            lng = geocode_result[0]["geometry"]["location"]["lng"]
            url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={str(lat)}%2C{str(lng)}&radius={str(distance)}&type=restaurant&key={self.api_key}"

            # Google Maps API request
            payload = {}
            headers = {}
            response = pip._vendor.requests.api.request(
                "GET", url, headers=headers, data=payload
            )
            response = json.loads(response.text)
            restaurant = []  # list of restaurants

            # add restaurant names to list
            for i in range(len(response["results"])):
                restaurant.append(response["results"][i]["name"])

            # return list of restaurants
            return Response(restaurant, status=status.HTTP_200_OK)

        else:
            return Response(
                "Please enter a location and distance",
                status=status.HTTP_400_BAD_REQUEST,
            )
