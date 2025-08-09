#@author uakabibara01
#@category Export
#@keybinding
#@menupath
#@toolbar

output_file = askFile("Export function list to", "Save")

with open(output_file.absolutePath, "w", encoding="utf-8") as f:
    functionManager = currentProgram.getFunctionManager()
    functions = functionManager.getFunctions(True)
    
    for func in functions:
        entry = func.getEntryPoint()
        name = func.getName()
        sig = func.getPrototypeString(True, False)
        f.write(f"{entry}: {sig}\n")