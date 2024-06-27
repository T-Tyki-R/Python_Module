def mood_reponse(mood = ""):
    if mood == "happy".capitalize():
        return f"Good! Continue to live joyously everyday!"
    elif mood == "sad".capitalize():
        return f"Although things may lead to sadness, You only need a spark of positivity to make a rainy day a brighter one"
    elif mood == "upset".capitalize():
        return f"Its better and healthier to remain calm and collected. Anger can lead to serious health issues."
    else:
        return f"I'm afraid I don't have any response to that mood"

