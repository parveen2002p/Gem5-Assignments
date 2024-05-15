from m5.params import *
from m5.SimObject import SimObject

class VectorOperations(SimObject):
    type = 'VectorOperations'
    cxx_header = "learning_gem5/part2/vector_operations.hh"
    cxx_class = "gem5::VectorOperations"
    tick1 = Param.Int(150, "Tick for vector cross product")
    tick2 = Param.Int(1500, "Tick for vector normalization")
    tick3 = Param.Int(15000, "Tick for vector subtraction")
    v1i = Param.Int(1, "val for vector")
    v1j = Param.Int(2, "val for vector")
    v1k = Param.Int(3, "val for vector")
    v2i = Param.Int(4, "val for vector")
    v2j = Param.Int(5, "val for vector")
    v2k = Param.Int(6, "val for vector")
    