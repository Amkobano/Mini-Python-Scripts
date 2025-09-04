import os  # Provides functions to interact with the operating system (folders, files)
import argparse  # Allows parsing command-line arguments
from pydub import AudioSegment  # Library to handle audio files (conversion, channels, etc.)
from mutagen.easyid3 import EasyID3  # Simplified interface to edit ID3 tags (title, artist, album)
from mutagen.id3 import ID3, APIC  # Advanced ID3 tag handling, including embedding album art

# List of Surah names to rename files and set ID3 tags
surahs = [
    "Al-Fatiha",
    "Al-Baqarah",
    "Al-Imran",
    "An-Nisa",
    "Al-Ma'idah",
    "Al-Anam",
    "Al-A'raf",
    "Al-Anfal",
    "At-Taubah",
    "Yunus",
    "Hud",
    "Yusuf",
    "Ar-Ra'd",
    "Ibrahim",
    "Al-Hijr",
    "An-Nahl",
    "Al-Isra",
    "Al-Kahf",
    "Maryam",
    "Ta-Ha",
    "Al-Anbiya",
    "Al-Hajj",
    "Al-Mu'minun",
    "An-Nur",
    "Al-Furqan",
    "Ash-Shu'ara",
    "An-Naml",
    "Al-Qasas",
    "Al-Ankabut",
    "Ar-Rum",
    "Luqman",
    "As-Sajdah",
    "Al-Ahzab",
    "Saba",
    "Fatir",
    "Ya-Sin",
    "As-Saffat",
    "Sad",
    "Az-Zumar",
    "Ghafir",
    "Fussilat",
    "Ash-Shura",
    "Az-Zukhruf",
    "Ad-Dukhan",
    "Al-Jathiyah",
    "Al-Ahqaf",
    "Muhammad",
    "Al-Fath",
    "Al-Hujurat",
    "Qaf",
    "Adh-Dhariyat",
    "At-Tur",
    "An-Najm",
    "Al-Qamar",
    "Ar-Rahman",
    "Al-Waqi'ah",
    "Al-Hadid",
    "Al-Mujadila",
    "Al-Hashr",
    "Al-Mumtahanah",
    "As-Saff",
    "Al-Jumu'ah",
    "Al-Munafiqun",
    "At-Taghabun",
    "At-Talaq",
    "At-Tahrim",
    "Al-Mulk",
    "Al-Qalam",
    "Al-Haqqah",
    "Al-Ma'arij",
    "Nuh",
    "Al-Jinn",
    "Al-Muzzammil",
    "Al-Muddaththir",
    "Al-Qiyamah",
    "Al-Insan",
    "Al-Mursalat",
    "An-Naba",
    "An-Nazi'at",
    "Abasa",
    "At-Takwir",
    "Al-Infitar",
    "Al-Mutaffifin",
    "Al-Inshiqaq",
    "Al-Buruj",
    "At-Tariq",
    "Al-Ala",
    "Al-Ghashiyah",
    "Al-Fajr",
    "Al-Balad",
    "Ash-Shams",
    "Al-Lail",
    "Ad-Duha",
    "Ash-Sharh",
    "At-Tin",
    "Al-Alaq",
    "Al-Qadr",
    "Al-Bayyina",
    "Az-Zalzalah",
    "Al-Adiyat",
    "Al-Qari'ah",
    "At-Takathur",
    "Al-Asr",
    "Al-Humazah",
    "Al-Fil",
    "Quraysh",
    "Al-Ma'un",
    "Al-Kawthar",
    "Al-Kafirun",
    "An-Nasr",
    "Al-Masad",
    "Al-Ikhlas",
    "Al-Falaq",
    "An-Nas"
]

# Function to convert MP3 files to mono WAV files and add metadata
def convert_mp3_to_wav(source_path, output_path):

    # Check if source directory exists
    if not os.path.isdir(source_path):
        print(f"Directory {source_path} does not exist.")
        return

    # Create output directory if it does not exist
    if not os.path.isdir(output_path):
        try:
            os.mkdir(output_path)
            print(f"Directory '{output_path}' created successfully.")
        except FileExistsError:
            print(f"Directory '{output_path}' already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return

    # Path to the cover image to embed in the MP3 files
    cover_path = "/Users/amarbanovic/Downloads/mahmoud-khalil-al-hussary-2873.jpg"

    index = 0  # Initialize index to match surah list
    for file in sorted(os.listdir(source_path)):  # Loop through all files in the source folder
        if file.endswith("mp3"):  # Only process MP3 files
            try:

                # Generate new filename based on surah index
                if index < len(surahs):
                    new_filename = f"{index+1:03d} {surahs[index]} - Hussary.mp3"
                
                # Load MP3 file
                mp3file = AudioSegment.from_file(os.path.join(source_path, file))
                mp3file = mp3file.set_channels(1)  # Convert to mono
                export_path = os.path.join(output_path, new_filename)
                mp3file.export(export_path, format="mp3")  # Export as MP3

                # Set basic ID3 tags (title, artist, album)
                audio = EasyID3(export_path)
                audio["title"] = f"{index+1:03d} {surahs[index]}"
                audio["artist"] = "Mahmoud Khalil Al-Hussary"
                audio["album"] = "Al Quran - Mahmoud Khalil Al-Hussay"
                audio.save()

                # Embed cover image if it exists
                if os.path.isfile(cover_path):
                    audio_id3 = ID3(export_path)
                    with open(cover_path, "rb") as albumart:
                        audio_id3.add(
                            APIC(
                                encoding=3,       # UTF-8 encoding
                                mime="image/jpeg",  # MIME type of the image
                                type=3,             # 3 = front cover
                                desc="Cover",       # Description of the image
                                data=albumart.read()  # Read image bytes
                            ),
                        )
                    audio_id3.save(v2_version=3)  # Save ID3v2.3 tags

                index = index + 1  # Increment index for next surah

                print(f"{new_filename} converted")  # Inform user
                print(export_path)  # Print full export path

                # Optional: print all tags (commented out)
                # tags = ID3(export_path)
                # print(tags.pprint())
            except Exception as e:
                print(f"Error converting {file}: {e}")  # Handle conversion errors
                
# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(
        description="Convert MP3 files to WAV format with mono channel",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python stereo_to_mono_audio.py -s /path/to/source -o /path/to/output
  python stereo_to_mono_audio.py --source /music/mp3files --output /music/wavfiles
        """
    )
    
    # Argument for source directory
    parser.add_argument(
        "-s", "--source",
        required=True,
        help="Source directory containing MP3 files"
    )
    
    # Argument for output directory
    parser.add_argument(
        "-o", "--output", 
        required=True,
        help="Output directory for converted WAV files"
    )
    
    args = parser.parse_args()  # Parse the arguments
    
    # Call conversion function with provided paths
    convert_mp3_to_wav(args.source, args.output)

# Entry point of the script
if __name__ == "__main__":
    main()
