from seismem import SeisMem


SM = SeisMem()
# Add multiple files to the storage object.
SM.add_file("test0.SAC")
SM.add_file("test1.SAC")
# Save the storage object to a single file.
SM.dump("test.json")

SM2 = SeisMem()
# Load a SeisMem storage object from file.
SM2.load("test.json")

keys = SM2.storage.keys()
print(keys)
test_trace = SM2.storage[list(keys)[0]]
test_trace.plot()
