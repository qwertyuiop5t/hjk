import os
import requests
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from tqdm import tqdm
import mimetypes

def upload_with_progress_bar(url, files, data=None):
    multipart_data = MultipartEncoder(fields=files)
    progress_bar = tqdm(total=multipart_data.len, unit='B', unit_scale=True)
    monitor = MultipartEncoderMonitor(multipart_data, lambda monitor: progress_bar.update(monitor.bytes_read - progress_bar.n))
    headers = {'Content-Type': multipart_data.content_type}
    with requests.Session() as session:
        with session.post(url, headers=headers, data=monitor, stream=True, timeout=1200) as response:
            response.raise_for_status()
            progress_bar.close()

def send_photo(photo_path, chat_id, bot_token):
    try:
        with open(photo_path, 'rb') as f:
            files = {'photo': (photo_path, f)}
            upload_with_progress_bar(
                f'https://api.telegram.org/bot{bot_token}/sendPhoto?chat_id={chat_id}',
                files=files
            )
            print("Sent successfully")
            print("")
    except requests.exceptions.HTTPError as e:
        print('Error sending photo:', e.response.content.decode())
        print("")
    except requests.exceptions.RequestException as e:
        print('Error sending photo:', e)
        print("")

def send_document(doc_path, chat_id, bot_token):
    try:
        with open(doc_path, 'rb') as f:
            files = {'document': (doc_path, f)}
            upload_with_progress_bar(
                f'https://api.telegram.org/bot{bot_token}/sendDocument?chat_id={chat_id}',
                files=files
            )
            print("Sent successfully")
            print("")
    except requests.exceptions.HTTPError as e:
        print('Error sending photo:', e.response.content.decode())
        print("")
    except requests.exceptions.RequestException as e:
        print('Error sending photo:', e)
        print("")

def send_video(video_path, chat_id, bot_token):
    try:
        with open(video_path, 'rb') as f:
            files = {'video': (video_path, f)}  # update 'document' to 'video'
            upload_with_progress_bar(
                f'https://api.telegram.org/bot{bot_token}/sendVideo?chat_id={chat_id}',
                files=files
            )
            print("Sent successfully")
            print("")
    except requests.exceptions.HTTPError as e:
        print('Error sending video:', e.response.content.decode())
        print("")
    except requests.exceptions.RequestException as e:
        print('Error sending video:', e)
        print("")

def send_audio(audio_path, chat_id, bot_token):
    try:
        with open(audio_path, 'rb') as f:
            files = {'audio': (audio_path, f)}  # update 'document' to 'audio'
            upload_with_progress_bar(
                f'https://api.telegram.org/bot{bot_token}/sendAudio?chat_id={chat_id}',
                files=files
            )
            print("Sent successfully")
            print("")
    except requests.exceptions.HTTPError as e:
        print('Error sending audio:', e.response.content.decode())
        print("")
    except requests.exceptions.RequestException as e:
        print('Error sending audio:', e)
        print("")


while True:
    user_input = str(input("[+] Please enter file: "))
    if os.path.exists(user_input):
        mime_type, encoding = mimetypes.guess_type(user_input)

        if mime_type.startswith("image/"):
            send_photo(user_input, '5054815588', '6126038539:AAEcV_8vtj628h8KsbU2hidg7Y6hOEnbBks')

        elif mime_type.startswith("application/"):
            send_document(user_input, '5054815588', '6126038539:AAEcV_8vtj628h8KsbU2hidg7Y6hOEnbBks')

        elif mime_type.startswith("video/"):
            send_video(user_input, '5054815588', '6126038539:AAEcV_8vtj628h8KsbU2hidg7Y6hOEnbBks')

        elif mime_type.startswith("video/"):
            send_audio(user_input, '5054815588', '6126038539:AAEcV_8vtj628h8KsbU2hidg7Y6hOEnbBks')

        else:
            print("Not Supported")

    else:
        print(f"{user_input} does not exist.")
        print("")
