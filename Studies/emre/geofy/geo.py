from osgeo import gdal
import numpy as np


class Geo():
    def __init__(self):
        self.src_filename = r'C:\Users\emrea\Desktop\'22 codes\deep-ternaloc\deep-ternaloc\Studies\emre\data\n38_e038_1arc_v3.dt2'
        
        
        
        
    def readAsArray(self):
        self.src_ds=gdal.Open(self.src_filename) 
        self.gt=self.src_ds.GetGeoTransform()
        self.rb=self.src_ds.GetRasterBand(1)
        self.data_array = self.src_ds.ReadAsArray()
        self.data_array=self.data_array.astype(int)[:,:]
        return self.data_array