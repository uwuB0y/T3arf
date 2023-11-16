import telebot
from telebot.types import InlineKeyboardMarkup as MK , InlineKeyboardButton as BTN
from kvsqlite.sync import Client
import random

owner = 6075471009 #ur ID
ownerUN = "susiraq" #ur userName 
Chn = "-1001878107253" #channel id , Note: You must make the bot admin in the channel , except that it won't work
ChnUN = "TeAMoN404"

Gays = ['creator','member','administrator']

TOKEN = "zxzxzxzxzxzxzxzxzxz" #ur bot token

Tho = telebot.TeleBot(
    TOKEN,
    parse_mode="Markdown",
    disable_web_page_preview=True,
    skip_pending=True,
    num_threads=40
)
db = Client("T3arf.sqlite", "users")
ban = Client("T3arf.sqlite", "ban_users")
adm = Client("T3arf.sqlite", "admins")

startMaD = "*مرحبا بك في لوحة الادمن*" # start message for admin
startM = f"*مرحبًا بك مجددًا في بوت التعارف\nأختر احد الازرار ادناه\nـ----------  ----------  ----------\nDev bY ->* [Tho](t.me/{ownerUN}) ." # start message for users

@Tho.message_handler(commands=["start"])
def start(msg):
    idU = msg.from_user.id
    if Tho.get_chat_member(Chn, idU).status not in Gays:
        Tho.reply_to(msg, f"*عذرًا عزيزي\nأشترك بنقاة البوت حتى تكدر تستخدمة\n\n- @{ChnUN}\nأشترك وأرسل /start*")
        return
    else:pass
    if ban.exists(f"user_{idU}"):
        Tho.reply_to(msg, f"*أنت محظور من استعمال البوت\n لو كنت تظن انه اجراء خاطئ\n تواصل معي:\n- @{ownerUN}*")
        return
    else:pass
    if idU == owner or adm.exists(f"user_{idU}"):
        ad = MK(row_width=1)
        brod = BTN("أذاعة", callback_data="brod")
        status = BTN("ألاحصائيات", callback_data="stats")
        banD = BTN("حظر مستخدم", callback_data="ban")
        unbanD = BTN("الغاء حظر", callback_data="unban")
        ADad = BTN("رفع ادمن", callback_data="ADad")
        RMad = BTN("تنزيل ادمن", callback_data="RMad")
        file = BTN("أرسل التخزين", callback_data="send")
        ad.row(brod,status)
        ad.row(unbanD,banD)
        ad.row(RMad,ADad)
        ad.row(file)
        Tho.reply_to(msg, text=startMaD, reply_markup=ad)
    if db.exists(f"user_{idU}"):
        ky = MK(row_width=1)
        btn11 = BTN("معلوماتي", callback_data="MyInfo")
        btn22 = BTN("أقترح شريكي", callback_data="find")
        ky.row(btn11, btn22)
        Tho.reply_to(msg, text=startM, reply_markup=ky)
        return
    else:
        btn = MK(row_width=1)
        btn1 = BTN("أوافق", callback_data="yes")
        btn.row(btn1)
        Tho.reply_to(msg, '''*أهلاً بك في بوت التعارف
عند استخدامك للبوت فانت توافق على مايلي:
- الدردشة معك في البرايفت جات (بالخاص)
- مشاركة اسمك الاول و جنسك وعمرك
اضغط على الزر ادناه للمتابعة*''', reply_markup=btn)
        return

def find(idU, gnder, call):
    num = 0
    ids = []
    gay = db.keys('user_%')
    for ah in gay:
        ah = ah[0]
        try:
            getID = db.get(ah)["id"]
            print(f"get ID: {getID}")
            if db.get(ah)["gnder"] == db.get(f"user_{idU}")["gnder"] and gnder == True and getID != idU:
                ids.append(int(getID))
                print(f"done put {getID} in the list : gnder : {gnder}")
                num +=1
            elif db.get(ah)["gnder"] != db.get(f"user_{idU}")["gnder"] and gnder == False and getID != idU:
                ids.append(int(getID))
                print(f"done put {getID} in the list : gnder : {gnder}")
                num +=1
        except Exception as e:
            print(f"{e}")
            continue
    if num >= 1:
        idd = random.choice(ids)
        print(f"done choice the id: {idd}")
        try:
            userN = f"@{Tho.get_chat(idd).username}"
        except:
            userN = "لا يوجد"    
        try:
            c = MK(row_width=1)
            Fi = BTN("أبحث مجدداً", callback_data="find")
            bcv = BTN("رجوع", callback_data="back")
            c.row(Fi, bcv)
            finl = db.get(f"user_{idd}")
            name = finl["name"]
            gnderR = finl["gnder"]
            age = int(finl["age"])
            print(f"name:{name}\ngnder:{gnderR}\nage:{age}")
            Tho.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.id,
                reply_markup=c,
                text=f"*وجِدَ شريكٌ لكَ!\n- أسمه: *[{name}](tg://user?id={idd})* .\n- عمره: {age} .\n- جنسه: {gnderR} .\n- يوزره: {userN} .\n - *[Dev](t.me/{ownerUN}) ."
                )
            return
        except Exception as e:
            print(e)
    else:
        v = MK(row_width=1)
        bc = BTN("رجوع", callback_data="back")
        v.row(bc)
        Tho.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=f"*لا توجد نتائج*",
            reply_markup=v
            )
        print("no results")
        return

@Tho.callback_query_handler(func=lambda call: True)
def callback(call):
    idU = call.from_user.id
    if Tho.get_chat_member(Chn, idU).status not in Gays:
        Tho.send_message,(call.message.chat.id, f"*عذرًا عزيزي\nأشترك بنقاة البوت حتى تكدر تستخدمة\nـ---------------------------\n- @{ChnUN}\nأشترك وأرسل /start*")
        return
    
    if ban.exists(f"user_{idU}"):
        Tho.send_message(call.message.chat.id, f"*أنت محظور من استعمال البوت\n لو كنت تظن انه اجراء خاطئ\n تواصل معي:\n- @{ownerUN}*")
        return
    
    if call.data == "brod":
        Tho.register_next_step_handler(
            Tho.send_message(call.message.chat.id, "*أرسل النص المراد أذاعته*"),
            brodC
        )
        return

    if call.data == "backAD":
        ad = MK(row_width=1)
        brod = BTN("أذاعة", callback_data="brod")
        status = BTN("ألاحصائيات", callback_data="stats")
        banD = BTN("حظر مستخدم", callback_data="ban")
        unbanD = BTN("الغاء حظر", callback_data="unban")
        ADad = BTN("رفع ادمن", callback_data="ADad")
        RMad = BTN("تنزيل ادمن", callback_data="RMad")
        file = BTN("أرسل التخزين", callback_data="send")
        ad.row(brod,status)
        ad.row(unbanD,banD)
        ad.row(RMad,ADad)
        ad.row(file)
        Tho.edit_message_text(
            text=startMaD,
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            reply_markup=ad
        )
        return
    
    if call.data == "stats":
        kysU = db.keys(f"user_%")
        kysB = ban.keys(f"user_%")
        kysAD = adm.keys(f"user_%")
        Tu = 0
        Tb = 0
        Tad = 0
        try:
            for _ in kysU:
                Tu += 1
        except TypeError:
            Tu = 0
        try:
            for _ in kysB:
                Tb += 1
        except TypeError:
            Tb = 0
        try:
            for _ in kysAD:
                Tad += 1
        except TypeError:
            Tad = 0
        kyss = MK(row_width=1)
        btcR = BTN("رجوع", callback_data="backAD")
        kyss.row(btcR)
        Tho.edit_message_text(
            text=f"*أهلاً بكَ في قسم الاحصائيات\nعدد مستخدمين البوت: {Tu} .\nعدد الادمنية: {Tad} .\nعدد المحظورين: {Tb} .*",
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            reply_markup=kyss
        )
        return

    if call.data == "ban":
        Tho.register_next_step_handler(
            Tho.send_message(call.message.chat.id, "*أرسل الأيدي المراد حظره*"),
            banU
        )
        return
    
    if call.data == "unban":
        Tho.register_next_step_handler(
            Tho.send_message(call.message.chat.id, "*أرسل الايدي المراد الغاء حظره*"),
            unbanU
        )
        return
    
    if call.data == "ADad":
        if idU == owner:
            Tho.register_next_step_handler(
                Tho.send_message(call.message.chat.id, "*أرسل الايدي*"),
                ADadU
            )
            return
        else:
            Tho.send_message(call.message.chat.id, "*هذا الامر للمالك فقط*")
            return
            
    if call.data == "RMad":
        if idU == owner:
            Tho.register_next_step_handler(
                Tho.send_message(call.message.chat.id, "*أرسل الايدي*"),
                RMadU
            )
            return
        else:
            Tho.send_message(call.message.chat.id, "*هذا الامر للمالك فقط*")
            return
    
    if call.data == "send":
        if idU == owner:
            Tho.send_document(call.message.chat.id, open("T3arf.sqlite", 'rb'))
            return
        else:
            Tho.send_message(call.message.chat.id, "*هذا الامر للمالك فقط*")
            return

    if call.data == "yes":
        btn = MK(row_width=1)
        Male,Female = BTN("ذكر", callback_data="Male"), BTN("أنثى", callback_data="Female")
        btn.row(Female, Male)
        Tho.edit_message_text(
            text="*أختر جنسك من الازرار ادناه*",
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            reply_markup=btn
        )
        return

    if call.data == "Male":
        Tho.register_next_step_handler(
            Tho.send_message(call.message.chat.id, "*أرسل اسمك و عمرك بهذا الشكل:\n\nذوالفقار 15\nاذا جان أسمك مركب ادمجة مثل عبد العزيز\nيصير عبدالعزيز*"),
            addM
        )
        Tho.delete_message(call.message.chat.id, call.message.id, 500)
        return

    if call.data == "Female":
        Tho.register_next_step_handler(
            Tho.send_message(call.message.chat.id, "*أرسلي أسمكِ وعمركِ بهذا الشكل:\n\nنباء 15\nاذا جان أسمج مركب ادمجيه مثل نور الهدى\nيصير نورالهدى*"),
            addF
        )
        Tho.delete_message(call.message.chat.id, call.message.id, 500)
        return

    if call.data == "MyInfo":
        info = db.get(f"user_{idU}")
        name = info["name"]
        age = info["age"]
        gnder = info["gnder"]
        ky = MK(row_width=1)
        btnR = BTN("رجوع", callback_data="back")
        btn7 = BTN("حذف معلوماتي", callback_data="del")
        ky.row(btn7, btnR)
        Tho.edit_message_text(
            f"*- أسمك: {name}.\n- عمرك: {int(age)}.\n- جنسك: {gnder}.\n----------  ----------  ----------\n-* [Dev](t.me/{ownerUN}).",
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            reply_markup=ky
        )
        return

    if call.data == "back":
        ky = MK(row_width=1)
        btna = BTN("معلوماتي", callback_data="MyInfo")
        btnb = BTN("أقترح شريكي", callback_data="find")
        ky.row(btna, btnb)
        Tho.edit_message_text(
            startM,
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            reply_markup=ky
        )
        return

    if call.data == "del":
        db.delete(f"user_{idU}")
        Tho.edit_message_text(
            "*تم حذفك من قاعدة البيانات\nلو تريد التسجيل مجدداً أرسل /start*",
            chat_id=call.message.chat.id,
            message_id=call.message.id
        )
        return

    if call.data == "find":
        n = MK(row_width=1)
        yy = BTN("نفس جنسي", callback_data="yy")
        nn = BTN("الجنس المغاير", callback_data="nn")
        bc = BTN("رجوع", callback_data="back")
        n.row(nn, yy)
        n.row(bc)
        Tho.edit_message_text(
            "*هل تريد التعرف على من بنفس جنسك\nأو من الجنس المغاير؟*",
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            reply_markup=n
        )
        return

    if call.data == "yy":
        Tho.edit_message_text(
            "*جارِ البحث ، أنتظر قليلاً من فضلِك*",
            chat_id=call.message.chat.id,
            message_id=call.message.id
        )
        find(
            idU,
            True,
            call
        )
        return

    if call.data == "nn":
        Tho.edit_message_text(
            "*جارِ البحث ، أنتظر قليلاً من فضلِك*",
            chat_id=call.message.chat.id,
            message_id=call.message.id
        )
        find(
            idU,
            False,
            call
        )
        return

def add(msg, gnder, data):
    idu = msg.from_user.id
    data = data.split(" ")
    if len(data) > 2 or len(data) < 2:
        Tho.reply_to(msg, "*أدخال خاطئ\n أرسل /start للمحاولة مجدداً*")
        return
    else:
        try:
            age = float(data[1])
            name = data[0]
            if float(age) <= 12:
                Tho.reply_to(msg, f"*عذرًا أنت صغير جداً\n- تم حظرك من البوت\nلو كنت تظن انه اجراء خاطئ\n تواصل معي:\n- @{ownerUN}*")
                ban.set(f"user_{idu}", {"id":idu})
                return
            elif float(age) >= 100:
                Tho.reply_to(msg, "*عمر كبير جداً\nأرسل /start وحاول مجدداً*")
                return
            else:
                if len(name) <= 1 or len(name) >= 15:
                    Tho.reply_to(msg, "*أسم غير صالح\nأرسل /start وحاول مجدداً*")
                    return
                else:
                    db.set(
                        f"user_{idu}",
                        {"id":int(idu),
                        "name":name,
                        "gnder":gnder,
                        "age":int(age),
                        }
                    )
                    ky = MK(row_width=1)
                    btn11 = BTN("معلوماتي", callback_data="MyInfo")
                    btn22 = BTN("أقترح شريكي", callback_data="find")
                    ky.row(btn11, btn22)
                    Tho.reply_to(msg, startM, reply_markup=ky)
                    Tho.send_message(owner, f"*- مستخدم جديد!\nأسمه: *[{msg.from_user.first_name}](tg://user?id={idu})* .\nأيديه: *`{idu}`* .\nيوزره: @{msg.from_user.username} .*".replace("@None", "لايوجد"))
                    return
        except:
            Tho.reply_to(msg, "*أدخل العمر رقماً فقط\nأرسل /start للمحاولة مجدداً*")
            return

def brodC(msg):
    if adm.exists(f'user_{msg.from_user.id}') or msg.from_user.id == owner:
        kys = db.keys(f'user_%')
        lstKys = []
        T = 0
        for id in kys:
            m = db.get(id[0])['id']
            lstKys.append(m)
            T += 1
        D = 0
        F = 0
        Tho.reply_to(msg, f"*جارِ الاذاعة لـ{T} مستخدم*")
        for user in lstKys:
            try:
                Tho.copy_message(chat_id=user,from_chat_id=msg.chat.id,message_id=msg.message_id)
                D += 1
            except:
                F += 1
                continue
        Tho.reply_to(msg,f"*عدد مستخدمين البوت {T} .\nأكتمات لـ {D} .\nفشلت لـ {F} .*")
        return
    else:
        Tho.reply_to(msg,"*عذرا أنت مو ادمن*")
        return

def banU(msg):
    idU = msg.text.strip()
    if ban.exists(f"user_{idU}"):
        Tho.reply_to(msg,"*هذا المستخدم أصلا محظور*")
        return
    else:
        ban.set(f"user_{idU}", {"id":idU})
        Tho.reply_to(msg, "*تم حظر المستخدم بنجاح*")
        return

def unbanU(msg):
    idU = msg.text.strip()
    if not ban.exists(f"user_{idU}"):
        Tho.reply_to(msg,"*هذا المستخدم أصلا مو محظور*")
        return
    else:
        ban.delete(f"user_{idU}")
        Tho.reply_to(msg, "*تم الغاء حظره بنجاح*")
        return

def ADadU(msg):
    idU = msg.text.strip()
    if adm.exists(f"user_{idU}"):
        Tho.reply_to(msg,"*هذا المستخدم أصلا أدمن*")
        return
    else:
        adm.set(f"user_{idU}", {"id":idU})
        Tho.reply_to(msg, "*تم رفع المستخدم بنجاح*")
        return

def RMadU(msg):
    idU = msg.text.strip()
    if not adm.exists(f"user_{idU}"):
        Tho.reply_to(msg,"*هذا المستخدم أصلا مو أدمن*")
        return
    else:
        adm.delete(f"user_{idU}")
        Tho.reply_to(msg, "*تنزيل المستخدم بنجاح*")
        return

def addM(msg):
    data = msg.text
    add(
        msg,
        "ذكر",
        data
    )
    return

def addF(msg):
    data = msg.text
    add(
        msg,
        "أنثى",
        data
    )
    return

print("Bot Started !...")
Tho.infinity_polling()