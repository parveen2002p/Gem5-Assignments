
import m5
from m5.objects import *

system = System()

system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()


system.mem_mode = 'timing'              
system.mem_ranges = [AddrRange('512MB')]

system.cpu = TimingSimpleCPU()

# cache prep

class L2Cache(Cache):
    size = '256kB'
    assoc = 4
    tag_latency = 10
    data_latency = 10
    response_latency = 10
    mshrs = 20
    tgts_per_mshr = 12

    def attachToBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def attachToMem(self, bus):
        self.mem_side = bus.cpu_side_ports

class L1ICache(Cache):
    size = '16kB'
    assoc = 2
    tag_latency =2
    data_latency =2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20

    def attachToCpu(self, cpu):
        self.cpu_side = cpu.icache_port
    
    def attachToBus(self, bus):
        self.mem_side = bus.cpu_side_ports

class L1DCache(Cache):
    size = '16kB'
    assoc = 2
    tag_latency =2
    data_latency =2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20

    def attachToCpu(self, cpu):
        # cpu has port it has wire
        self.cpu_side = cpu.dcache_port
    
    def attachToBus(self, bus):
        # bus has port it has wire
        self.mem_side = bus.cpu_side_ports




# create object of them & use theese objects to call func or assign port also for membus & l2bus
L1I=L1ICache()
L1D=L1DCache()
system.cpu.icache = L1I
system.cpu.dcache = L1D


L1I.attachToCpu(system.cpu)
L1D.attachToCpu(system.cpu)

# bus to connect l1 to l2 as l2 has 1 port only
L2Bus=L2XBar()
system.l2bus = L2Bus
L1I.attachToBus(L2Bus)
L1D.attachToBus(L2Bus)

# l2 created & cpu attached to membus & membus attached to l2bus
L2 = L2Cache()
system.l2cache = L2
L2.attachToBus(L2Bus)
MemBus=SystemXBar()
system.membus = MemBus
L2.attachToMem(MemBus)


system.cpu.createInterruptController()


system.cpu.interrupts[0].pio = MemBus.mem_side_ports
system.cpu.interrupts[0].int_requestor = MemBus.cpu_side_ports
system.cpu.interrupts[0].int_responder = MemBus.mem_side_ports



system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = MemBus.mem_side_ports


system.system_port = MemBus.cpu_side_ports




binary_path = "/home/jmd/miben/mibench/automotive/qsort/qsort_small"
input_path = "/home/jmd/miben/mibench/automotive/qsort/input_small.dat"
system.workload = SEWorkload.init_compatible(binary_path)

process = Process()
process.cmd = [binary_path,input_path]
system.cpu.workload = process
system.cpu.createThreads()


root = Root(full_system = False, system = system)
m5.instantiate()

print("Beginning your simulation!")
exit_event = m5.simulate()
print("BYE BYE 2 ")
print('Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause()))
