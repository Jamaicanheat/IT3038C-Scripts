import win32com.client

# Create an instance of Photoshop
psApp = win32com.client.Dispatch('Photoshop.Application')

# Get the active document
doc = psApp.ActiveDocument

# Load the plugin
plugin = psApp.LoadExtension('path/to/plugin')

# Call a function in the plugin
result = plugin.Run('function_name', arg1, arg2, arg3)

# Display the result
print(result)
