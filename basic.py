#This file will contain information to display basic information.
import pandas as pd
import numpy as np

#This class will be used to pull weather information for me
class Weather():

    #I was using this method to set up the initial attribute but I needed
    #to reset the attribute each time I used it. 
    # def __init__(self):
    #     pass
    #self.__data = pd.read_csv('weather.csv')

    #This method will get the average mean temperature per day.
    def get_mean_temp(self):
        self.__data = pd.read_csv('weather.csv')
        self.__data = self.__data[[1]]
        mean = self.__data['actual_mean_temp'].mean()
        return mean

    #This method will get the average mean high temperature per day.
    def get_mean_high_temp(self):
        self.__data = pd.read_csv('weather.csv')
        self.__data = self.__data[[3]]
        high_mean = self.__data['actual_max_temp'].mean()
        return high_mean

    #This method will get the average mean low temperature per day.
    def get_mean_low_temp(self):
        self.__data = pd.read_csv('weather.csv')
        self.__data = self.__data[[2]]
        low_mean = self.__data['actual_min_temp'].mean()
        return low_mean

    #This method will get the average mean rain per day.
    def get_mean_rain(self):
        self.__data = pd.read_csv('weather.csv')
        self.__data = self.__data[[10]]
        rain_mean = self.__data['actual_precipitation'].mean()
        return rain_mean



#### Practice code here ######
#Code ideas that I tried out.
# weather = Weather()
# weather.get_mean_rain()
# print(data._Weather__age)
#print(weather._Weather__data.get_mean_temp())
# print(weather.get_mean_high_temp())
#print(weather.get_mean_temp())
