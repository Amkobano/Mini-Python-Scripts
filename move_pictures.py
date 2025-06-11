import os
import shutil

def move_files_from_subfolders(source_folder, destination_folder):
    # Erstelle das Zielverzeichnis, wenn es nicht existiert
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Gehe durch alle Unterordner im Quellverzeichnis
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)

            # Verschiebe die Datei in das Zielverzeichnis
            shutil.move(source_path, destination_path)
            print(f"Verschiebe {source_path} nach {destination_path}")

if __name__ == "__main__":
    source_folder = "/Volumes/SSK Storage/Pictures/Bilder_Iphone7_bis_21_10_2021"
    destination_folder = "/Volumes/SSK Storage/Pictures/Bilder_Iphone7_bis_21_10_2021"

    move_files_from_subfolders(source_folder, destination_folder)
