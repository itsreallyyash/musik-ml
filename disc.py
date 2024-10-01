import yt_dlp as youtube_dl
import pandas as pd
import os

# Function to download video as MP3
def download_video_as_mp3(youtube_url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path + '/%(title)s.%(ext)s',
        'cookiefile': 'cookies.txt',  # Use the cookies file to bypass bot detection
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

# Function to search YouTube for a song
def search_and_download_song(artist, title, output_folder):
    search_query = f"{artist} {title} official audio"
    
    # Use yt-dlp to search and get the first result
    with youtube_dl.YoutubeDL({'quiet': True, 'cookiefile': 'cookies.txt'}) as ydl:
        try:
            result = ydl.extract_info(f"ytsearch1:{search_query}", download=False)['entries'][0]
            youtube_url = result['webpage_url']
            print(f"Downloading: {artist} - {title} from {youtube_url}")
            
            # Download the song as mp3
            download_video_as_mp3(youtube_url, output_folder)
        except Exception as e:
            print(f"Failed to download {artist} - {title}: {str(e)}")

# Function to download all songs from the CSV
def download_songs_from_csv(csv_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Load the CSV file
    df = pd.read_csv(csv_path)
    
    # Iterate through each row in the CSV
    for index, row in df.iterrows():
        artist = row['Artist_x']
        title = row['Title']
        search_and_download_song(artist, title, output_folder)

# Example usage
csv_file_path = 'ultimate.csv'  # Path to your CSV file
output_directory = 'audio files'  # Directory to save the downloaded songs
download_songs_from_csv(csv_file_path, output_directory)
