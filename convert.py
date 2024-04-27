# Open the text file and read the private keys
with open('Only-private-keys.txt', 'r') as file:
    priv_keys = file.readlines()

# Format the private keys into the desired command format
formatted_keys = [f'importprivkey {key.strip()} "" false\n' for key in priv_keys]

# Write the formatted commands to a new file
with open('command_file.txt', 'w') as file:
    file.writelines(formatted_keys)
