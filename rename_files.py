import os

def replace_spaces_with_underscores(directory):
    # Gehe durch alle Dateien und Unterordner im angegebenen Verzeichnis
    for root, dirs, files in os.walk(directory, topdown=False):
        # Benenne Dateien um
        for name in files:
            if ' ' in name:
                old_path = os.path.join(root, name)
                new_name = name.replace(" ", "_")
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f"Datei umbenannt: {old_path} -> {new_path}")
        
        # Benenne Unterordner um
        for name in dirs:
            if ' ' in name:
                old_path = os.path.join(root, name)
                new_name = name.replace(" ", "_")
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f"Ordner umbenannt: {old_path} -> {new_path}")

if __name__ == "__main__":
    directory = "/Volumes/SSK Storage/NutritionـandـLifestyleـinـPregnancy"  # Ersetze dies mit dem Pfad zu deinem Verzeichnis
    replace_spaces_with_underscores(directory)
