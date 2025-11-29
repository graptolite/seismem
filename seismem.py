'''
    SeisMem | Load multiple obspy seismic streams into one dictionary object.
    Copyright (C) 2025  Yingbo Li

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import obspy
from io import BytesIO
import os
import json
import base64

def obspy2bytes(obspy_obj):
    store = BytesIO()
    obspy_obj.write(store,format="SAC")
    store.seek(0)
    b = store.read()
    store.close()
    return b

def obspy2bytesstr(obspy_obj):
    b = obspy2bytes(obspy_obj)
    s = base64.b64encode(b).decode()
    return s

def bytesstr2obspy(bytesstr):
    b = BytesIO(base64.decodebytes(bytesstr.encode("ascii")))
    o = obspy.read(b)
    return o

class SeisMem():
    def __init__(self,load_file=None):
        self.storage = {}
        if load_file:
            try:
                self.load(load_file)
            except:
                print("Failed to load",str(load_file))
        return
    def __add__(self,other):
        self.storage = self.storage | other.storage
        return
    def add(self,stream,name):
        self.storage[name] = stream
    def add_file(self,stream_path):
        name = os.path.basename(stream_path)
        stream = obspy.read(stream_path)
        self.add(stream,name)
        return
    def list_stream_names(self):
        return list(self.storage.keys())
    def get(self,stream_name):
        return self.storage[stream_name]
    def dump(self,out):
        str_storage = {k:obspy2bytesstr(v) for k,v in self.storage.items()}
        with open(out,"w") as outfile:
            json.dump(str_storage,outfile,indent=2)
        return
    def load(self,load_file,replace=False):
        with open(load_file) as infile:
            str_storage = json.load(infile)
        storage = {k:bytesstr2obspy(v) for k,v in str_storage.items()}
        if replace:
            self.storage = storage
        else:
            self.storage = storage | self.storage
        return
