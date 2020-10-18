
Set SHELL = CreateObject("WScript.Shell")
Set FS = CreateObject("Scripting.FileSystemObject")
Set INFOLDER = FS.GetFolder("./in")
CMD = "Python jsonToXml.py"

Function GetNewestFile(folder)
  Dim newestFile
  For Each file in folder.Files
    If newestFile = "" Then
      Set newestFile = file
    Else
      If newestFile.DateCreated < file.DateCreated Then
        Set newestFile = file
      End If
    End If
  Next
  GetNewestFile = newestFile.Name
End Function

msgbox(GetNewestFile(INFOLDER))