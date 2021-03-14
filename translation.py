class Translation(object):
    START_TEXT = """😊Salom

🤖Ushbu Botimiz Telegram orqali Hohlagan URL manzillarni ko'chirib olish boti hisoblanadi.

📹YouTube dan ham Vedio Yuklab berishimiz mumkin
Buning uchun /help buyrug'ini yuborib To'liq ma'lumot bilib oling.

💻Dasturchi: @abdulloev_shavkat
📡Kanallarimiz @PHP_Secrets , @app_Telegraph_Uzbek , @EHMUZ"""
    RENAME_403_ERR = "Kechirasiz. Sizga ushbu faylning nomini o'zgartirish huquqi berilmagan."
    ABS_TEXT = " Iltimos, xudbin bo'lmang."
    UPGRADE_TEXT = "<b>👉 /help buyrug'ini yuboring </b>"
    FORMAT_SELECTION = "☝️Kerakli formatni tanlang: <a href='{}'>fayl hajmi taxminiy bo'lishi mumkin</a> \n👇Quyidagi Tugmalardan birini bosish orqali Siz Tashlagan URL manzilingizni 📁File/Vedio📹 Farmqatlarda ⚙️o'zingizga moslab olishingiz mumkin.\n\n👍Biz Bilan Birga Qoling @v_a_q_t"
    SET_CUSTOM_USERNAME_PASSWORD = """Agar siz premium videolarni yuklab olishni xohlasangiz, quyidagi formatda taqdim eting:
URL | filename | username | password"""
    NOYES_URL = "@uploadsavebot URL topildi. Iltimos, https://t.me/abdulloev_shavkat dan foydalaning va menga tezkor URL manzilini oling, shunda men Telegram-ga yuklay olaman, boshqa foydalanuvchilar uchun sekinlashmasdan."
    DOWNLOAD_START = "📥Yuklab Olinmoqda..."
    UPLOAD_START = "📤Yuklanmoqda..."
    RCHD_BOT_API_LIMIT = "Hajmi ruxsat etilgan kattalikdan (50MB) kattaroq. Shunga qaramay, yuklashga harakat qilmoqda."
    RCHD_TG_API_LIMIT = "📥Yuklab olingan {} sekund.\n🎚Aniqlangan fayl hajmi: {}\nKechirasiz. Ammo, men Telegram API cheklovlari tufayli 1.5GB dan katta fayllarni yuklay olmayman."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Iltimos, meni foydali deb bilsangiz, baholash maqsadida Kanalimizga Qo'shiling: @PHP_Secrets"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "{} Soniya ichida yuklab olindi.📥\n{} Soniya ichida yuklandi.📤\n📡Kanalimiz : @PHP_Secrets"
    NOT_AUTH_USER_TEXT = "Iltimos /upgrade obunangizni."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Aniqlangan fayl hajmi: {}. Bepul foydalanuvchilar faqat yuklashlari mumkin: {}\nIltimos /upgrade obunangizni.\nAgar bu xato deb o'ylasangiz, iltimos murojaat qiling <a href='https://telegram.me/SHAVKAT'>@abdulloev_shavkat</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Shaxsiy video/fayl eskizi saqlandi. Ushbu rasm video/faylda ishlatiladi."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Xos eskiz muvaffaqiyatli o'chirildi."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media muvaffaqiyatli o'chirildi."
    SAVED_RECVD_DOC_FILE = "Hujjat muvaffaqiyatli yuklandi."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Haqiqiy ThumbNail topilmadi."
    NO_VOID_FORMAT_FOUND = "ERROR ... \ n <b> YouTubeDL </b> dedi: {}"
    USER_ADDED_TO_DB = "<a href='tg://user?id={}'> {} </a> foydalanuvchisi {} ga {} qadar qo'shildi."
    CURENT_PLAN_DETAILS = """Siz Haqingizda
--------
Telegram ID: <code>{}</code>
Plan nomi: Bepul
Muddati tugaydi: 31/12/2020"""
    HELP_USER = """Salom, Men URL ni yuklash botiman ..
    
1. URL manzilini yuboring (Link|Kengaytmali yangi nom).
2. Boshqa eskizni yuborish (ixtiyoriy).
3. Tugmani tanlang.
   SVideo - Skrinshotlar va video sifatida yuboradi.
   DFile - Skrinshot va fayl sifatida yuboradi. 
   Video - Skrinshotlarsiz videoni o'zini yuboradi.
   File - Skrinshotsiz fayni o'zini yuboradi.
   
<b>👉 Qo'llanma(Yo'riqnoma) :</b> 👉 <a href="https://telegra.ph/uploadsavebot-da-ishlash-Version-21-04-07">Bosing</a>

--------

💻Dasturchi: @RedFoc
📡Kanallarimiz @PHP_Secrets , @app_Telegraph_Uzbek , @EHMUZ"""
    REPLY_TO_DOC_GET_LINK = "Yuqori tezlikda to'g'ridan-to'g'ri yuklab olish havolasini olish uchun Telegram media-ga javob bering"
    REPLY_TO_DOC_FOR_C2V = "O'zgartirish uchun Telegram media-ga javob bering"
    REPLY_TO_DOC_FOR_SCSS = "Skrinshotlarni olish uchun Telegram media-ga javob bering"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Telegram media-ga /rename ga maxsus eskiz yordami bilan javob bering"
    AFTER_GET_DL_LINK = "To'g'ridan-to'g'ri ulanish <a href='{}'> Yaratilgan </a> {} kun davomida amal qiladi.\n© @uploadsavebot"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Sintaksis: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "Avval uni mahalliy tilimga yuklab olish uchun har qanday ommaviy axborot vositalariga /downloadmedia ni yuboring.\nHozir yuklab olingan ommaviy axborot vositalarini bilish uchun yuborish /storageinfo."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video davomiyligi: {}\nUshbu mediani saqlash joyimdan o'chirish uchun yuboring /clearffmpegmedia.\nSend /trim HH:MM:SS [HH:MM:SS] Yuqoridagi ommaviy axborot vositalaridan kichkina foto/video."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "Saqlangan media allaqachon mavjud. Mavjud media tafsilotlarini bilish uchun iltimos, saqlash ma'lumotlarini yuboring."
    USER_DELETED_FROM_DB = "Ma'lumotlar bazasidan <a href='tg://user?id={}'> {} </a> foydalanuvchi o'chirildi."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Ichki oqimlarni olish uchun Telegram media-ga (MKV) javob bering"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Shaxsiy rasmlarni yaratish uchun media albomga javob bering / generatecustomthumbnail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.me/RedFoc"
    EXTRACT_ZIP_INTRO_ONE = "Avval siqilgan faylni yuboring, keyin javob /unzip buyrug'ini faylga yuboring."
    EXTRACT_ZIP_INTRO_THREE = "Qabul qilingan faylni tahlil qilish. ⚠️ Bu biroz vaqt talab qilishi mumkin. Iltimos, sabr qiling."
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Kechirasiz. Siqilgan faylni qayta ishlash paytida xatolar yuz berdi. Iltimos, hamma narsani yana ikki marta tekshiring va agar muammo takrorlanmasa, bu haqda xabar bering <a href='https://telegram.me/SHAVKAT'>@abdulloev_shavkat</a>"
    EXTRACT_ZIP_STEP_TWO = """Quyidagi variantlardan yuklash uchun fayl_nomini tanlang.
Faylni olgandan so'ng, uni kichik rasmlarni qo'llab-quvvatlash bilan qayta nomlash uchun siz /rename buyrug'idan foydalanishingiz mumkin."""
    CANCEL_STR = "Jarayon bekor qilindi"
    ZIP_UPLOADED_STR = "{} Fayllarni {} sekund ichida yukladi"
    FREE_USER_LIMIT_Q_SZE = """Qayta ishlash mumkin emas.
Bepul foydalanuvchilar 30 daqiqada atigi bitta so'rov.
/upgrade yoki 1800 soniyadan keyin harakat qilib ko'ring."""
    SLOW_URL_DECED = "URL juda sekin ko'rinadi. Siz mening uyimni aylantirganingiz uchun, men ushbu faylni yuklab olishga xayolim yo'q. Shu bilan birga, nega bunday qilmayapsiz: ==> https://t.me/abdulloev_shavkat va menga tezkor URL manzilini olib keling, shunda men boshqa foydalanuvchilar uchun sekinlashmasdan Telegram-ga yuklay olaman."
