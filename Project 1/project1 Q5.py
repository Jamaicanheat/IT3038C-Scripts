import psutil

# Get the available disk space in bytes
available_space = psutil.disk_usage('/').free

# Convert the available space to gigabytes
gb_available = round(available_space / (1024 * 1024 * 1024), 2)

print(f"You have {gb_available} GB of free disk space.")
