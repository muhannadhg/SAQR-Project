# Project صقر

السلام عليكم هذا هو مشروع صقر
        
عباره عن مشروع مشابه لاليكسا او نست قوقل
        

قم بفتح محرر النصوص (مثل Visual Studio Code) أو محرر Python المفضل لديك.

تثبيت المكتبات:

قبل تشغيل البرنامج، قم بتثبيت المكتبات التالية باستخدام الأمر pip install في واجهة الأوامر (Command Prompt) أو الطرفية (Terminal):


speech_recognition: تستخدم لتحويل الكلام المسموع من الميكروفون إلى نص.

gtts (Google Text-to-Speech): تستخدم لتحويل النص إلى كلام باستخدام خدمة قوقل للتحويل النصي إلى كلام.

os: تستخدم لتشغيل ملفات الصوت.

pywhatkit: تستخدم للبحث في اليوتيوب وتشغيل أول مقطع يتم العثور عليه.

wikipediaapi: تستخدم للبحث في موقع ويكيبيديا.

BeautifulSoup: تستخدم لتحليل وتنقية نص HTML المسترجع من ويكيبيديا.

requests: تستخدم لجلب بيانات من موقع جوجل باستخدام Google Custom Search API.

py-translate هذا مكتبة يترجم الكلام ، واستخدمتها عشان يترجم اسم الفلم
تحذير   ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️                      

لاجهزة الماك بوك
استخدم ملف main.py
يجب تحميل brew

طريقة التحميل ادخل التيرمنال الذي بداخل محرر الاكواد الذي تستعمله في بايثون

التحميل من موقع : https://brew.sh/

وعند اكتمال التحميل يجب تحميل  :

        brew install portaudio
        brew install mpg321


        
تحذير   ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️          

لاجهزة الويندوز

استخدم ملف main_win.py

يجب تحميل 
https://visualstudio.microsoft.com/visual-cpp-build-tools/

طريقة التحميل 
https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst


وعند اكتمال التحميل يجب تحميل من موجه الاوامر (cmd) الذي بجهازك ويجب عند تشغيله تشغله (كامسؤل)  :

         choco install ffmpeg-full


وبعد ذالك حمل simpleaudio الطريقة ادخل التيرمنال الذي بداخل محرر الاكواد الذي تستعمله في بايثون :

         pip install simpleaudio



ويجب على جميع الاجهزه تحمل هذه المكتبات ⚠️ ⚠️ ⚠️ ⚠️

ولتحميل المكتبات اكتب الامر التالي في التيرمنل الخاص بمحرر الاكواد الذي تستعمله في بايثون:


        pip install speechrecognition gtts pywhatkit wikipedia-api beautifulsoup4 requests pyaudio py-translate tkmacosx pyshorteners




شرح وظائف البرنامج:

استيراد المكتبات: في بداية البرنامج، يتم استيراد جميع المكتبات اللازمة.

دالة say(text): تحوّل النص إلى كلام وتنطقه باستخدام المكتبة gTTS.

دالة print_user_input(text): تقوم بطباعة كلام المستخدم على واجهة التطبيق.

دالة print_saqr_output(text, not_r=0): تقوم بطباعة نص واجهة المستخدم على واجهة التطبيق وقد تنطقه إذا كان not_r = 2.

دالة process_key_words(key_words): تحليل كلمات المستخدم وتنفيذ الأوامر المعترف بها.

دالة lisn_for_key_wordss(): تستمع إلى المستخدم وتكتشف إذا تم قول "صقر"، ثم تحليل الأوامر الصادرة من المستخدم.

دالة start_listening(): تبدأ تنفيذ دالة lisn_for_key_wordss() في خلفية البرنامج.


شرح واجهة التطبيق:

يوجد إطار نصي أعلى النافذة، يُظهر الأوامر التي يقوم المستخدم بإصدارها.

يوجد إطار نصي أدنى النافذة، يُظهر إخراج البرنامج (ردود صقر).


طريقة عمل البرنامج:

يبدأ البرنامج بالاستماع إلى الكلمة الرئيسية "صقر".

بعد اكتشاف الكلمة الرئيسية، يقوم البرنامج بتحويل الكلام إلى نص باستخدام مكتبة SpeechRecognition.

ثم يتم معالجة النص واستخراج الكلمات الرئيسية لتنفيذ الأوامر المطلوبة.

إذا تم اكتشاف كلمة "صقر" في الجملة، يقوم البرنامج بتنفيذ الأوامر المرتبطة بالكلمة الرئيسية ويقوم بإجراء الإجابات المناسبة.

يتم تحديث واجهة Tkinter بعرض نص الإدخال والإخراج والعلامات التعبيرية حسب حالة الاستماع والاستجابة.



بدء تنفيذ البرنامج:

قم بتشغيل البرنامج عبر سطر الأوامر باستخدام الأمر:


        python اسم-ملف-البرنامج.py

بعد تشغيل البرنامج، يمكنك التحدث إليه بقول "صقر" أولًا، ثم قم بإصدار الأوامر المعترف بها. سيقوم البرنامج بتنفيذ الأوامر ويظهر الإجابات على واجهة التطبيق.



ملاحظة: قد تحتاج إلى ضبط إعدادات الصوت على جهاز الكمبيوتر للسماح بالوصول إلى الميكروفون وتشغيل الصوت للحصول على أفضل أداء للبرنامج.


نتمنى لكم تجربه رائعه مع صقر ❤️	


مطورين المشروع مهند الحقباني عبدالله الفهد دينا العمر ريمان نجدي
