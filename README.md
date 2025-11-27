
# ADVANCED RAT CONTROL PANEL

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Educational-orange.svg)

**ADVANCED RAT CONTROL PANEL** — bu Python dasturlash tilida yozilgan ochiq manbali (Open Source) loyiha. 

Ushbu vosita quyidagi maqsadlarda yaratilgan:
* Masofaviy boshqaruv tizimlari (Remote Administration Tool) arxitekturasi qanday ishlashini tushunish.
* Client-Server aloqalari va soket dasturlashni (Socket Programming) o'rganish.
* Kiberxavfsizlik va tarmoq himoyasi bo'yicha bilimlarni amaliy oshirish.

> **⚠️ DIQQAT:** Ushbu dastur faqat **ta'lim va qonuniy pentesting (tizimni tekshirish)** uchun mo'ljallangan. Undan g'arazli maqsadlarda foydalanish qat'iyan man etiladi.

---

## 📥 Yuklab Olish va O'rnatish

Dasturni ishga tushirish uchun kompyuteringizda **Python 3** o'rnatilgan bo'lishi kerak.

**1. Repozitoriyani yuklab oling:**
Terminal yoki CMD ni ochib quyidagi buyruqni kiriting:

```bash
git clone https://github.com/VIPOS-testuser/ADVANCED_RAT_CONTROL_PANEL.git
```

**2. Papkaga kiring:**

```bash
cd ADVANCED_RAT_CONTROL_PANEL
```

**3. Kerakli kutubxonalarni o'rnating:**
Dastur asosan standart kutubxonalardan foydalanadi. `.exe` formatidagi payload yaratish uchun `pyinstaller` va  talab qilinadi:

```bash
pip install pyinstaller
```

**4. Dasturni ishga tushiring:**

```bash
python main.py
```

-----

## 🖥 Dastur Interfeysi

Dastur ishga tushganda siz quyidagi boshqaruv panelini ko'rasiz. Bu menyu orqali serverni sozlash, payload yaratish va mijozlarni boshqarish mumkin.

```text
╔══════════════════════════════════════════════════════════╗
║                ADVANCED RAT CONTROL PANEL                ║
╠══════════════════════════════════════════════════════════╣
║ Author  : @Xorazmlik_2004                                ║
║ Version : TEST v1                                        ║
╚══════════════════════════════════════════════════════════╝

    Server: [OFF]  |  Port: 4444
    Payload IP: 127.0.0.1

╔════════════════════════════════════════╗
║ 1. Sozlamalar (IP/Port)                ║
║ 2. Serverni Ishga Tushirish            ║
║ 3. Payload Yaratish (.py - Script)     ║
║ 4. Payload Yaratish (.exe - Dastur)    ║
║ 5. Ulanganlar Ro'yxati                 ║
║ 6. Boshqarish (Select ID)              ║
║ 7. Chiqish                             ║
╚════════════════════════════════════════╝

>> Tanlang:
```

-----

## ⚙️ Imkoniyatlari

  * **Server Konfiguratsiyasi:** IP manzil va Portni dastur ichida dinamik o'zgartirish imkoniyati.
  * **Multi-Client Support:** Bir vaqtning o'zida bir nechta ulanishlarni qabul qilish va boshqarish.
  * **Payload Generator:**
      * `.py` (Python skripti) — Ochiq manbali, o'rganish uchun qulay payload.
      * `.exe` (Windows Dasturi) — Python o'rnatilmagan muhitlar uchun (PyInstaller yordamida).
  * **Barqaror Aloqa:** Sinxronizatsiya muammolari hal qilingan (Sync Fix).
  * **CLI Interfeys:** Qulay va tushunarli buyruqlar qatori interfeysi.

-----

## ⚠️ Qonuniy Ogohlantirish (Disclaimer)

Ushbu dasturiy ta'minot (**ADVANCED RAT CONTROL PANEL**) muallifi (@Xorazmlik\_2004) va hissa qo'shuvchilar ushbu vositadan noto'g'ri foydalanish oqibatlari uchun javobgar emas.

1.  **Faqat Ta'lim Uchun:** Ushbu kod tarmoq xavfsizligi mutaxassislari va tizim ma'murlari o'z tarmoqlarini himoya qilishni o'rganishlari uchun yozilgan.
2.  **Ruxsatsiz Foydalanish Taqiqlanadi:** Ushbu dasturni o'zingizga tegishli bo'lmagan yoki egasining yozma ruxsati bo'lmagan kompyuter/tarmoqlarda ishlatish **NOQONUNIY** hisoblanadi va mahalliy hamda xalqaro qonunchilikka asosan jinoiy javobgarlikka sabab bo'lishi mumkin.
3.  **Mas'uliyat:** Dasturni yuklab olish va ishlatish orqali siz barcha javobgarlikni o'z zimmangizga olasiz va undan faqat qonuniy maqsadlarda foydalanishga rozilik bildirasiz.

-----

**Author:** @Xorazmlik\_2004  
**GitHub:** [VIPOS-testuser](https://www.google.com/search?q=https://github.com/VIPOS-testuser)
