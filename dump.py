import swd
import struct

dev = swd.Swd()
cm = swd.CortexM(dev)

ver = dev.get_version().str
print(f'ST-Link Version: {ver}')

voltage = dev.get_target_voltage()
print(f'Target voltage: {voltage}')

idcode = hex(dev.get_idcode())
print(f'Target IDCODE: {idcode}')

print("\nResetting...\n")
cm.reset_halt()

print("Dumping firmware...\n")

with open("dump.bin", "wb") as f:
    for addr in range(0, int("0x40000",16), 4):        
        cm.set_reg('PC', 0xbeef) # CHANGE HERE ACCORDINGLY 
        cm.set_reg('R4', addr)
        cm.step()
        instr = struct.pack("I",cm.get_reg('R4'))
        f.write(instr)

print("Done")

# (gdb) set $pc = 0x6d4
# (gdb) set $r4 = 0x10
# (gdb) si
# 0x000006d6 in ?? ()
# (gdb) i r
