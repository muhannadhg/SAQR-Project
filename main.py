import speech_recognition as sr  # هذا يحول الكلام الى نص
from gtts import gTTS  # يستخدم تقنية قوقل الي تحول النص الى كلام مجانيه طبعا
import os  # هذي اشياء في النظام مثلا يشغل صوت يحفظ ملفات الى اخره
import pywhatkit as kit  # هذي حقت اليوتيوب مدري صراحه ايش تسوي بس الى اعرفه انها تبحث في اليوتيوب وتطلع اول مقطع
import \
    wikipediaapi  # هذي حقت ويكبيديا اذا سالت  مثلا من هو محمد بن سلمان رح يبحث في ويكبيديا وبعد كذا بيطبع لك الناتج وبينطقه الحبيب الي فوق
from bs4 import \
    BeautifulSoup  # هذي سالفتها طويله بالمختصر شفتو ويكبيديا اذا جاء يطبع الكلام يطبعها ويضيف عليها اشياء حقت ال HTML والحبيب حق قوقل ينطقها شرطةً وسلاشً زي كذا هذا يحذفها هذي فايدته
import \
    requests  # هذا ياطويل العمر حق ال Api سالفته يربط بين الموقعي حقي وقوقل جلب بينات فقط نقول مستقبلاً ان شاء الله نقدر نعدل مو بس نجلب
import tkinter as tk  # هذا حطيته والله بس عشان سياسة المكان (نقاط)
import \
    threading  # هذا شفتو اذا جاء ينطق البرنامج كان يعلق الحين ذا خلها ينطق في الخلفية مايحتاج البرنامج يعلق كل مره ينطق فيها
import subprocess  # وذا سالفته طويل بس بختصار عشان جهازي ماك هو الي يشغل الفيديو
from translate import Translator  # هذا مكتبة يترجم الكلام ، واستخدمتها عشان يترجم اسم الفلم
import webbrowser


# ذا ينطق الكلام
def say(text):
    tts = gTTS(text=text, lang='ar')
    tts.save('output.mp3')
    os.system('mpg321 output.mp3')


# وذا ياخذ كلام المستخدم وحطه في والجهة وينطقه
def print_user_input(text):
    output_text.tag_configure("user_tag", justify='right', foreground='#EAEAEA')
    output_text.insert("end", f"{text}\n", "user_tag")
    output_text.see("end")


# وذا ياطويلين العمر نفس فكرت الي فوق بس انه للصقر مو للمستخدم
def print_saqr_output(text, not_r=0):
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

    elif "وين اقرب" in key_words:
        search_query = key_words.replace("وين اقرب", "")
        print_saqr_output(f"جاري البحث عن{search_query} على قوقل ماب.")

        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        input_addr = search_query
        detile = {
            "input": input_addr,
            "inputtype": "textquery",
            "fields": "formatted_address,name,rating,opening_hours,geometry",
            "language": "ar",
            "key": "AIzaSyBRPEUwx5q0dgHdIqjp60HOSZwaE3sr8zQ"
        }

        payload = {}
        headers = {}

        response = requests.request("GET", url, params=detile, headers=headers, data=payload)
        data = response.json()
        print(data)
        if "candidates" in data and data["candidates"]:
            location = data["candidates"][0]["geometry"]["location"]
            lat = location["lat"]
            lng = location["lng"]

            # Open Google Maps in the default web browser with the specified location
            maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
            webbrowser.open(maps_url)
        else:
            print("Location not found.")

    elif "شوف لي" in key_words:

        search_query = key_words.replace("شوف لي", "")
        print_saqr_output(f"جاري البحث عن{search_query} على IMDB")

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
        data = response.json()
        print(response.json())
        rank = data["d"][0]["rank"]
        s = data["d"][0]["s"]
        y = data["d"][0]["y"]
        poster_url = data["d"][0]["i"]["imageUrl"]

        print_saqr_output(f"ترتيب الفلم هو {rank}")
        print_saqr_output(f"ابطال الفلم هم {s}", 1)
        print_saqr_output(f"سنة تصنيع الفلم هي {y}")
        print_saqr_output("جاري عرض صورة الفلم ........", 1)
        from io import BytesIO
        from PIL import Image

        response = requests.get(poster_url)
        img = Image.open(BytesIO(response.content))
        img.show()

    elif "اسم المنتج" in key_words:

        search_query = key_words.replace("اسم المنتج", "")
        print_saqr_output(f"جاري البحث عن{search_query} على amazon")

        params = {
            'api_key': '42BE4EBED3F64E438E73820838E9F149',
            'type': 'search',
            'amazon_domain': 'amazon.sa',
            'search_term': search_query,
            'sort_by': 'featured',
            'language': 'ar_SA',
            'currency': 'sar',
            'output': 'json'
        }

        api_result = requests.get('https://api.rainforestapi.com/request', params)

        res = api_result.json()

        x = 0
        while x < 3:
            try:
                if (x == 0):
                    data = res["search_results"][x]
                    print(data)
                    title = data["title"]
                    print_saqr_output(f"اسم المنتج : {title}")

                    rating = data["rating"]
                    print_saqr_output(f"تقييم المنتج : {rating}")

                    ratings_total = data["ratings_total"]
                    print_saqr_output(f"عدد المقيمين المنتج : {ratings_total}", 1)

                    prices = data["prices"][0]["name"]
                    print_saqr_output(f"سعر المنتج : {prices}")

                    link = data["link"]
                    print_saqr_output(f"رابط المنتج : {link}", 1)
                else:
                    data = res["search_results"][x]
                    print(data)
                    title = data["title"]
                    print_saqr_output(f"اسم المنتج : {title}", 1)

                    rating = data["rating"]
                    print_saqr_output(f"تقييم المنتج : {rating}", 1)

                    ratings_total = data["ratings_total"]
                    print_saqr_output(f"عدد المقيمين المنتج : {ratings_total}", 1)

                    prices = data["prices"][0]["name"]
                    print_saqr_output(f"سعر المنتج : {prices}", 1)

                    link = data["link"]
                    print_saqr_output(f"رابط المنتج : {link}", 1)

                x += 1
            except KeyError as ke:
                print('اعتذر لا استطيع جلب المزيد من العلومات')
                break

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
                print_saqr_output(f"نتيجة {i}:", 1)
                print_saqr_output(f"العنوان: {title}", 1)
                print_saqr_output(f"الرابط: {link}", 1)
                print_saqr_output(f"مقتطف: {snippet}", 1)
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


# وذا عشان يعرف انت تبي صقر ولا تبي انساك هههههه امزح هذا بس يتاكد انك قلت صقر في البداية
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
                        print_saqr_output("يجب قول صقر قبل اعطاء اي اوامر", 1)
                else:
                    print_saqr_output("يجب قول صقر قبل اعطاء اي اوامر", 1)


def start_listening():
    lisn_for_key_wordss_thread = threading.Thread(target=lisn_for_key_wordss)
    lisn_for_key_wordss_thread.daemon = True
    lisn_for_key_wordss_thread.start()


# هذا حق  Tkinter
root = tk.Tk()
root.title("صقر Project")
root.geometry("800x600")

# هذا يحط لك emoji تحت
emoji_label = tk.Label(root, text="جاري التحميل ..... (للبدء قل صقر)", font=("Arial", 60))
emoji_label.pack(side="bottom", pady=20)

# Entry field to receive the national address
national_address_entry = tk.Entry(root, font=("Arial", 25))
national_address_entry.pack(fill="x", padx=20, pady=10)


def get_national_address():
    api_key = "c1dbaa243a974f619b50f429d1cbd571"
    addressstring = national_address_entry.get()  # Get the user input from the entry field
    if (addressstring == ""):
        print_saqr_output("ادخل في الاعلى العنوان الوطني")
        pass
    else:
        base_url = "https://apina.address.gov.sa/NationalAddress/v3.1/Address/address-free-text"
        addressstring = {
            "addressstring": addressstring
        }
        api_key = {
            "api_key": api_key
        }

        response = requests.get(base_url, params=addressstring, headers=api_key)

        if response.status_code == 200:
            data = response.json()
            totalSearchResults = int(data["totalSearchResults"])
            if totalSearchResults > 0:
                address_details = data["Addresses"][0]
                address_info = f"العنوان الأول: {address_details['Address1']}\n" \
                               f"العنوان الثاني: {address_details['Address2']}\n" \
                               f"الحي: {address_details['District']}\n" \
                               f"المدينة: {address_details['City']}\n" \
                               f"الرمز البريدي: {address_details['PostCode']}"
                print_saqr_output(address_info,1)
            else:
                print_saqr_output("لم يتم العثور على نتائج للعنوان المدخل.")
        else:
            print_saqr_output(f"حدث خطأ في الاتصال. رمز الحالة: {response.status_code}")


def get_national_address2():
    api_key = "c1dbaa243a974f619b50f429d1cbd571"
    addressstring = national_address_entry.get()  # Get the user input from the entry field
    if (addressstring == ""):
        print_saqr_output("ادخل في الاعلى العنوان الوطني")
        pass
    else:
        base_url = "https://apina.address.gov.sa/NationalAddress/v3.1/Address/address-free-text"
        addressstring = {
            "addressstring": addressstring
        }
        api_key = {
            "api_key": api_key
        }

        response = requests.get(base_url, params=addressstring, headers=api_key)

        if response.status_code == 200:
            data = response.json()
            totalSearchResults = int(data["totalSearchResults"])
            if totalSearchResults > 0:
                lat = data["Addresses"][0]["Latitude"]
                lng = data["Addresses"][0]["Longitude"]

                # Open Google Maps in the default web browser with the specified location
                maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
                webbrowser.open(maps_url)
            else:
                print_saqr_output("لم يتم العثور على نتائج للعنوان المدخل.")
        else:
            print_saqr_output(f"حدث خطأ في الاتصال. رمز الحالة: {response.status_code}")


def get_cv_name():
    api_key = "C1vH94RqBOqceB5KLP7WXeJY5UBfXEG4"
    cr_number = national_address_entry.get()  # Get the user input from the entry field
    if (cr_number == ""):
        print_saqr_output("ادخل في الاعلى السجل التجاري")
        pass
    else:
        base_url = "https://api.wathq.sa/v5/commercialregistration/fullinfo/" + cr_number
        api_key = {
            "accept": "application/json",
            "apiKey": api_key
        }

        response = requests.get(base_url, headers=api_key)

        if response.status_code == 200:
            data = response.json()
            crName = data["crName"]
            parties = data["parties"][0]["name"]
            relation = data["parties"][0]["relation"]["name"]
            businessType = data["businessType"]["name"]
            status = data["status"]["name"]
            address = data["address"]["general"]["address"]
            print_saqr_output(f"الاسم : {crName}")
            print_saqr_output(f"المالك : {parties}")
            print_saqr_output(f"المنصب : {relation}")
            print_saqr_output(f"نوع العمل : {businessType}")
            print_saqr_output(f"حالة السجل : {status}")
            print_saqr_output(f"الموقع الرئيسي : {address}", 1)
        else:
            print_saqr_output(f"حدث خطأ في الاتصال. رمز الحالة: {response.status_code}")


# وذا كرفت فيه عشان بس يتغير الايموجي في الحالتين
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
                        if "معلومات العنوان الوطني" in replace_saqr:
                            get_national_address()
                        elif "حدد العنوان الوطني" in replace_saqr:
                            get_national_address2()
                        elif "معلومات التاجر" in replace_saqr:
                            get_cv_name()
                        else:
                            process_key_words(replace_saqr)
                    else:
                        print_saqr_output("يجب قول صقر قبل اعطاء اي اوامر", 1)
                else:
                    print_saqr_output("يجب قول صقر قبل اعطاء اي اوامر", 1)
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

# وبس والله البرنامج حطيت في حيلي واو تعبت قعدت عليه ساعة ونص ، وشوي عشان التطويرات

# اتمني اعجبكم تقيمكم للبرنامج والي مايعجبه بالله صقر قوم اجلده

# والي يشكك انه اسوء برنامج استماع حاب اقولك حتى انا مشكك
