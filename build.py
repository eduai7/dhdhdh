"""Генератор статических страниц сайта. Запуск: python3 build.py <out_dir>"""
import random, sys, pathlib

OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "../site")

# ---------- иконки ----------
IC = {
 "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
 "drop": '<path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"/>',
 "wind": '<path d="M17.7 7.7a2.5 2.5 0 1 1 1.8 4.3H2"/><path d="M9.6 4.6A2 2 0 1 1 11 8H2"/><path d="M12.6 19.4A2 2 0 1 0 14 16H2"/>',
 "tree": '<path d="m17 14 3 3.3a1 1 0 0 1-.7 1.7H4.7a1 1 0 0 1-.7-1.7L7 14h-.3a1 1 0 0 1-.7-1.7L9 9h-.2A1 1 0 0 1 8 7.3L12 3l4 4.3a1 1 0 0 1-.8 1.7H15l3 3.3a1 1 0 0 1-.7 1.7H17Z"/><path d="M12 22v-3"/>',
 "mountain": '<path d="m8 3 4 8 5-5 5 15H2L8 3z"/>',
 "waves": '<path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M6.3 17.7l-1.4 1.4M19.1 4.9l-1.4 1.4"/>',
 "flame": '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.07-2.14-.22-4.05 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.15.43-2.29 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
 "trash": '<path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/>',
 "factory": '<path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/>',
 "paw": '<circle cx="11" cy="4" r="2"/><circle cx="18" cy="8" r="2"/><circle cx="20" cy="16" r="2"/><path d="M9 10a5 5 0 0 1 5 5v3.5a3.5 3.5 0 0 1-6.84 1.05Q6.52 17.48 4.46 16.84A3.5 3.5 0 0 1 5.5 10Z"/>',
 "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20"/>',
 "recycle": '<path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/>',
 "sprout": '<path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/>',
 "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 "landmark": '<path d="M3 22h18"/><path d="M6 18v-7M10 18v-7M14 18v-7M18 18v-7"/><path d="m12 2 8 5H4z"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 "bulb": '<path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7V16h8v-1.3A7 7 0 0 0 12 2z"/>',
 "bike": '<circle cx="5.5" cy="17.5" r="3.5"/><circle cx="18.5" cy="17.5" r="3.5"/><path d="M15 6h2l3 11.5M5.5 17.5 9 9h6l-3 8.5"/>',
 "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
 "check": '<path d="M5 12l5 5L20 7"/>',
 "bird": '<path d="M16 7h.01"/><path d="M3.4 18H12a8 8 0 0 0 8-8V7a4 4 0 0 0-7.28-2.3L2 20"/><path d="m20 7 2 .5-2 .5"/><path d="M10 18v3M14 17.75V21M7 18a6 6 0 0 0 3.84-10.61"/>',
}
def icon(name, cls="icon"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{IC[name]}</svg>'

# ---------- помощники для двух языков ----------
def t(ru, uz):            # строчный текст
    return f'<span data-l="ru">{ru}</span><span data-l="uz">{uz}</span>'
def el(tag, ru, uz, attrs=""):  # блочный элемент на двух языках
    a = f" {attrs}" if attrs else ""
    return f'<{tag}{a} data-l="ru">{ru}</{tag}><{tag}{a} data-l="uz">{uz}</{tag}>'

# ---------- лес для hero ----------
def forest_svg(seed=3):
    rnd = random.Random(seed)
    layers = [("#4A4D3E", .55, 230, 60), ("#3a3d30", .8, 300, 46), ("#2C3022", 1, 360, 34)]
    out = ['<svg class="forest" viewBox="0 0 1440 400" preserveAspectRatio="none" aria-hidden="true">']
    for color, op, base, w in layers:
        d = f"M0 400 L0 {base} "
        x = -10
        while x < 1460:
            h = rnd.randint(70, 190) if base < 300 else rnd.randint(60, 160)
            ww = w * rnd.uniform(.7, 1.3)
            top = base - h
            d += f"L{x:.0f} {base} L{x+ww*.18:.0f} {base-h*.35} L{x+ww*.08:.0f} {base-h*.35} L{x+ww*.32:.0f} {base-h*.68} L{x+ww*.22:.0f} {base-h*.68} L{x+ww/2:.0f} {top} L{x+ww*.78:.0f} {base-h*.68} L{x+ww*.68:.0f} {base-h*.68} L{x+ww*.92:.0f} {base-h*.35} L{x+ww*.82:.0f} {base-h*.35} L{x+ww:.0f} {base} "
            x += ww * rnd.uniform(.55, .9)
        d += "L1440 400 Z"
        out.append(f'<path fill="{color}" opacity="{op}" d="{d}"/>')
    out.append("</svg>")
    return "".join(out)

# ---------- страницы ----------
PAGES = [
    ("index.html",      "Главная",              "Bosh sahifa"),
    ("ecosystems.html", "Экосистемы",           "Ekotizimlar"),
    ("threats.html",    "Угрозы",               "Tahdidlar"),
    ("protect.html",    "Как сохранить",        "Qanday asraymiz"),
    ("uzbekistan.html", "Природа Узбекистана",  "Oʻzbekiston tabiati"),
    ("habits.html",     "Эко-привычки",         "Eko-odatlar"),
    ("about.html",      "О проекте",            "Loyiha haqida"),
]
SITE_RU, SITE_UZ = "Зелёный мир", "Yashil dunyo"

def layout(fname, title_ru, title_uz, body, extra_js=""):
    nav = "".join(
        f'<a href="{f}"{" class=\"active\"" if f == fname else ""}>{t(r, u)}</a>' for f, r, u in PAGES)
    foot_links = "".join(f'<li><a href="{f}">{t(r, u)}</a></li>' for f, r, u in PAGES)
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_ru} — {SITE_RU}</title>
<meta name="description" content="Сайт о природе и о том, как её сохранить. Tabiat va uni asrash haqida sayt.">
<meta name="theme-color" content="#2C3022">
<script>try{{var l=localStorage.getItem("lang");if(l)document.documentElement.lang=l}}catch(e){{}}</script>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23C2A75A' stroke-width='2'%3E{IC["leaf"].replace('"', "'").replace("#", "%23")}%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:wght@500;600;700&family=Manrope:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body data-title-ru="{title_ru} — {SITE_RU}" data-title-uz="{title_uz} — {SITE_UZ}">
<header class="header">
  <div class="container">
    <a href="index.html" class="logo">{icon("leaf")}{t(SITE_RU, SITE_UZ)}</a>
    <nav class="nav">{nav}</nav>
    <div class="lang-switch" role="group" aria-label="Language">
      <button data-set="ru">RU</button><button data-set="uz">UZ</button>
    </div>
    <button class="burger" aria-label="Menu">{icon("menu")}</button>
  </div>
</header>
<main>
{body}
</main>
<footer class="footer">
  <div class="container">
    <div class="cols">
      <div>
        <a href="index.html" class="logo">{icon("leaf")}{t(SITE_RU, SITE_UZ)}</a>
        {el("p", "Образовательный проект о природе и её защите. Каждое маленькое действие имеет значение.",
               "Tabiat va uni muhofaza qilish haqidagi taʼlimiy loyiha. Har bir kichik harakat muhim.", 'style="margin-top:12px"')}
        <div class="palette"><i style="background:#B5A68A"></i><i style="background:#C2A75A"></i><i style="background:#7A6524"></i><i style="background:#4A4D3E"></i><i style="background:#2C3022"></i></div>
      </div>
      <div><h4>{t("Страницы", "Sahifalar")}</h4><ul>{foot_links}</ul></div>
      <div>
        <h4>{t("Помните", "Esda tuting")}</h4>
        {el("p", "Природа не нуждается в людях. Люди нуждаются в природе.", "Tabiatga inson kerak emas. Insonga tabiat kerak.")}
      </div>
    </div>
    <div class="copy">© 2026 {t(SITE_RU, SITE_UZ)}</div>
  </div>
</footer>
{extra_js}
<script src="js/main.js"></script>
</body>
</html>'''

def hero(eyebrow, h1, lead, small=True, buttons=""):
    return f'''<section class="hero{' small' if small else ''}">
  <div class="container hero-content">
    <span class="eyebrow">{t(*eyebrow)}</span>
    {el("h1", *h1)}
    {el("p", *lead, 'class="lead"')}
    {buttons}
  </div>
  {forest_svg(len(h1[0]))}
  <div class="fog"></div>
</section>'''

def head(h2, p=None):
    return f'<div class="section-head reveal">{el("h2", *h2)}{el("p", *p) if p else ""}</div>'

def card(ic, h3, p, cls="", tag=None):
    tg = f'<span class="tag">{t(*tag)}</span>' if tag else ""
    return f'<div class="card reveal {cls}"><div class="badge">{icon(ic)}</div>{el("h3", *h3)}{el("p", *p)}{tg}</div>'

def write(fname, html):
    (OUT / fname).write_text(html, encoding="utf-8")

# =====================================================================
# 1. ГЛАВНАЯ
# =====================================================================
links = [
  ("ecosystems.html", "globe", ("Экосистемы", "Ekotizimlar"), ("Леса, болота, горы, пустыни и океаны — как устроена жизнь на Земле.", "Oʻrmonlar, botqoqliklar, togʻlar, choʻllar va okeanlar — Yerdagi hayot qanday tuzilgan.")),
  ("threats.html", "flame", ("Угрозы", "Tahdidlar"), ("Что разрушает природу: вырубка, мусор, изменение климата.", "Tabiatni nima buzmoqda: daraxt kesish, chiqindi, iqlim oʻzgarishi.")),
  ("protect.html", "sprout", ("Как сохранить", "Qanday asraymiz"), ("Решения на уровне государства, города и каждого человека.", "Davlat, shahar va har bir inson darajasidagi yechimlar.")),
  ("uzbekistan.html", "mountain", ("Природа Узбекистана", "Oʻzbekiston tabiati"), ("Аральское море, заповедники и редкие животные нашей страны.", "Orol dengizi, qoʻriqxonalar va yurtimizning noyob hayvonlari.")),
  ("habits.html", "recycle", ("Эко-привычки", "Eko-odatlar"), ("Интерактивный чек-лист: отмечайте полезные привычки.", "Interaktiv roʻyxat: foydali odatlaringizni belgilang.")),
  ("about.html", "bulb", ("О проекте и тест", "Loyiha va test"), ("Зачем этот сайт и проверка ваших знаний.", "Sayt nima uchun va bilimingizni sinab koʻring.")),
]
link_cards = "".join(
  f'<a href="{h}" class="card reveal"><div class="badge">{icon(ic)}</div>{el("h3", *hh)}{el("p", *pp)}<div class="more">{t("Подробнее →", "Batafsil →")}</div></a>'
  for h, ic, hh, pp in links)

body = hero(
  ("Сохраним природу вместе", "Tabiatni birga asraymiz"),
  ("Природа — наш общий дом", "Tabiat — umumiy uyimiz"),
  ("Леса, реки, болота и горы дают нам воздух, воду и пищу. Узнайте, что им угрожает и что может сделать каждый из нас уже сегодня.",
   "Oʻrmonlar, daryolar, botqoqliklar va togʻlar bizga havo, suv va oziq beradi. Ularga nima tahdid solayotganini va har birimiz bugunoq nima qila olishimizni bilib oling."),
  small=False,
  buttons=f'<div class="btns"><a href="protect.html" class="btn btn-primary">{t("Как помочь природе", "Tabiatga qanday yordam beramiz")}</a><a href="ecosystems.html" class="btn btn-ghost">{t("Узнать больше", "Koʻproq bilish")}</a></div>'
) + f'''
<section class="block">
  <div class="container">
    {head(("Почему это важно", "Nega bu muhim"), ("Всё живое на планете связано между собой. Когда исчезает одно звено, страдает вся цепочка — включая человека.", "Sayyoradagi barcha tirik mavjudotlar oʻzaro bogʻliq. Bitta boʻgʻin yoʻqolsa, butun zanjir, jumladan inson ham zarar koʻradi."))}
    <div class="grid">
      {card("wind", ("Чистый воздух", "Toza havo"), ("Растения и фитопланктон в океане вырабатывают кислород и поглощают углекислый газ.", "Oʻsimliklar va okeandagi fitoplankton kislorod ishlab chiqaradi va karbonat angidridni yutadi."))}
      {card("drop", ("Пресная вода", "Chuchuk suv"), ("Леса, ледники и болота накапливают и очищают воду, которую мы пьём.", "Oʻrmonlar, muzliklar va botqoqliklar biz ichadigan suvni toʻplaydi va tozalaydi."))}
      {card("paw", ("Разнообразие жизни", "Hayot xilma-xilligi"), ("Миллионы видов растений и животных опыляют поля, очищают почву и поддерживают баланс.", "Millionlab oʻsimlik va hayvon turlari ekinlarni changlatadi, tuproqni tozalaydi va muvozanatni saqlaydi."), "gold")}
    </div>
  </div>
</section>
<section class="block alt">
  <div class="container">
    {head(("Исследуйте сайт", "Saytni oʻrganing"))}
    <div class="grid">{link_cards}</div>
  </div>
</section>
<section class="block">
  <div class="container">
    <div class="banner reveal">
      {el("h2", "Мы не унаследовали Землю от предков — мы берём её взаймы у наших детей", "Biz Yerni ajdodlardan meros olmaganmiz — uni farzandlarimizdan qarzga olganmiz")}
      {el("p", "Народная мудрость, которая сегодня актуальна как никогда.", "Bugun har qachongidan ham dolzarb boʻlgan xalq hikmati.")}
    </div>
  </div>
</section>'''
write("index.html", layout("index.html", "Главная", "Bosh sahifa", body))

# =====================================================================
# 2. ЭКОСИСТЕМЫ
# =====================================================================
body = hero(("Как устроена природа", "Tabiat qanday tuzilgan"),
  ("Экосистемы Земли", "Yer ekotizimlari"),
  ("Экосистема — это сообщество живых организмов и среда, в которой они живут. Каждая из них по-своему важна для планеты.",
   "Ekotizim — tirik organizmlar jamoasi va ular yashaydigan muhit. Ularning har biri sayyora uchun oʻziga xos ahamiyatga ega.")) + f'''
<section class="block">
  <div class="container">
    <div class="grid">
      {card("tree", ("Леса", "Oʻrmonlar"), ("Покрывают около трети суши. Дом для большей части наземных видов, «лёгкие» планеты и защита почвы от эрозии.", "Quruqlikning qariyb uchdan bir qismini qoplaydi. Quruqlikdagi turlarning katta qismi uchun uy, sayyoraning «oʻpkasi» va tuproqni eroziyadan himoya qiladi."), tag=("Хранят углерод", "Uglerodni saqlaydi"))}
      {card("leaf", ("Болота и торфяники", "Botqoqlik va torfzorlar"), ("Работают как губка: удерживают воду, предотвращают наводнения и засухи. Торфяники хранят огромные запасы углерода.", "Gubka kabi ishlaydi: suvni ushlab turadi, toshqin va qurgʻoqchilikning oldini oladi. Torfzorlar ulkan uglerod zaxiralarini saqlaydi."), "gold", ("Природный фильтр", "Tabiiy filtr"))}
      {card("waves", ("Реки и озёра", "Daryo va koʻllar"), ("Источник пресной воды для людей, полей и животных. Очень чувствительны к загрязнению.", "Odamlar, dalalar va hayvonlar uchun chuchuk suv manbai. Ifloslanishga juda sezgir."), tag=("Пресная вода", "Chuchuk suv"))}
      {card("mountain", ("Горы", "Togʻlar"), ("Ледники в горах — «водонапорные башни» для равнин. Здесь живут редкие виды, например снежный барс.", "Togʻlardagi muzliklar tekisliklar uchun «suv minoralari». Bu yerda qor qoploni kabi noyob turlar yashaydi."), tag=("Ледники", "Muzliklar"))}
      {card("sun", ("Пустыни и степи", "Choʻl va dashtlar"), ("Только кажутся пустыми. Растения и животные здесь приспособились к жаре и нехватке воды.", "Faqat boʻsh koʻrinadi. Bu yerdagi oʻsimlik va hayvonlar issiqlik va suv tanqisligiga moslashgan."), tag=("Саксаул, джейран", "Saksovul, jayron"))}
      {card("globe", ("Океаны", "Okeanlar"), ("Покрывают больше 70% поверхности Земли, регулируют климат и дают значительную часть кислорода.", "Yer yuzasining 70% dan ortigʻini qoplaydi, iqlimni boshqaradi va kislorodning katta qismini beradi."), "gold", ("Климат", "Iqlim"))}
    </div>
  </div>
</section>
<section class="block alt">
  <div class="container grid-2">
    <div class="reveal">
      {el("h2", "Почему болота так важны", "Botqoqliklar nega muhim")}
      {el("p", "Болота долго считали «бесполезными» землями и осушали их. Сегодня учёные знают: это одни из самых ценных экосистем.", "Botqoqliklar uzoq vaqt «foydasiz» yer hisoblanib, quritilgan. Bugun olimlar bilishadi: bu eng qimmatli ekotizimlardan biri.")}
      {el("p", "Торфяники занимают лишь несколько процентов суши, но хранят больше углерода, чем все леса мира вместе взятые. Когда болото осушают, этот углерод попадает в атмосферу.", "Torfzorlar quruqlikning bir necha foizini egallaydi, lekin dunyodagi barcha oʻrmonlardan koʻproq uglerod saqlaydi. Botqoq quritilganda bu uglerod atmosferaga chiqadi.")}
      {el("p", "Кроме того, болота очищают воду, спасают от наводнений и дают дом перелётным птицам.", "Bundan tashqari, botqoqliklar suvni tozalaydi, toshqindan saqlaydi va koʻchmanchi qushlarga boshpana beradi.")}
    </div>
    <div class="panel reveal">{icon("bird")}</div>
  </div>
</section>
<section class="block">
  <div class="container">
    {head(("Цепочка жизни", "Hayot zanjiri"), ("Пример того, как всё связано:", "Hammasi qanday bogʻliqligiga misol:"))}
    <div class="steps">
      <div class="step reveal"><div>{el("h3", "Растения", "Oʻsimliklar")}{el("p", "Получают энергию солнца и создают органическое вещество.", "Quyosh energiyasini oladi va organik modda hosil qiladi.")}</div></div>
      <div class="step reveal"><div>{el("h3", "Травоядные", "Oʻtxoʻrlar")}{el("p", "Насекомые, птицы и звери питаются растениями и разносят семена.", "Hasharotlar, qushlar va hayvonlar oʻsimliklar bilan oziqlanadi va urugʻlarni tarqatadi.")}</div></div>
      <div class="step reveal"><div>{el("h3", "Хищники", "Yirtqichlar")}{el("p", "Регулируют численность травоядных и не дают им уничтожить растительность.", "Oʻtxoʻrlar sonini tartibga soladi va ularning oʻsimliklarni yoʻq qilishiga yoʻl qoʻymaydi.")}</div></div>
      <div class="step reveal"><div>{el("h3", "Разрушители", "Parchalovchilar")}{el("p", "Грибы и бактерии превращают остатки в плодородную почву — и круг замыкается.", "Zamburugʻ va bakteriyalar qoldiqlarni unumdor tuproqqa aylantiradi — va doira yopiladi.")}</div></div>
    </div>
  </div>
</section>'''
write("ecosystems.html", layout("ecosystems.html", "Экосистемы", "Ekotizimlar", body))

# =====================================================================
# 3. УГРОЗЫ
# =====================================================================
body = hero(("Что происходит", "Nima boʻlmoqda"),
  ("Угрозы природе", "Tabiatga tahdidlar"),
  ("Большинство экологических проблем созданы человеком — а значит, человек может их и решить.",
   "Ekologik muammolarning aksariyati inson tomonidan yaratilgan — demak, inson ularni hal qila oladi ham.")) + f'''
<section class="block">
  <div class="container">
    <div class="stats reveal">
      <div class="stat"><b>~10 {t("млн га", "mln ga")}</b>{t("лесов исчезает в мире ежегодно", "oʻrmon dunyoda har yili yoʻqoladi")}</div>
      <div class="stat"><b>{t("Млн тонн", "Mln tonna")}</b>{t("пластика попадает в океан каждый год", "plastik har yili okeanga tushadi")}</div>
      <div class="stat"><b>~90%</b>{t("площади Аральского моря утрачено", "Orol dengizi maydoni yoʻqolgan")}</div>
      <div class="stat"><b>~99%</b>{t("людей дышат воздухом хуже норм ВОЗ*", "odamlar JSST meʼyoridan yomon havodan nafas oladi*")}</div>
    </div>
  </div>
</section>
<section class="block alt">
  <div class="container">
    {head(("Главные проблемы", "Asosiy muammolar"))}
    <div class="grid">
      {card("tree", ("Вырубка лесов", "Oʻrmonlarni kesish"), ("Леса вырубают под поля, пастбища и строительство. Животные теряют дом, почва — защиту, а климат — естественный «фильтр».", "Oʻrmonlar dala, yaylov va qurilish uchun kesiladi. Hayvonlar uysiz qoladi, tuproq himoyasini, iqlim esa tabiiy «filtr»ni yoʻqotadi."))}
      {card("trash", ("Пластик и мусор", "Plastik va chiqindi"), ("Пластик разлагается сотни лет. Он распадается на микрочастицы, которые попадают в воду, рыбу и в итоге — в организм человека.", "Plastik yuzlab yillar davomida parchalanadi. U mikrozarralarga boʻlinib, suvga, baliqqa va oxir-oqibat inson organizmiga tushadi."), "gold")}
      {card("sun", ("Изменение климата", "Iqlim oʻzgarishi"), ("Сжигание угля, нефти и газа нагревает планету. Тают ледники, учащаются засухи, жара и наводнения.", "Koʻmir, neft va gaz yoqish sayyorani isitadi. Muzliklar eriydi, qurgʻoqchilik, jazirama va toshqinlar koʻpayadi."))}
      {card("drop", ("Нехватка воды", "Suv tanqisligi"), ("Неэффективный полив и потери воды осушают реки и озёра. Пример — трагедия Аральского моря.", "Samarasiz sugʻorish va suv isrofi daryo va koʻllarni quritadi. Misol — Orol dengizi fojiasi."))}
      {card("paw", ("Браконьерство", "Brakonerlik"), ("Незаконная охота ставит редкие виды на грань исчезновения. Каждый потерянный вид — невосполнимая утрата.", "Noqonuniy ov noyob turlarni yoʻqolib ketish yoqasiga olib keladi. Har bir yoʻqolgan tur — qaytarib boʻlmas yoʻqotish."), "gold")}
      {card("factory", ("Загрязнение воздуха", "Havo ifloslanishi"), ("Выхлопы машин, заводы и сжигание мусора наполняют воздух вредными частицами, опасными для лёгких и сердца.", "Mashina chiqindisi, zavodlar va chiqindi yoqish havoni oʻpka va yurak uchun xavfli zarrachalar bilan toʻldiradi."))}
    </div>
    {el("p", "* По оценкам ВОЗ, около 99% населения Земли дышит воздухом, который не соответствует её рекомендациям.", "* JSST hisob-kitoblariga koʻra, Yer aholisining qariyb 99% i uning tavsiyalariga mos kelmaydigan havodan nafas oladi.", 'style="margin-top:28px;color:var(--text-muted);font-size:.85rem"')}
  </div>
</section>
<section class="block">
  <div class="container">
    <div class="banner reveal">
      {el("h2", "Хорошая новость", "Yaxshi xabar")}
      {el("p", "Природа умеет восстанавливаться, если дать ей шанс. Озоновый слой восстанавливается после запрета вредных веществ, а многие виды вернулись благодаря заповедникам.", "Agar imkon berilsa, tabiat tiklana oladi. Zararli moddalar taqiqlanganidan keyin ozon qatlami tiklanmoqda, koʻplab turlar esa qoʻriqxonalar tufayli qaytdi.")}
      <div class="btns" style="justify-content:center"><a href="protect.html" class="btn btn-primary">{t("Что можно сделать →", "Nima qilish mumkin →")}</a></div>
    </div>
  </div>
</section>'''
write("threats.html", layout("threats.html", "Угрозы", "Tahdidlar", body))

# =====================================================================
# 4. КАК СОХРАНИТЬ
# =====================================================================
body = hero(("Решения", "Yechimlar"),
  ("Как сохранить природу", "Tabiatni qanday asraymiz"),
  ("Защита природы — это работа на трёх уровнях: государство, сообщество и каждый человек.",
   "Tabiatni muhofaza qilish uch darajadagi ish: davlat, jamiyat va har bir inson.")) + f'''
<section class="block">
  <div class="container">
    <div class="grid">
      {card("landmark", ("Государство", "Davlat"), ("Создание заповедников и национальных парков, законы против загрязнения, переход на солнечную и ветровую энергию, экономное использование воды в сельском хозяйстве.", "Qoʻriqxona va milliy bogʻlar tashkil etish, ifloslanishga qarshi qonunlar, quyosh va shamol energiyasiga oʻtish, qishloq xoʻjaligida suvni tejash."))}
      {card("users", ("Сообщество", "Jamiyat"), ("Субботники и посадка деревьев, раздельный сбор мусора во дворах, школьные эко-клубы, общие сады и парки.", "Shanbaliklar va daraxt ekish, hovlilarda chiqindini saralab yigʻish, maktab eko-klublari, umumiy bogʻ va parklar."), "gold")}
      {card("user", ("Каждый из нас", "Har birimiz"), ("Экономить воду и свет, отказаться от лишнего пластика, ходить пешком или ездить на транспорте, не мусорить на природе.", "Suv va elektrni tejash, ortiqcha plastikdan voz kechish, piyoda yurish yoki jamoat transportidan foydalanish, tabiatda chiqindi tashlamaslik."))}
    </div>
  </div>
</section>
<section class="block alt">
  <div class="container grid-2">
    <div class="reveal">
      {el("h2", "Правило трёх «R»", "Uch «R» qoidasi")}
      {el("p", "Простая формула, которая помогает сократить количество мусора в разы.", "Chiqindi miqdorini bir necha baravar kamaytirishga yordam beradigan oddiy formula.")}
      <div class="steps" style="margin-top:24px">
        <div class="step"><div>{el("h3", "Reduce — сокращай", "Reduce — kamaytir")}{el("p", "Не покупай лишнего. Многоразовая сумка и бутылка вместо одноразовых.", "Ortiqcha narsa sotib olma. Bir martalik oʻrniga koʻp martalik sumka va shisha.")}</div></div>
        <div class="step"><div>{el("h3", "Reuse — используй повторно", "Reuse — qayta foydalan")}{el("p", "Банки, коробки и одежда могут прожить вторую жизнь. Чини, а не выбрасывай.", "Bankalar, qutilar va kiyimlar ikkinchi hayot kechirishi mumkin. Tashlama, tuzat.")}</div></div>
        <div class="step"><div>{el("h3", "Recycle — перерабатывай", "Recycle — qayta ishlat")}{el("p", "Сортируй бумагу, пластик, стекло и металл и сдавай их в пункты приёма.", "Qogʻoz, plastik, shisha va metallni saralab, qabul punktlariga topshir.")}</div></div>
      </div>
    </div>
    <div class="panel reveal">{icon("recycle")}</div>
  </div>
</section>
<section class="block">
  <div class="container">
    {head(("Дома, в дороге и на природе", "Uyda, yoʻlda va tabiatda"))}
    <div class="grid">
      {card("drop", ("Вода", "Suv"), ("Закрывайте кран, пока чистите зубы. Чините протечки — капающий кран теряет тысячи литров в год.", "Tish yuvayotganda jumrakni yoping. Oqayotgan jumrakni tuzating — u yiliga minglab litr suvni isrof qiladi."))}
      {card("bulb", ("Энергия", "Energiya"), ("Светодиодные лампы, выключенные приборы и свет в пустой комнате — простая экономия.", "Yorugʻlik diodli lampalar, oʻchirilgan asboblar va boʻsh xonada oʻchirilgan chiroq — oddiy tejamkorlik."), "gold")}
      {card("bike", ("Транспорт", "Transport"), ("Короткие расстояния — пешком или на велосипеде, длинные — на метро и автобусе.", "Qisqa masofalar — piyoda yoki velosipedda, uzoq masofalar — metro va avtobusda."))}
      {card("sprout", ("Посадите дерево", "Daraxt eking"), ("Одно взрослое дерево даёт тень, очищает воздух и становится домом для птиц и насекомых.", "Bitta katta daraxt soya beradi, havoni tozalaydi va qush va hasharotlarga uy boʻladi."), "gold")}
    </div>
  </div>
</section>'''
write("protect.html", layout("protect.html", "Как сохранить", "Qanday asraymiz", body))

# =====================================================================
# 5. ПРИРОДА УЗБЕКИСТАНА
# =====================================================================
body = hero(("Наша страна", "Bizning yurt"),
  ("Природа Узбекистана", "Oʻzbekiston tabiati"),
  ("От снежных вершин Чаткала до песков Кызылкума — Узбекистан богат уникальной природой, которую важно сберечь.",
   "Chotqolning qorli choʻqqilaridan Qizilqum qumlarigacha — Oʻzbekiston noyob tabiatga boy va uni asrash muhim.")) + f'''
<section class="block">
  <div class="container grid-2">
    <div class="reveal">
      {el("h2", "Аральское море", "Orol dengizi")}
      {el("p", "Одна из крупнейших экологических катастроф XX века. Воду рек Амударьи и Сырдарьи стали массово забирать на орошение хлопковых полей, и море начало высыхать.", "XX asrning eng yirik ekologik falokatlaridan biri. Amudaryo va Sirdaryo suvlari paxta dalalarini sugʻorish uchun ommaviy olina boshlandi va dengiz qurib bordi.")}
      {el("p", "На месте дна появилась новая пустыня — Аралкум. Ветер разносит с неё соль и пыль на сотни километров.", "Dengiz tubi oʻrnida yangi choʻl — Orolqum paydo boʻldi. Shamol undan tuz va changni yuzlab kilometrlarga tarqatadi.")}
    </div>
    <div class="timeline reveal">
      <div class="tl-item"><b>1960</b>{el("p", "Арал — одно из крупнейших озёр мира, с рыболовством и портами.", "Orol — dunyodagi eng yirik koʻllardan biri, baliqchilik va portlar bilan.")}</div>
      <div class="tl-item"><b>1980–1990</b>{el("p", "Уровень воды быстро падает, рыболовство исчезает, порты остаются в пустыне.", "Suv sathi tez pasayadi, baliqchilik yoʻqoladi, portlar choʻlda qoladi.")}</div>
      <div class="tl-item"><b>2000-е / 2000-yillar</b>{el("p", "Море распадается на несколько отдельных водоёмов.", "Dengiz bir nechta alohida suv havzalariga boʻlinadi.")}</div>
      <div class="tl-item"><b>{t("Сегодня", "Bugun")}</b>{el("p", "На высохшем дне высаживают саксаул и другие растения, чтобы остановить пыльные бури.", "Qurigan tubida chang boʻronlarini toʻxtatish uchun saksovul va boshqa oʻsimliklar ekilmoqda.")}</div>
    </div>
  </div>
</section>
<section class="block alt">
  <div class="container">
    {head(("Охраняемые территории", "Muhofaza etiladigan hududlar"), ("Здесь природа находится под защитой закона.", "Bu yerda tabiat qonun himoyasida."))}
    <div class="grid">
      {card("mountain", ("Чаткальский заповедник", "Chotqol qoʻriqxonasi"), ("Горный биосферный заповедник в Ташкентской области: арчовые леса, дикие яблони, горные козлы.", "Toshkent viloyatidagi togʻ biosfera qoʻriqxonasi: archazorlar, yovvoyi olmalar, togʻ echkilari."))}
      {card("tree", ("Угам-Чаткальский нацпарк", "Ugom-Chotqol milliy bogʻi"), ("Один из крупнейших национальных парков страны с горными реками, ущельями и альпийскими лугами.", "Togʻ daryolari, daralar va alp oʻtloqlari bilan mamlakatning eng yirik milliy bogʻlaridan biri."), "gold")}
      {card("leaf", ("Зааминский нацпарк", "Zomin milliy bogʻi"), ("Горы Туркестанского хребта, древние арчовые леса и чистый горный воздух.", "Turkiston tizmasi togʻlari, qadimiy archazorlar va toza togʻ havosi."))}
      {card("sun", ("Кызылкумский заповедник", "Qizilqum qoʻriqxonasi"), ("Тугайные леса вдоль Амударьи — дом для бухарского оленя и фазанов.", "Amudaryo boʻyidagi toʻqay oʻrmonlari — Buxoro bugʻusi va qirgʻovullar uchun uy."), "gold")}
    </div>
  </div>
</section>
<section class="block">
  <div class="container">
    {head(("Редкие животные", "Noyob hayvonlar"), ("Эти виды занесены в Красную книгу Узбекистана.", "Bu turlar Oʻzbekiston Qizil kitobiga kiritilgan."))}
    <div class="grid">
      {card("paw", ("Снежный барс", "Qor qoploni"), ("Скрытный хищник высокогорий. В Узбекистане встречается в Чаткальских и Гиссарских горах.", "Baland togʻlarning yashirin yirtqichi. Oʻzbekistonda Chotqol va Hisor togʻlarida uchraydi."))}
      {card("paw", ("Бухарский олень", "Buxoro bugʻusi"), ("Житель тугайных лесов. Когда-то был на грани исчезновения, его численность восстанавливают в заповедниках.", "Toʻqay oʻrmonlari aholisi. Bir paytlar yoʻqolib ketish arafasida edi, uning soni qoʻriqxonalarda tiklanmoqda."), "gold")}
      {card("paw", ("Джейран", "Jayron"), ("Изящная антилопа пустынь. Для её спасения в Бухарской области создан питомник «Джейран».", "Choʻllarning nafis kiyigi. Uni saqlab qolish uchun Buxoro viloyatida «Jayron» pitomnigi tashkil etilgan."))}
      {card("paw", ("Сурок Мензбира", "Menzbir sugʻuri"), ("Маленький эндемик Западного Тянь-Шаня — живёт только в этом горном регионе.", "Gʻarbiy Tyan-Shanning kichik endemigi — faqat shu togʻ mintaqasida yashaydi."), "gold")}
    </div>
  </div>
</section>
<section class="block alt">
  <div class="container">
    <div class="banner reveal">
      {el("h2", "«Яшил макон» — Зелёное пространство", "«Yashil makon» — Yashil hudud")}
      {el("p", "С 2021 года в Узбекистане проходит общенациональный проект по массовой посадке деревьев в городах и районах. Присоединиться может каждый — во время весенних и осенних акций.", "2021-yildan beri Oʻzbekistonda shahar va tumanlarda ommaviy daraxt ekish boʻyicha umummilliy loyiha amalga oshirilmoqda. Bahorgi va kuzgi aksiyalarda har kim qatnasha oladi.")}
    </div>
  </div>
</section>'''
write("uzbekistan.html", layout("uzbekistan.html", "Природа Узбекистана", "Oʻzbekiston tabiati", body))

# =====================================================================
# 6. ЭКО-ПРИВЫЧКИ (интерактивный чек-лист)
# =====================================================================
habits = [
  ("Ношу с собой многоразовую бутылку для воды", "Oʻzim bilan koʻp martalik suv idishini olib yuraman"),
  ("Хожу в магазин со своей сумкой", "Doʻkonga oʻz sumkam bilan boraman"),
  ("Выключаю свет, когда выхожу из комнаты", "Xonadan chiqayotganda chiroqni oʻchiraman"),
  ("Закрываю кран, пока чищу зубы", "Tish yuvayotganda jumrakni yopaman"),
  ("Принимаю душ вместо ванны", "Vanna oʻrniga dush qabul qilaman"),
  ("Сортирую мусор: бумага, пластик, стекло", "Chiqindini saralayman: qogʻoz, plastik, shisha"),
  ("Сдаю батарейки в специальные пункты", "Batareyalarni maxsus punktlarga topshiraman"),
  ("Короткие поездки делаю пешком или на велосипеде", "Qisqa masofalarni piyoda yoki velosipedda bosib oʻtaman"),
  ("Отказываюсь от одноразовых трубочек и посуды", "Bir martalik naycha va idishlardan voz kechaman"),
  ("Печатаю только то, что действительно нужно", "Faqat haqiqatan kerakli narsalarni chop etaman"),
  ("Убираю за собой мусор на природе", "Tabiatda oʻzimdan keyin chiqindini yigʻishtiraman"),
  ("Посадил(а) хотя бы одно дерево", "Kamida bitta daraxt ekdim"),
]
checks = "".join(
  f'<label class="check reveal"><input type="checkbox" id="h{i}"><span class="box"><svg viewBox="0 0 24 24">{IC["check"]}</svg></span><span class="txt">{t(r, u)}</span></label>'
  for i, (r, u) in enumerate(habits))

body = hero(("Начни с себя", "Oʻzingdan boshla"),
  ("Эко-привычки", "Eko-odatlar"),
  ("Отметьте привычки, которые у вас уже есть. Прогресс сохранится в браузере — возвращайтесь и добавляйте новые.",
   "Sizda allaqachon bor odatlarni belgilang. Natija brauzerda saqlanadi — qaytib kelib yangilarini qoʻshing.")) + f'''
<section class="block">
  <div class="container">
    <div class="section-head">
      {el("h2", "Мой эко-чек-лист", "Mening eko-roʻyxatim")}
      <div class="progress-wrap"><div class="progress-bar"></div></div>
      <span class="progress-label">{t("Выполнено:", "Bajarildi:")} <span class="progress-num">0 / {len(habits)}</span></span>
    </div>
    <div class="checklist">{checks}</div>
  </div>
</section>
<section class="block alt">
  <div class="container">
    {head(("Неделя эко-челленджа", "Eko-chellenj haftasi"), ("Попробуйте каждый день добавлять одно новое действие.", "Har kuni bitta yangi harakat qoʻshib koʻring."))}
    <div class="grid">
      {card("trash", ("Пн–Вт", "Du–Se"), ("Посчитайте, сколько пластика вы выбрасываете за день, и откажитесь от одной вещи.", "Kuniga qancha plastik tashlashingizni sanang va bittasidan voz keching."))}
      {card("drop", ("Ср–Чт", "Chor–Pay"), ("Сократите время в душе на 2 минуты и проверьте краны на протечки.", "Dushdagi vaqtni 2 daqiqaga qisqartiring va jumraklarni tekshiring."), "gold")}
      {card("bike", ("Пт–Сб", "Ju–Sha"), ("Все короткие поездки — пешком. Заодно это полезно для здоровья.", "Barcha qisqa yoʻllar — piyoda. Bu sogʻliq uchun ham foydali."))}
      {card("sprout", ("Вс", "Yak"), ("Выйдите в парк или за город и соберите мусор вместе с друзьями.", "Parkka yoki shahar tashqarisiga chiqib, doʻstlar bilan chiqindi yigʻing."), "gold")}
    </div>
  </div>
</section>'''
write("habits.html", layout("habits.html", "Эко-привычки", "Eko-odatlar", body))

# =====================================================================
# 7. О ПРОЕКТЕ + ТЕСТ
# =====================================================================
quiz_js = '''<script>
window.QUIZ = [
 {q:{ru:"Какая экосистема хранит больше всего углерода на единицу площади?",uz:"Qaysi ekotizim maydon birligiga eng koʻp uglerod saqlaydi?"},
  a:[{ru:"Пустыня",uz:"Choʻl"},{ru:"Торфяное болото",uz:"Torfli botqoq"},{ru:"Степь",uz:"Dasht"}],c:1},
 {q:{ru:"Из-за чего в основном высохло Аральское море?",uz:"Orol dengizi asosan nima sababdan qurib qoldi?"},
  a:[{ru:"Из-за землетрясения",uz:"Zilzila tufayli"},{ru:"Из-за забора воды рек на орошение",uz:"Daryo suvining sugʻorishga olinishi tufayli"},{ru:"Из-за таяния ледников",uz:"Muzliklar erishi tufayli"}],c:1},
 {q:{ru:"Что означает первая «R» в правиле трёх «R»?",uz:"Uch «R» qoidasidagi birinchi «R» nimani anglatadi?"},
  a:[{ru:"Reduce — сокращай",uz:"Reduce — kamaytir"},{ru:"Run — беги",uz:"Run — yugur"},{ru:"Repair — чини",uz:"Repair — tuzat"}],c:0},
 {q:{ru:"Какое животное живёт в горах Узбекистана и занесено в Красную книгу?",uz:"Qaysi hayvon Oʻzbekiston togʻlarida yashaydi va Qizil kitobga kiritilgan?"},
  a:[{ru:"Белый медведь",uz:"Oq ayiq"},{ru:"Кенгуру",uz:"Kenguru"},{ru:"Снежный барс",uz:"Qor qoploni"}],c:2},
 {q:{ru:"Какое растение сажают на высохшем дне Арала против пыльных бурь?",uz:"Chang boʻronlariga qarshi Orolning qurigan tubiga qaysi oʻsimlik ekilmoqda?"},
  a:[{ru:"Саксаул",uz:"Saksovul"},{ru:"Пальма",uz:"Palma"},{ru:"Рис",uz:"Sholi"}],c:0},
];
</script>'''

body = hero(("О нас", "Biz haqimizda"),
  ("О проекте", "Loyiha haqida"),
  ("«Зелёный мир» — образовательный сайт о природе, её проблемах и о том, как каждый может помочь.",
   "«Yashil dunyo» — tabiat, uning muammolari va har kim qanday yordam bera olishi haqidagi taʼlimiy sayt.")) + f'''
<section class="block">
  <div class="container grid-2">
    <div class="reveal">
      {el("h2", "Наша цель", "Bizning maqsadimiz")}
      {el("p", "Мы хотим, чтобы как можно больше людей узнали, почему природа важна и что ей угрожает, — и начали действовать.", "Imkon qadar koʻproq odam tabiat nima uchun muhimligini va unga nima tahdid solayotganini bilib, harakat qilishni boshlashini istaymiz.")}
      {el("p", "Сайт работает на двух языках — русском и узбекском, чтобы быть понятным всем жителям Узбекистана.", "Sayt ikki tilda — rus va oʻzbek tillarida ishlaydi, shunda Oʻzbekistonning barcha aholisi uchun tushunarli boʻladi.")}
      {el("p", "Цвета сайта взяты из настоящего мшистого леса — оттенки болота, мха и старой коры.", "Sayt ranglari haqiqiy moxli oʻrmondan olingan — botqoq, mox va eski poʻstloq tuslari.")}
    </div>
    <div class="panel reveal">{icon("leaf")}</div>
  </div>
</section>
<section class="block alt">
  <div class="container">
    {head(("Проверьте себя", "Oʻzingizni sinang"), ("5 вопросов по материалам сайта.", "Sayt materiallari boʻyicha 5 ta savol."))}
    <div class="quiz reveal" id="quiz"></div>
  </div>
</section>
<section class="block">
  <div class="container">
    {head(("Полезные источники", "Foydali manbalar"))}
    <ul class="sources reveal">
      <li><a href="https://www.unep.org/" target="_blank" rel="noopener">UNEP — {t("Программа ООН по окружающей среде", "BMT Atrof-muhit dasturi")}</a></li>
      <li><a href="https://www.iucnredlist.org/" target="_blank" rel="noopener">IUCN Red List — {t("Красный список МСОП", "XTMI Qizil roʻyxati")}</a></li>
      <li><a href="https://www.fao.org/forest-resources-assessment/" target="_blank" rel="noopener">FAO — {t("Оценка лесных ресурсов мира", "Jahon oʻrmon resurslarini baholash")}</a></li>
      <li><a href="https://www.who.int/health-topics/air-pollution" target="_blank" rel="noopener">{t("ВОЗ — загрязнение воздуха", "JSST — havo ifloslanishi")}</a></li>
      <li><a href="https://www.ramsar.org/" target="_blank" rel="noopener">{t("Рамсарская конвенция о водно-болотных угодьях", "Suv-botqoq yerlari toʻgʻrisidagi Ramsar konvensiyasi")}</a></li>
    </ul>
  </div>
</section>'''
write("about.html", layout("about.html", "О проекте", "Loyiha haqida", body, quiz_js))

print("OK:", [p[0] for p in PAGES])
