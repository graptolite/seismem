Load multiple obspy seismic streams into one dictionary object. This dictionary can be saved to disk in one file to avoid having many small stream files, and reread into SeisMem object. This saving is done by formatting the loaded [obspy](https://github.com/obspy/obspy) stream objects into SAC format, Base64 encoding them into a string, and then saving in json format.

# Usage
See also `example.py` for a demonstration of SeisPy.
1. Initialize a `SM = SeisMem()` instance (the variable name can be changed).
2. Either add streams to the instance `SM` (in which case the stream must also be given a unique name - e.g. seismic archive file name format - unless it's to overwrite an existing named stream), or add files to the instance (in which case the file path will be used for the name).
3. To retrieve a stream from `SM` storage by name, use `SM.storage[<stream name>]`.
4. `SM.dump(<filename>)` saves the current state of the `SM` storage (stream collection) to disk.
