import os
import argparse
from pydub import AudioSegment

surahs = [
    "Al-Fatiha (The opener)",
    "Al-Baqarah (The cow)",
    "Al-Imran (Family of Imran)",
    "An-Nisa (The Women)",
    "Al-Ma'idah (The Table Spread)",
    "Al-Anam (The Cattle)",
    "Al-A'raf (The Heights)",
    "Al-Anfal (The Spoils of War)",
    "At-Taubah (The Repentance)",
    "Yunus (Jonah)",
    "Hud (Hud)",
    "Yusuf (Joseph)",
    "Ar-Ra'd (Thunder)",
    "Ibrahim (Abraham)",
    "Al-Hijr (The Stoneland)",
    "An-Nahl (The Bee)",
    "Al-Isra (The Night Journey)",
    "Al-Kahf (The Cave)",
    "Maryam (Mary)",
    "Ta-Ha (Ta-Ha)",
    "Al-Anbiya (The Prophets)",
    "Al-Hajj (The Pilgrimage)",
    "Al-Mu'minun (The Believers)",
    "An-Nur (The Light)",
    "Al-Furqan (The Criterion)",
    "Ash-Shu'ara (The Poets)",
    "An-Naml (The Ants)",
    "Al-Qasas (The Story)",
    "Al-Ankabut (Spider)",
    "Ar-Rum (The Romans)",
    "Luqman (Luqman)",
    "As-Sajdah (Prostration)",
    "Al-Ahzab (The Confederates)",
    "Saba (Sheba)",
    "Fatir (The Originator)",
    "Ya-Sin (Ya Sin)",
    "As-Saffat (Those Who Set the Ranks)",
    "Sad (The letter Saad)",
    "Az-Zumar (The Troops)",
    "Ghafir (The Forgiver)",
    "Fussilat (Explained in Detail)",
    "Ash-Shura (The Consultation)",
    "Az-Zukhruf (The Ornaments of Gold)",
    "Ad-Dukhan (The Smoke)",
    "Al-Jathiyah (The Crouching)",
    "Al-Ahqaf (The Wind Curved Sandhill)",
    "Muhammad (Muhammad)",
    "Al-Fath (The Victory)",
    "Al-Hujurat (The Private Chambers)",
    "Qaf (Qaf)",
    "Adh-Dhariyat (The Scatterers)",
    "At-Tur (The Mountain)",
    "An-Najm (The Star)",
    "Al-Qamar (The Moon)",
    "Ar-Rahman (The Beneficent)",
    "Al-Waqi'ah (The Inevitable)",
    "Al-Hadid (The Iron)",
    "Al-Mujadila (The Pleading Women)",
    "Al-Hashr (The Exile)",
    "Al-Mumtahanah (She That is to be Examined)",
    "As-Saff (The Ranks)",
    "Al-Jumu'ah (Congregation Prayer)",
    "Al-Munafiqun (The Hypocrites)",
    "At-Taghabun (Mutual Disposession)",
    "At-Talaq (The Divorce)",
    "At-Tahrim (The Prohibition)",
    "Al-Mulk (The Sovereignty)",
    "Al-Qalam (The Pen)",
    "Al-Haqqah (The Reality)",
    "Al-Ma'arij (The Ascending Stairways)",
    "Nuh (Noah)",
    "Al-Jinn (The Jinn)",
    "Al-Muzzammil (The Enshrouded One)",
    "Al-Muddaththir (The Cloaked One)",
    "Al-Qiyamah (The Resurrection)",
    "Al-Insan (The Man)",
    "Al-Mursalat (The Emissaries)",
    "An-Naba (The Tidings)",
    "An-Nazi'at (Those who drag forth)",
    "Abasa (He Frowned)",
    "At-Takwir (The Overthrowing)",
    "Al-Infitar (The Cleaving)",
    "Al-Mutaffifin (The Defrauding)",
    "Al-Inshiqaq (The Sundering)",
    "Al-Buruj (The Mansions of the Stars)",
    "At-Tariq (The Nightcommer)",
    "Al-Ala (The Most High)",
    "Al-Ghashiyah (The Overwhelming)",
    "Al-Fajr (The Dawn)",
    "Al-Balad (The City)",
    "Ash-Shams (The Sun)",
    "Al-Lail (The Night)",
    "Ad-Duha (The Morning Brightness)",
    "Ash-Sharh (The Expansion)",
    "At-Tin (The Fig)",
    "Al-Alaq (The Blood Clot)",
    "Al-Qadr (The Power)",
    "Al-Bayyina (The Evidence)",
    "Az-Zalzalah (The Earthquake)",
    "Al-Adiyat (The Courser)",
    "Al-Qari'ah (The Calamity)",
    "At-Takathur (Vying for increase)",
    "Al-Asr (The Declining Day)",
    "Al-Humazah (The Slanderer)",
    "Al-Fil (The Elephant)",
    "Quraysh (Quraish)",
    "Al-Ma'un (The Small Kindness)",
    "Al-Kawthar (The Abundance)",
    "Al-Kafirun (The Disbelievers)",
    "An-Nasr (The Divine Support)",
    "Al-Masad (The Palm Fiber)",
    "Al-Ikhlas (The Sincerity)",
    "Al-Falaq (The Daybreak)",
    "An-Nas (The Mankind)"
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

    for file in sorted(os.listdir(source_path)):
        if file.endswith("mp3"):
            try:
                mp3file = AudioSegment.from_file(os.path.join(source_path, file))
                mp3file = mp3file.set_channels(1)
                mp3file.export(os.path.join(output_path, file), format="mp3")
                print(f"{file} converted")
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
