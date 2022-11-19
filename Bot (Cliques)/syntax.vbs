Dim wshShell
Set wshShell = CreateObject("WScript.shell")


WScript.Sleep(40000)
wshShell.Run("fix.bat") 
