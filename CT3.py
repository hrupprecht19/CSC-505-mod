#Defines the screen names
#Prints the total number of screens
#Prints the navigation flow (e.g., "Home → Add Item → Save → View List")
#Optionally includes descriptions of what each screen does
# Module 3: Critical Thinking Assignment
Mod3_CT_Dict = {
    'Page 1': 'Shark Shopping',
    'Page 2': 'Add to Catch',
    'Page 3': 'View Haul',
    'Page 4': 'Edit Catch',
    'Page 5': 'Ocean Settings'
}

print('Screen Names:')
for page, description in Mod3_CT_Dict.items():
    print(description)

print('Total number of screens:', len(Mod3_CT_Dict))

# Explicit directed transitions as requested by the flow
transitions = [
    ('Shark Shopping', 'Add to Catch'),
    ('Add to Catch', 'View Haul'),
    ('View Haul', 'Edit Catch'),
    ('Shark Shopping', 'Ocean Settings'),
]

# Validate transitions reference existing screens
screen_set = set(Mod3_CT_Dict.values())
print('\nDirected Flow:')
for src, dst in transitions:
    if src not in screen_set or dst not in screen_set:
        print(f'Warning: Unknown screen in transition {src} → {dst}')
    else:
        print(f'{src} → {dst}')
