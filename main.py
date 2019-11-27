# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:49:02 2019

"""
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '900')
Config.write()

zoom1 = 6
lat1=44.705362
lon1=16.974940


class MapViewApp(App):
    
     def build(self):
        global zoom1
        global lon1
        global lat1
        map = MapView(zoom=zoom1, lat=lat1, lon=lon1, double_tap_zoom = False)
        marker_1 = MapMarker(lon=17.03, lat=51.1)
        map.add_marker(marker_1)
        return map


class MainApp(App):
    def build(self): 
        MapViewApp().run()
        return 0
    
if __name__ == "__main__":
    MainApp().run()