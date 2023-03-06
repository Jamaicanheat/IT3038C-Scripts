import win32com.client

# Create an instance of Excel
excel = win32com.client.Dispatch('Excel.Application')

# Open a workbook
workbook = excel.Workbooks.Open('path/to/workbook')

# Load the plugin
plugin = workbook.Application.AddIns.Add('path/to/plugin')

# Call a function in the plugin
result = plugin.Run('function_name', arg1, arg2, arg3)

# Display the result
print(result)

# Close the workbook and Excel
workbook.Close()
excel.Quit()
