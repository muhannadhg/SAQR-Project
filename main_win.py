import speech_recognition as sr # هذا يحول الكلام الى نص
from gtts import gTTS # يستخدم تقنية قوقل الي تحول النص الى كلام مجانيه طبعا
import os # هذي اشياء في النظام مثلا يشغل صوت يحفظ ملفات الى اخره
import pywhatkit as kit # هذي حقت اليوتيوب مدري صراحه ايش تسوي بس الى اعرفه انها تبحث في اليوتيوب وتطلع اول مقطع
import wikipediaapi # هذي حقت ويكبيديا اذا سالت  مثلا من هو محمد بن سلمان رح يبحث في ويكبيديا وبعد كذا بيطبع لك الناتج وبينطقه الحبيب الي فوق
from bs4 import BeautifulSoup # هذي سالفتها طويله بالمختصر شفتو ويكبيديا اذا جاء يطبع الكلام يطبعها ويضيف عليها اشياء حقت ال HTML والحبيب حق قوقل ينطقها شرطةً وسلاشً زي كذا هذا يحذفها هذي فايدته
import requests # هذا ياطويل العمر حق ال Api سالفته يربط بين الموقعي حقي وقوقل جلب بينات فقط نقول مستقبلاً ان شاء الله نقدر نعدل مو بس نجلب
import tkinter as tk # هذا حطيته والله بس عشان سياسة المكان (نقاط)
import threading # هذا شفتو اذا جاء ينطق البرنامج كان يعلق الحين ذا خلها ينطق في الخلفية مايحتاج البرنامج يعلق كل مره ينطق فيها
import subprocess # وذا سالفته طويل بس بختصار عشان جهازي ماك هو الي يشغل الفيديو
from pydub import AudioSegment
import simpleaudio as sa
from translate import Translator #هذا مكتبة يترجم الكلام ، واستخدمتها عشان يترجم اسم الفلم

# دالة لتحويل ملف mp3 إلى wave
def mp3_to_wave(mp3_file, wave_file):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wave_file, format="wav")

# دالة لتشغيل الملف الصوتي
def play_audio(wave_file):
    wave_obj = sa.WaveObject.from_wave_file(wave_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()

# دالة للنطق
def say(text):
    tts = gTTS(text=text, lang='ar')
    tts.save('output.mp3')
    mp3_to_wave('output.mp3', 'output.wav')
    play_audio('output.wav')
    # قم بحذف الملف المؤقت
    os.remove('output.mp3')
    os.remove('output.wav')

#وذا ياخذ كلام المستخدم وحطه في والجهة وينطقه
def print_user_input(text):
    output_text.tag_configure("user_tag", justify='right', foreground='#EAEAEA')
    output_text.insert("end", f"{text}\n", "user_tag")
    output_text.see("end")

#وذا ياطويلين العمر نفس فكرت الي فوق بس انه للصقر مو للمستخدم
def print_saqr_output(text,not_r=0):
    if not_r == 1:
        output_text.tag_configure("program_tag", justify='left', foreground='#B2B2B2')
        output_text.insert("end", f"{text}\n", "program_tag")
        output_text.see("end")
    elif not_r == 2:
        say(text)
    else:
        output_text.tag_configure("program_tag", justify='left', foreground='#B2B2B2')
        output_text.insert("end", f"{text}\n", "program_tag")
        output_text.see("end")
        say(text)

# وذي الكلامات المفتاحية او مدي وش تسمى ازبده هذا يعرف وش انت تبي من صقر
def process_key_words(key_words):
    if "شغل" in key_words:
            search_query = key_words.replace("شغل", "")
            print_saqr_output(f"جاري البحث عن{search_query} على اليوتيوب.")
            kit.playonyt(search_query)
    elif "تحبني" in key_words:
        print_saqr_output("لا")
    elif "انت افضل" in key_words:
        print_saqr_output("ياحبيبي ياقلبي انتا لو تبغا عيوني اخفع امها ذحين كذا واعطيك", 1)
        os.system('mpg321 bander_r.mp3')
    elif "عادي اجربك" in key_words or "عادي جربك" in key_words:
        print_saqr_output("لا طبعا مهند وبس .......")
    elif "انتهينا" in key_words:
        print_saqr_output("ونتهينا  👋 🙁", 1)
        os.system('mpg321 srtkaif.mp3')
    elif "من هو الافضل" in key_words and len(key_words) < 18:
        print_saqr_output("ميسي وبعد ذالك أُستاذة عبير و أمجاد")
    elif "لماذا تم اضافه لك واجهه رسوميه" in key_words:
        video_path = "sys.mp4"  # اضف مسار الفيديو هنا
        print_saqr_output("سياسة المكان بين قوسين نقاط")
        try:
            subprocess.Popen(["open", video_path])  # فتح الفيديو باستخدام التطبيق المشغل الافتراضي
        except FileNotFoundError:
            print_saqr_output("لم يتم العثور على مشغل فيديو مناسب.")
    elif "من انت" in key_words:
        print_saqr_output("انا برنامج تم تطويري من قبل مهند الحقباني وتم ربطي مع ويكبيديا ومع محرك البحث قوقل")

        elif "شوف لي" in key_words:



            search_query = key_words.replace("شوف لي", "")
            print_saqr_output(f"جاري البحث عن{search_query} على اي ام دي بي.")

            translator = Translator(from_lang="ar", to_lang="en")
            translation = translator.translate(search_query)
            print_saqr_output(translation)

            url = "https://online-movie-database.p.rapidapi.com/auto-complete"

            querystring = {"q": translation}

            api_key = {
                "X-RapidAPI-Key": "20cddadde1msh9f461035256fe15p16e203jsn78eb1dac15bf",
                "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
            }

            response = requests.get(url, headers=api_key, params=querystring)
            data=response.json()
            print(response.json())
            rank=data["d"][0]["rank"]
            s=data["d"][0]["s"]
            y=data["d"][0]["y"]
            print_saqr_output(f"ترتيب الفلم هو {rank}")
            print_saqr_output(f"ابطال الفلم هم {s}",1)
            print_saqr_output(f"سنة تصنيع الفلم هي {y}")
    elif "ابحث" in key_words:
        person_query = key_words.replace("ابحث", "")

        def search_google(query, api_key, cx):
            base_url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "key": api_key,
                "cx": cx,
                "q": query
            }

    elif "ابحث" in key_words:
        person_query = key_words.replace("ابحث", "")

        def search_google(query, api_key, cx):
            base_url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "key": api_key,
                "cx": cx,
                "q": query
            }

            try:
                response = requests.get(base_url, params=params)
                data = response.json()
                return data
            except requests.RequestException as e:
                print("حدث خطأ أثناء الاتصال بمحرك البحث.")
                print(e)
                return None

        api_key = "AIzaSyBRPEUwx5q0dgHdIqjp60HOSZwaE3sr8zQ"
        cx = "a542a07dfc65a476b"

        query = person_query
        search_result = search_google(query, api_key, cx)

        if search_result:
            items = search_result.get("items", [])
            for i, item in enumerate(items, start=1):
                title = item.get("title", "عنوان غير متوفر")
                link = item.get("link", "رابط غير متوفر")
                snippet = item.get("snippet", "معلومات غير متوفرة")
                print_saqr_output(f"نتيجة {i}:",1)
                print_saqr_output(f"العنوان: {title}",1)
                print_saqr_output(f"الرابط: {link}",1)
                print_saqr_output(f"مقتطف: {snippet}",1)
                if i == 1:
                    print_saqr_output(f"{title}", 2)
                    print_saqr_output(f"{snippet}", 2)
                print_saqr_output("--------------------------")

        else:
            print_saqr_output(f" لم يتم العثور على نتائج {person_query}.")

    elif "من هو" in key_words:
        person_query = key_words.replace("من هو", "")
        wiki_wiki = wikipediaapi.Wikipedia(
            language='ar', extract_format=wikipediaapi.ExtractFormat.HTML, user_agent="MyApp/1.0"
        )
        page = wiki_wiki.page(person_query)
        if page.exists():
            summary = BeautifulSoup(page.summary[:200], "html.parser").text
            print_saqr_output(f"{person_query} هو: {summary}")
        else:
            print_saqr_output(f" لاتوجد معلومات {person_query}.")
    else:
        print_saqr_output("اطلب غير معرف")
        pass

#وذا عشان يعرف انت تبي صقر ولا تبي انساك هههههه امزح هذا بس يتاكد انك قلت صقر في البداية
def lisn_for_key_wordss():
    recognizer = sr.Recognizer()
    wake_word_detected = False

    while True:
        with sr.Microphone() as source:
            print("قل شيئا...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

            print("جاري التعرف على الصوت...")
            key_words = recognizer.recognize_google(audio, language="ar")
            print_user_input(key_words)

            if "صقر" in key_words and len(key_words) < 9:
                wake_word_detected = True
                print_saqr_output("اهلا بك!")
            else:
                if wake_word_detected or "صقر" in key_words:
                    index = key_words.index("صقر")
                    key_words = key_words[index:]
                    if "صقر" in key_words and "ص" == key_words[0]:
                        replace_saqr = key_words.replace("صقر", "", 1)
                        process_key_words(replace_saqr)
                    else:
                        print_saqr_output("يجب قول صقر قبل اعطاء اي اوامر",1)
                else:
                    print_saqr_output("يجب قول صقر قبل اعطاء اي اوامر",1)


def start_listening():
    lisn_for_key_wordss_thread = threading.Thread(target=lisn_for_key_wordss)
    lisn_for_key_wordss_thread.daemon = True
    lisn_for_key_wordss_thread.start()


# هذا حق  Tkinter
root = tk.Tk()
root.title("صقر Project")
root.geometry("800x600")

# هذا يحط لك emoji تحت
emoji_label = tk.Label(root, text="جاري التحميل ..... (للبدء قل صقر)", font=("Arial", 30))
emoji_label.pack(side="bottom", pady=20)

#وذا كرفت فيه عشان بس يتغير الايموجي في الحالتين
def lisn_for_key_wordss():
    recognizer = sr.Recognizer()
    wake_word_detected = False

    while True:
        with sr.Microphone() as source:
            print("قل شيئا...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        try:
            print("جاري التعرف على الصوت...")
            emoji_label.config(text="⏳")  # عرض الإيموجي للتعرف على الصوت
            key_words = recognizer.recognize_google(audio, language="ar")
            if "صقر" in key_words:
                index = key_words.index("صقر")
                key_words = key_words[index:]
                print_user_input(key_words)

            if "صقر" in key_words and len(key_words) < 9:
                wake_word_detected = True
                print_saqr_output("اهلا بك!")
            else:
                if wake_word_detected or "صقر" in key_words:
                    if "صقر" in key_words and "ص" == key_words[0]:
                        replace_saqr = key_words.replace("صقر", "", 1)
                        process_key_words(replace_saqr)
                    else:
                        print_saqr_output("يجب قول صقر قبل اعطاء اي اوامر",1)
                else:
                    print_saqr_output("يجب قول صقر قبل اعطاء اي اوامر",1)
                    pass

        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            pass
        finally:
            emoji_label.config(text="🎙")


# هذا يعرض كلامك بينك وبين صويقر❤️
output_text = tk.Text(root, font=("Arial", 30), wrap="word")
output_text.pack(fill="both", expand=True)

# هذا بس يبدا عشان يتسمع ترى اقدر اخلي فيه تسجيل واسمع وش تقولون فا انتبه من هذي التقنيات مثل اليكسا و نست قوقل
start_listening()

# هذا عشان يبدا البرنامج وعشان بعد يتحدث كل شوي
root.mainloop()


#وبس والله البرنامج حطيت في حيلي واو تعبت قعدت عليه ساعة ونص ، وشوي عشان التطويرات

#اتمني اعجبكم تقيمكم للبرنامج والي مايعجبه بالله صقر قوم اجلده

#والي يشكك انه اسوء برنامج استماع حاب اقولك حتى انا مشكك
