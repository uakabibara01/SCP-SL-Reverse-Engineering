# @author uakabibara01
# @category Export
# @keybinding
# @menupath
# @toolbar

from ghidra.program.model.listing import CodeUnit
from ghidra.app.script import GhidraScript

output_file = askFile("Export entire ASM to", "Save")

with open(output_file.absolutePath, "w", encoding="utf-8") as f:
    listing = currentProgram.getListing()
    for instr in listing.getInstructions(True):
        addr = instr.getAddress()
        mnemonic = instr.getMnemonicString()
        op_str = instr.toString()  
        f.write(f"{addr}:\t{mnemonic} {op_str}\n")

print("Export completed:", output_file.absolutePath)
