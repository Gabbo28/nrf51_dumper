# nrf51_dumper

Script for dumpig Nordic nrf51 SoCs' internal flash memory, bypassing Code Read Protection (CRP).

The gadget instruction address at line 23, and the corresponding register, need to be changed accordingly to the target's code.
(The script doesn't find the gadget, otherwise where's the fun? :) )

## Requiremets

- [pyswd](https://github.com/cortexm/pyswd): python module for debugging microcontrollers with SWD using ST-Link/V2 (/V2-1) or V3 debugger.
- ST-Link V2/V3 debugger
