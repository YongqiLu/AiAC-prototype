detected_labels = ['aac']

label_commands = {
    'aac': 'G', 'nail': 'R', 'wood': 'Y', 'aac_nail_wood': 'A', 'none': '0'
}

if 'aac' in detected_labels and not 'nail' in detected_labels and not 'wood' in detected_labels:
    command = label_commands['aac']
elif 'nail' in detected_labels and 'wood' in detected_labels:
    command = label_commands['aac_nail_wood']
elif 'nail' in detected_labels:
    command = label_commands['nail']
elif 'wood' in detected_labels:
    command = label_commands['wood']
else:
    command = label_commands['none']
    
print(f"Detected Labels: {detected_labels}")
print(f"Sending command to Arduino: {command}")

