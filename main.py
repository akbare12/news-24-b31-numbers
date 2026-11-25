# news-image-20261124, angle NUMBERS: 38 stories, hero trio Riyadh / Shanghai / Huawei.
# Deterministic PIL-only front page, 1024x1024, output via MAKEFUN_OUTPUT_DIR.
import os
from PIL import Image, ImageDraw, ImageFont
OUT=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png'); W,H=1024,1024; RED=(178,34,34); NAVY=(16,32,64); CREAM=(250,246,235); INK=(18,18,18); GREY=(90,90,90); GOLD=(184,134,11); GREEN=(27,94,32); BLUE=(21,71,139); ORANGE=(176,84,0)
def F(s,b=False,ser=False):
    p='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf' if ser else ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if b else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
def wrap(t,f,mw,d):
    ws=[]
    for w in t.split():
        if not ws or d.textlength(ws[-1]+' '+w,font=f)>mw: ws.append(w)
        else: ws[-1]+=' '+w
    return ws
def txt(d,x,y,s,f,fill=INK):
    d.text((x,y),s,font=f,fill=fill); return y+f.size+2
def para(d,x,y,s,f,mw,fill=INK,lh=None):
    for ln in wrap(s,f,mw,d): y=txt(d,x,y,ln,f,fill)
    return y
def chip(d,x,y,s):
    c={'CONFIRMED':GREEN,'OFFICIAL':BLUE,'REPORTED':(70,70,70),'CLAIM':ORANGE}.get(s,(70,70,70)); f=F(7,True); w=d.textlength(s,font=f)+8; d.rounded_rectangle([x,y,x+w,y+12],2,fill=c); d.text((x+4,y+1),s,font=f,fill=(255,255,255)); return x+w+4
img=Image.new('RGB',(W,H),CREAM); d=ImageDraw.Draw(img)
d.rectangle([0,0,W,10],fill=RED); d.rectangle([0,H-8,W,H],fill=RED)
d.text((14,16),'THE WORLD ON ONE DAY',font=F(11,True),fill=RED); d.text((W-14,16),'38 STORIES \u00b7 6 REGIONS \u00b7 13 FIELDS',font=F(11,True),fill=RED,anchor='ra')
d.text((14,32),'Tuesday 24 November 2026',font=F(30,True,True),fill=INK)
para(d,14,66,'Riyadh tower hit again \u00b7 Shanghai party chief probed \u00b7 Huawei guilty on 10 of 12 counts.',F(12,False,True),990,RED)
# Region bar: Europe 9, Middle East 8, Asia 8, Africa 2, Americas 7, World/Space 4 = 38 stories.
RB=[('EUROPE 9',(31,58,138)),('MIDDLE EAST 8',RED),('ASIA 8',(0,110,70)),('AFRICA 2',GOLD),('AMERICAS 7',(90,40,110)),('WORLD / SPACE 4',NAVY)]; x=14
for nm,c in RB:
    w=164 if nm.startswith('WORLD') else 158; d.rectangle([x,86,x+w,106],fill=c); d.text((x+w/2,91),nm,font=F(10,True),fill=(255,255,255),anchor='ma'); x+=w+4
d.text((14,112),'THE DAY IN UTC',font=F(9,True),fill=RED)
UTC=[('02:15','NATO vows space defence'),('08:16','Hanoi hot-pot blast'),('10:42','Saudi strikes Yemen'),('14:27','Riyadh tower hit'),('16:51','Houthis 60 km from Aden'),('18:58','Hormuz ship attack'),('20:41','Huawei guilty')]
x=14
for t,e in UTC:
    d.text((x,124),t,font=F(9,True),fill=NAVY); d.text((x,135),e,font=F(8),fill=INK); x+=143
d.text((14,152),'THE DAY IN NUMBERS',font=F(9,True),fill=RED)
NUM=[('11','hurt in Riyadh'),('9','killed in Ukraine'),('50,018','Dow, first over 50k'),('+8.99%','Taiex record'),('25','killed in Yemen'),('26','Cikande fire toll'),('10/12','Huawei guilty'),('96','drones at Ukraine')]
x=14
for n,l in NUM:
    d.text((x,164),n,font=F(16,True,True),fill=RED); d.text((x,182),l,font=F(8),fill=INK); x+=127
def scene(x,y,w,h,k):
    d.rectangle([x,y,x+w,y+h],fill=(210,225,235)); d.rectangle([x,y+h-18,x+w,y+h],fill=(120,140,110))
    if h<50:
        d.rectangle([x,y,x+w,y+h],fill=(210,225,235))
        if k=='drone': d.ellipse([x+w*0.35,y+6,x+w*0.65,y+20],fill=(40,40,40)); d.rectangle([x+w*0.2,y+12,x+w*0.8,y+15],fill=(40,40,40))
        elif k=='trophy': d.ellipse([x+w/2-10,y+4,x+w/2+10,y+24],fill=GOLD); d.rectangle([x+w/2-3,y+24,x+w/2+3,y+32],fill=GOLD)
        elif k=='ship': d.rectangle([x+8,y+20,x+w-8,y+30],fill=(120,40,40)); d.rectangle([x+w*0.4,y+8,x+w*0.6,y+20],fill=(255,255,255))
        elif k=='chart': d.line([(x+8,y+28),(x+w*0.3,y+18),(x+w*0.55,y+22),(x+w-8,y+6)],fill=GREEN,width=3)
        elif k=='data': d.rectangle([x+10,y+8,x+w-10,y+28],fill=(30,30,50)); d.rectangle([x+w*0.3,y+12,x+w*0.42,y+24],fill=(255,60,60)); d.rectangle([x+w*0.58,y+12,x+w*0.7,y+24],fill=(255,60,60))
        elif k=='heli': d.ellipse([x+w*0.25,y+10,x+w*0.75,y+24],fill=(60,90,60)); d.rectangle([x+w*0.1,y+16,x+w*0.9,y+19],fill=(40,40,40))
        elif k=='market': d.rectangle([x+8,y+18,x+w-8,y+32],fill=(200,180,140)); d.rectangle([x+w*0.3,y+6,x+w*0.7,y+18],fill=(180,40,40))
        elif k=='desert': d.polygon([(x,y+32),(x+w*0.4,y+12),(x+w*0.7,y+32)],fill=(200,170,110)); d.ellipse([x+w*0.75,y+4,x+w*0.88,y+17],fill=(255,200,0))
        elif k=='strike': d.polygon([(x+w*0.2,y+32),(x+w*0.5,y+6),(x+w*0.8,y+32)],fill=(90,90,90)); d.ellipse([x+w*0.6,y+8,x+w*0.72,y+20],fill=(255,120,0))
        elif k=='rocket': d.rectangle([x+w*0.44,y+4,x+w*0.5,y+28],fill=(200,200,200)); d.polygon([(x+w*0.38,y+4),(x+w*0.5,y-2),(x+w*0.56,y+4)],fill=RED)
        else: d.rectangle([x+w*0.3,y+8,x+w*0.7,y+28],fill=NAVY)
        return
    if k=='tower': d.rectangle([x+w*0.42,y+8,x+w*0.58,y+h-18],fill=NAVY); d.polygon([(x+w*0.42,y+8),(x+w*0.5,y-2),(x+w*0.58,y+8)],fill=NAVY); d.ellipse([x+w*0.62,y+14,x+w*0.72,y+24],fill=(255,120,0)); d.ellipse([x+w*0.66,y+10,x+w*0.76,y+20],fill=(255,180,0))
    elif k=='gate': d.rectangle([x+8,y+h-52,x+w-8,y+h-18],fill=(150,40,40)); d.rectangle([x+w*0.44,y+h-72,x+w*0.56,y+h-18],fill=(120,30,30)); d.rectangle([x+w*0.2,y+h-40,x+w*0.8,y+h-30],fill=GOLD)
    elif k=='court': d.rectangle([x+10,y+22,x+w-10,y+h-18],fill=(220,210,190)); d.polygon([(x+10,y+22),(x+w/2,y+6),(x+w-10,y+22)],fill=(140,30,30)); d.rectangle([x+w*0.46,y+34,x+w*0.54,y+h-18],fill=(255,255,255))
    elif k=='drone': d.ellipse([x+w*0.3,y+12,x+w*0.7,y+34],fill=(40,40,40)); d.rectangle([x+w*0.2,y+20,x+w*0.8,y+24],fill=(40,40,40)); d.rectangle([x+w*0.42,y+36,x+w*0.58,y+h-18],fill=(90,90,90))
    elif k=='trophy': d.ellipse([x+w/2-14,y+8,x+w/2+14,y+44],fill=GOLD); d.rectangle([x+w/2-4,y+44,x+w/2+4,y+h-18],fill=GOLD); d.rectangle([x+w/2-18,y+h-26,x+w/2+18,y+h-18],fill=GOLD)
    elif k=='ship': d.rectangle([x+8,y+h-40,x+w-8,y+h-22],fill=(120,40,40)); d.rectangle([x+w*0.4,y+h-62,x+w*0.6,y+h-40],fill=(255,255,255)); d.ellipse([x+w*0.7,y+10,x+w*0.82,y+26],fill=(255,120,0))
    elif k=='chart': d.line([(x+8,y+h-24),(x+w*0.3,y+h-44),(x+w*0.55,y+h-30),(x+w-8,y+12)],fill=GREEN,width=4); d.line([(x+8,y+22),(x+w-8,y+22)],fill=RED,width=2)
    elif k=='data': d.rectangle([x+10,y+14,x+w-10,y+h-18],fill=(30,30,50)); d.rectangle([x+w*0.3,y+22,x+w*0.42,y+h-26],fill=(255,60,60)); d.rectangle([x+w*0.46,y+22,x+w*0.58,y+h-26],fill=(255,60,60)); d.rectangle([x+w*0.62,y+22,x+w*0.74,y+h-26],fill=(255,60,60))
    elif k=='heli': d.ellipse([x+w*0.25,y+20,x+w*0.75,y+44],fill=(60,90,60)); d.rectangle([x+w*0.1,y+28,x+w*0.9,y+32],fill=(40,40,40)); d.rectangle([x+w*0.75,y+30,x+w-6,y+38],fill=(60,90,60))
    elif k=='market': d.rectangle([x+8,y+30,x+w-8,y+h-18],fill=(200,180,140)); d.rectangle([x+w*0.3,y+14,x+w*0.7,y+32],fill=(180,40,40)); d.rectangle([x+w*0.42,y+32,x+w*0.58,y+h-18],fill=(120,80,40))
    elif k=='desert': d.polygon([(x,y+h-18),(x+w*0.4,y+h-52),(x+w*0.7,y+h-18)],fill=(200,170,110)); d.polygon([(x+w*0.5,y+h-18),(x+w*0.85,y+h-62),(x+w,y+h-18)],fill=(180,150,90)); d.ellipse([x+w*0.75,y+8,x+w*0.88,y+21],fill=(255,200,0))
    elif k=='strike': d.polygon([(x+w*0.2,y+h-18),(x+w*0.5,y+10),(x+w*0.8,y+h-18)],fill=(90,90,90)); d.ellipse([x+w*0.6,y+14,x+w*0.72,y+26],fill=(255,120,0)); d.ellipse([x+w*0.64,y+10,x+w*0.76,y+22],fill=(255,180,0))
    else: d.rectangle([x+w*0.44,y+8,x+w*0.5,y+h-30],fill=(200,200,200)); d.polygon([(x+w*0.38,y+8),(x+w*0.5,y-2),(x+w*0.56,y+8)],fill=RED); d.ellipse([x+w*0.62,y+16,x+w*0.78,y+32],fill=(120,160,220))
HERO=[('1 \u00b7 RIYADH \u00b7 MIDDLE EAST','CONFIRMED','Houthi drone hits Riyadh\u2019s tallest tower again, 11 hurt','A Houthi drone struck the PIF tower, Riyadh\u2019s tallest, for the second time in a week. Eleven people were hurt: 2 Saudis, 2 Indians, 3 Nepalis and 4 Egyptians. (Saudi officials)','tower'),('2 \u00b7 SHANGHAI \u00b7 ASIA','OFFICIAL','China probes Shanghai party chief Chen Jining','Chen Jining, 62, the Shanghai party chief, is under investigation for serious violations. He is the fourth Politburo member to fall in a probe this year. (CCDI)','gate'),('3 \u00b7 NEW YORK \u00b7 US / TECH','CONFIRMED','Huawei guilty on 10 of 12 counts','A US federal jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. It was cleared of racketeering, with sentencing in Sep 2027. (US court)','court')]
CARDS=[('4 \u00b7 ZAPORIZHZHIA \u00b7 EUROPE / WAR','REPORTED','Russian attacks kill 9 across Ukraine in a day','Nine were killed and 81 wounded as Russia launched 96 drones; 73 were downed. (Ukrainian officials)','drone'),('5 \u00b7 SENEGAL \u00b7 AFRICA / SPORT','OFFICIAL','CAS hands Senegal back the AFCON title','CAS restored Senegal as champions after Morocco forfeited 3-0, making it 1-0. (CAS)','trophy'),('6 \u00b7 HORMUZ \u00b7 MIDDLE EAST','REPORTED','IRGC attacks container ship in Hormuz','An IRGC attack hit a container ship at 18:58 UTC, disabling navigation near Khasab. (UKMTO)','ship'),('7 \u00b7 NEW YORK \u00b7 WORLD / MARKETS','CONFIRMED','Dow closes above 50,000 for the first time','The Dow closed at 50,018, first above 50,000; the Taiex jumped 8.99% to 40,122. (Markets)','chart'),('8 \u00b7 REDMOND \u00b7 WORLD / TECH','REPORTED',"Microsoft declares \u2018Code Red\u2019 after historic outage",'After a 24-hour outage, Microsoft declared Code Red, targeting one-hour recovery. (Reuters)','data'),('9 \u00b7 ESKISEHIR \u00b7 EUROPE','REPORTED','Turkish military helicopter crash kills 5','A Turkish military AS-532 helicopter crashed in Eskisehir, killing five on board. (Officials)','heli'),('10 \u00b7 CARTAGENA \u00b7 AMERICAS','REPORTED','Supermarket hostages: 25 held in Cartagena','Twenty-five were held in a Cartagena supermarket; five elderly women were freed. (Officials)','market'),('11 \u00b7 ADEN \u00b7 MIDDLE EAST','REPORTED','Houthis advance within 60 km of Aden','Houthi forces advanced to within 60 km of Aden in Yemen, pressing toward the port. (Wires)','desert'),('12 \u00b7 LAHJ \u00b7 MIDDLE EAST','REPORTED','Saudi strikes kill 25, wound 6 in Yemen','Saudi strikes in Wadi Maabaq, Lahj, killed or left missing 25 and wounded six. (Officials)','strike'),('13 \u00b7 JIUQUAN \u00b7 WORLD / SPACE','OFFICIAL','China names first foreign astronaut for Tiangong','China named the Shenzhou-24 crew, including Pakistan\u2019s Muhammad Zeeshan Ali. (CMSA)','rocket')]
x=14
for kick,ch,hl,dk,k in HERO:
    w=322; d.rectangle([x,200,x+w,382],outline=(180,170,150),width=1,fill=(255,255,255)); scene(x+4,204,w-8,88,k); d.text((x+6,296),kick,font=F(8,True),fill=RED); chip(d,x+6,308,ch); yy=para(d,x+6,324,hl,F(12,True,True),w-12); para(d,x+6,yy,dk,F(9),w-12); x+=w+9
for r in range(2):
    x=14; y=390+r*118
    for c in range(5):
        kick,ch,hl,dk,k=CARDS[r*5+c]; w=194; d.rectangle([x,y,x+w,y+112],outline=(180,170,150),width=1,fill=(255,255,255)); scene(x+3,y+3,w-6,36,k); d.text((x+5,y+42),kick,font=F(7,True),fill=RED); chip(d,x+5,y+54,ch); yy=para(d,x+5,y+68,hl,F(9,True,True),w-10); para(d,x+5,yy,dk,F(8),w-10); x+=w+4
# World map from real lat/lon, equirectangular, tall: lon -180..180, lat 78..-58, area 14,632 to 614,812.
MX,MY,MW,MH=14,632,600,180
def proj(lon,lat): return (MX+(lon+180)/360*MW, MY+(78-lat)/136*MH)
NA=[(-168,66),(-140,70),(-125,72),(-110,73),(-95,80),(-85,70),(-75,62),(-65,60),(-55,52),(-60,45),(-70,42),(-75,35),(-80,25),(-85,20),(-90,15),(-95,18),(-105,22),(-115,28),(-125,40),(-125,49),(-140,60),(-155,58),(-168,66)]; SA=[(-80,10),(-75,5),(-70,0),(-60,-5),(-50,-5),(-40,-10),(-35,-15),(-40,-25),(-50,-30),(-60,-35),(-70,-40),(-70,-50),(-75,-55),(-75,-40),(-80,-20),(-80,-10)]; AF=[(-17,15),(-10,30),(0,35),(10,37),(20,32),(30,31),(35,28),(40,15),(50,10),(45,0),(40,-10),(35,-20),(30,-30),(20,-35),(15,-25),(12,-15),(10,0),(0,5),(-8,5),(-17,15)]; EU=[(-10,36),(-10,43),(0,44),(5,43),(10,45),(15,40),(20,40),(25,36),(30,36),(35,36),(40,38),(45,40),(50,45),(60,50),(70,55),(80,60),(90,65),(100,70),(120,72),(140,72),(160,70),(170,66),(160,60),(150,55),(140,50),(130,45),(120,40),(110,35),(100,30),(95,25),(90,20),(85,15),(80,10),(75,8),(70,15),(65,20),(60,25),(55,25),(50,28),(45,30),(40,35),(35,36),(30,36),(20,36),(10,36)]; AU=[(113,-22),(120,-15),(130,-12),(140,-15),(150,-20),(153,-27),(150,-37),(140,-38),(130,-32),(120,-35),(113,-30),(113,-22)]
d.rectangle([MX,MY,MX+MW,MY+MH],fill=(205,225,240),outline=NAVY,width=1); d.text((MX+6,MY+4),'WORLD MAP \u00b7 PINS 1\u201313',font=F(9,True),fill=NAVY)
for poly in (NA,SA,AF,EU,AU): d.polygon([proj(a,b) for a,b in poly],fill=(190,205,160),outline=(90,110,80))
PINS=[(1,46.7,24.7,0,0),(2,121.5,31.2,0,0),(3,-74.0,40.7,0,0),(4,35.1,47.8,0,0),(5,-17.4,14.7,0,0),(6,56.3,26.5,0,0),(7,-74.0,40.7,16,-12),(8,-122.1,47.7,0,0),(9,30.5,39.8,0,0),(10,-75.5,10.4,0,0),(11,45.0,12.8,0,0),(12,44.9,13.0,18,10),(13,98.5,39.7,0,0)]
for n,lon,lat,dx,dy in PINS:
    px,py=proj(lon,lat); qx,qy=px+dx,py+dy
    if dx or dy: d.line([(px,py),(qx,qy)],fill=RED,width=1)
    d.ellipse([qx-8,qy-8,qx+8,qy+8],fill=RED,outline=(255,255,255),width=1); d.text((qx,qy-5),str(n),font=F(8,True),fill=(255,255,255),anchor='mm')
LEG=['1 Riyadh','2 Shanghai','3 New York','4 Zaporizhzhia','5 Senegal','6 Hormuz','7 New York','8 Redmond','9 Eskisehir','10 Cartagena','11 Aden','12 Lahj','13 Jiuquan']; d.text((630,632),'NUMBERED LEGEND',font=F(9,True),fill=RED)
for i,s in enumerate(LEG): d.text((630,648+i*13),s,font=F(9),fill=INK)
d.text((630,822),'Map: equirectangular, real lat/lon.',font=F(8),fill=GREY)
ALSO=['14 Ankara: Haftar visits Turkey, first time [REPORTED]','15 London: UK sanctions Houthis + 4 [OFFICIAL]','16 Villavicencio: car bomb injures 23 [REPORTED]','17 Gaza: Israel kills Hamas security chief [REPORTED]','18 Baghdad: Iraq takes Kurdish oilfields [OFFICIAL]','19 Gaza: meningitis alert, 272 in Oct [OFFICIAL]','20 DR Congo: missing Cessna, rebels claim [CLAIM]','21 Hanoi: hot-pot blast kills at least 6 [REPORTED]','22 Finland Gulf: Ukraine hits Sparta II [REPORTED]','23 Kuala Lumpur: migrants back to Myanmar [OFFICIAL]','24 Ulleungdo: shelter order, Russian jets [OFFICIAL]','25 Dhaka: Hasina plans return 16 Dec [REPORTED]','26 The Hague: 14 back ICJ Myanmar ruling [REPORTED]','27 Jakarta: 2 VP candidates nominated [OFFICIAL]','28 Beijing: official Ma death for spying [OFFICIAL]','29 Brussels: NATO vows space defence [OFFICIAL]','30 Mexico City: El Chapo, US drone aided [REPORTED]','31 San Salvador: 3 soldiers killed in Haiti [OFFICIAL]','32 Ottawa: Canada, only 41.9% of air fleet ready [REPORTED]','33 Washington: US adds Megaspeed to blacklist [OFFICIAL]','34 Kyiv: Zelensky urges talks soon [REPORTED]','35 Ras Al Khaimah: bus crash kills 13 [REPORTED]','36 London: record 5,258 heat deaths [OFFICIAL]','37 Kourou: Ariane 6 lofts 36 satellites [OFFICIAL]','38 Cikande: factory-fire toll rises to 26 [REPORTED]']
d.text((14,824),'ALSO ON TUESDAY 24 NOVEMBER \u2014 25 MORE STORIES',font=F(10,True),fill=RED)
for i,s in enumerate(ALSO):
    col=i//9; row=i%9; x=14+col*340; y=840+row*12; d.text((x,y),s,font=F(7),fill=INK)
d.rectangle([14,950,W-14,1000],outline=RED,width=1,fill=(255,240,240))
para(d,20,954,'DATE CHECK: Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC. LEFT OUT (not 24 Nov): Hormuz mine claim (23 Nov); Nvidia Huang return (23 Nov); EU sanctions package 22 (23 Nov); COP31 no deal (22 Nov); Merkury sunk (22 Nov); El Chapo Isidro arrested Fri 20 Nov; Cikande fire started Sat 21 Nov; Trump hush-money appeal (23 Nov); ATP final (22 Nov); F1 Las Vegas GP Sat 21 Nov. NOT YET: Shenzhou-24 launch Wed 25 Nov 00:18 UTC; MPR VP session 11 Dec; Huawei sentencing Sep 2027; Hasina return 16 Dec; COP32 decision not set.',F(8),980)
d.text((14,1006),'Sources: dailysummaryof.com/world/2026-11-24 \u00b7 Reuters \u00b7 AP \u00b7 UKMTO \u00b7 CAS \u00b7 CCDI \u00b7 CMSA \u00b7 UKHSA. CONFIRMED = 2+ outlets \u00b7 OFFICIAL = on record \u00b7 REPORTED = one outlet \u00b7 CLAIM = one side. Scenes are drawn illustrations, not photographs.',font=F(7),fill=GREY)
os.makedirs(os.path.dirname(OUT) or '.',exist_ok=True); img.save(OUT); print(OUT,img.size,os.path.getsize(OUT))
