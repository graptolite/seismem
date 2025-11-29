from seismem import SeisMem


SM = SeisMem()
# Add multiple files to the storage object.
SM.add_file("test0.SAC")
SM.add_file("test1.SAC")
# Save the storage object to a single file.
SM.dump("test.json")

# Load a SeisMem storage object from file.
SM2 = SeisMem(load_file="test.json")
keys = SM2.list_stream_names()
print(keys)
test_trace = SM2.get(list(keys)[0])
test_trace.plot()
