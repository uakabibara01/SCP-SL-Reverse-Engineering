# -*- coding: utf-8 -*-
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.app.decompiler import DecompInterface
from ghidra.program.model.symbol import SymbolType
from ghidra.util import Msg
import os

monitor = ConsoleTaskMonitor()
decompiler = DecompInterface()
decompiler.openProgram(currentProgram)

symtab = currentProgram.getSymbolTable()
outputDir = askDirectory("Select output directory", "OK")
exported = 0

for symbol in symtab.getAllSymbols(True):
    if symbol.getSymbolType() != SymbolType.FUNCTION:
        continue
    name = symbol.getName()
    if not name.startswith("FUN_"):
        continue

    func = getFunctionAt(symbol.getAddress())
    if not func:
        continue

    results = decompiler.decompileFunction(func, 120, monitor)
    if not results.decompileCompleted():
        Msg.warn(None, "Failed: %s" % name)
        continue

    dec = results.getDecompiledFunction().getC()
    filename = os.path.join(outputDir.getAbsolutePath(), "%s.c" % name)
    try:
        with open(filename, "wb") as f:
            f.write(dec.encode("utf-8"))
    except IOError as e:
        Msg.warn(None, "Permission error writing %s: %s" % (filename, e))
        continue

    exported += 1
    Msg.info(None, "Exported: %s" % name)

Msg.info(None, "TOTAL exported: %d into %s" % (exported, outputDir.getAbsolutePath()))
