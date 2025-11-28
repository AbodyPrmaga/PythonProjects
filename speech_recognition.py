try:
    import speech_recognition as sr
    from pydub import AudioSegment
    import os

    r = sr.Recognizer()

    mp3_file = r"/home/devs/Documents/WEB/Base/python/pp.mp3"
    base = os.path.splitext(os.path.basename(mp3_file))[0]
    wav_file = f"/home/devs/Documents/WEB/Base/python/temp_{base}.wav"

    AudioSegment.from_file(mp3_file).export(wav_file,format="wav")

    print("Done Convert Succssfully!")

    with sr.AudioFile(wav_file) as source:

        audio = r.record(source)

    print("Done Read File Succssfully!")


    text = r.recognize_google(audio,language="ar")

    print("Done GET A TEXT Succssfully!")


    print(text)

    os.remove(wav_file)

except Exception as ex:

    print(f"Error : {ex} !!")
