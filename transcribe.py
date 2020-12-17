# dependencies
import moviepy.editor as me
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



video = me.VideoFileClip("story.mp4")
audio = video.audio
audio.write_audiofile("ad3.wav")

apikey = '#########'
url = '####-6ce09306b525'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

with open('ad3.wav', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/wav', model='en-AU_NarrowbandModel', continuous=True).get_result()
len(res['results'])
text = [
          result['alternatives'][0]['transcript'].rstrip() + '.\n' for result in res['results']
       ]
text = [
          para[0].title() + para[1:] for para in text
       ]
transcript = ''.join(text)



with open('output.txt', 'w') as out:
    out.writelines(transcript)

