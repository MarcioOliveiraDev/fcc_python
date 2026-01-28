test_settings = {
    'theme': 'dark',
    'language': 'portuguese',
    'notification': 'blablabla'
}

def add_setting(setting, pair):
    
    key, value = pair[0].lower(), pair[1].lower()

    if key in setting:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    if key not in setting:
        setting[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(setting, pair):
    key, value = pair[0].lower(), pair[1].lower()

    if key in setting:
        setting[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    if key not in setting:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(setting, key):
    key = key.lower()

    if key in setting:
        del setting[key]
        return f"Setting '{key}' deleted successfully!"
    
    if key not in setting:
        return f"Setting not found!"
    
def view_settings(setting):
    if setting == {}:
        return "No settings available."
    
    if setting:
        text = "Current User Settings:\n"
        for key, value in setting.items():
            text += f"{key.capitalize()}: {value}\n"
        return text
