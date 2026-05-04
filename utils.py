def control_device(action):
    if action == "Light ON":
        return "💡 Light turned ON"
    elif action == "Fan ON":
        return "🌀 Fan turned ON"
    elif action == "Light OFF":
        return "💡 Light turned OFF"
    else:
        return "❌ No Action"