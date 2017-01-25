#This file will contain information to display basic information.
import pandas as pd
import numpy as np

class Weather():

    def __init__(self):
        self.__data = pd.read_csv('weather.csv')

    def get_mean_temp(self):
        self.__data = self.__data[[1]]
        print(self.__data)


# def mean_temp():
#     pass

# class Weather():
#
#     def __init__(self):
#         self.data = pd.read_csv('weather.csv')
#
#     def get_mean_temp(self):
#         self.data = self.data[[1]]
#         print(self.data)


#Code ideas that I tried out.
weather = Weather()
# print(data._Weather__age)
#print(weather._Weather__data.get_mean_temp())
print(weather.get_mean_temp())
#print(weather.get_mean_temp())
