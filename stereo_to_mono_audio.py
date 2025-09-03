import os
import argparse
from pydub import AudioSegment

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

def convert_mp3_to_wav(source_path, output_path):

    if not os.path.isdir(source_path):
        print(f"Directory {source_path} does not exist.")
        return

    if not os.path.isdir(output_path):
        try:
            os.mkdir(output_path)
            print(f"Directory '{output_path}' created successfully.")
        except FileExistsError:
            print(f"Directory '{output_path}' already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return

    index = 0
    for file in sorted(os.listdir(source_path)):
        if file.endswith("mp3"):
            try:

                if index < len(surahs):
                    new_filename = f"{index+1:03d} {surahs[index]} - Hussary.mp3"
                index = index + 1
                mp3file = AudioSegment.from_file(os.path.join(source_path, file))
                mp3file = mp3file.set_channels(1)
                mp3file.export(os.path.join(output_path, new_filename), format="mp3")
                print(f"{new_filename} converted")
            except Exception as e:
                print(f"Error converting {file}: {e}")


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
    
    parser.add_argument(
        "-s", "--source",
        required=True,
        help="Source directory containing MP3 files"
    )
    
    parser.add_argument(
        "-o", "--output", 
        required=True,
        help="Output directory for converted WAV files"
    )
    
    args = parser.parse_args()
    
    # Pfade aus den Argumenten verwenden
    convert_mp3_to_wav(args.source, args.output)

if __name__ == "__main__":
    #source_path = "/Users/amarbanovic/Music/MahmoudKhalilAl-husary"
    #output_path = "/Users/amarbanovic/Music/MahmoudKhalilAl-husary/mp3files"

    #convert_mp3_to_wav(source_path, output_path)

    main()
