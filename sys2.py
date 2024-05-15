import m5
from m5.objects import *
root = Root(full_system = False)

from optparse import OptionParser
parser = OptionParser()

parser.add_option("-a", "--tick1", dest="tick1", type="int")
parser.add_option("-b", "--tick2", dest="tick2", type="int")
parser.add_option("-c", "--tick3", dest="tick3", type="int")


(options, args) = parser.parse_args()

v1i=int(input("Enter vector 1 1st Dimension value: ")) 
v1j=int(input("Enter vector 1 2nd Dimension value: ")) 
v1k=int(input("Enter vector 1 3rd Dimension value: ")) 

v2i=int(input("Enter vector 2 1st Dimension value: ")) 
v2j=int(input("Enter vector 2 2nd Dimension value: ")) 
v2k=int(input("Enter vector 2 3rd Dimension value: ")) 


if not options.tick1:
    options.tick1=150
if not options.tick2:
    options.tick2=1500
if not options.tick3:
    options.tick3=15000

# print(options.tick1)
# print(options.tick2)
# print(options.tick3)

root.vector_operation = VectorOperations(tick1=options.tick1,tick2=options.tick2,tick3=options.tick3,v1i=v1i,v1j=v1j,v1k=v1k,v2i=v2i
                              ,v2j=v2j,v2k=v2k)
m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'
      .format(m5.curTick(), exit_event.getCause()))