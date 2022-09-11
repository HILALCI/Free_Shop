from tkinter import *
from tkinter import messagebox
import hashlib
import mysql.connector


#Mysql baslantisini yapmak icin
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "Magaza"
)

#Cursor ile calismtirma imlec ile ilerleme yapmak icin ekliyoruz.
mycurs = mydb.cursor()


#GUI windowlarin her biri fonksiyon olarak ele alinmisitir.
def openMain():


    def openInfo():
        inf = Toplevel()
        inf.title("Hakkimizda")
        inf.bind("<Escape>", lambda event: inf.destroy())
        Label(inf, text = "Özgür Mağaza", font=("Times New Roman TUR", 12, "bold")).pack()
        Label(inf, text = "----------", font=("Times New Roman TUR", 12, "bold")).pack()
        Label(inf, text = "Mağazamiz 2022 yilinda faliyetine baslamistir.").pack(anchor=W)
        Label(inf, text = "Mağazamizda sadece Ozgur urunler bulunmaktadir.").pack(anchor=W)
        Label(inf, text = "Purism urunlerinin resmi distribütöruyuz.").pack(anchor=W)
        Label(inf, text = "").pack(anchor=W)
        Label(inf, text = "").pack(anchor=W)
        Label(inf, text = "Toplu alimlar icin : ozgurmagaza@mail.co").pack(anchor=W)

    def openLogin():
        def openReg():
            kay = Tk()
            kay.title("Kayit Formu")
            kay.geometry("500x400+400+200")
            kay.resizable(True, True)
            kay.bind("<Escape>", lambda event: kay.destroy())
            Label(kay, text = "Kayit Formu", font=("Times New Roman TUR", 12, "bold")).grid(row=0, column=10)
            Label(kay, text = "-------------").grid(row=1, column=10)
            Label(kay, text = "").grid(row=2, column=2)
            Label(kay, text = "* olan alanlarin doldurulmasi zorunludur.").grid(row=3, column=10)
            Label(kay, text = "").grid(row=4, column=0)
            Label(kay, text = "").grid(row=5, column=1)
            Label(kay, text = "").grid(row=6, column=2)
            Label(kay, text = "").grid(row=7, column=3) 
            Label(kay, text = "").grid(row=4, column=4)
            Label(kay, text = "").grid(row=4, column=5)
            Label(kay, text = "T.C. Kimlik Numarasi*").grid(row=6, column=9)
            Label(kay, text = "Ad*").grid(row=7, column=9)
            Label(kay, text = "Soyad*").grid(row=8, column=9)
            Label(kay, text = "Numara*").grid(row=9, column=9)
            Label(kay, text = "E-mail*").grid(row=10, column=9)
            Label(kay, text = "Parola*").grid(row=11, column=9)
            Label(kay, text = "Adres Kodu*").grid(row=12, column=9)
            tc = Entry(kay, width =11)
            tc.grid(row=6, column=10)
            ad = Entry(kay)
            ad.grid(row=7, column=10)
            soyad = Entry(kay)
            soyad.grid(row=8, column=10)
            numa = Entry(kay)
            numa.grid(row=9, column=10)
            mail = Entry(kay)
            mail.grid(row=10, column=10)
            passwd = Entry(kay)
            passwd.grid(row=11, column=10)
            adres = Entry(kay,width= 10)
            adres.grid(row=12, column=10)
            
            def kayit():

                if(len(str(passwd.get())) != 0):
                    h = hashlib.sha3_512()
                    h.update(str.encode(f"{str(passwd.get())}"))

                if(len(str(tc.get())) == 0 or len(str(ad.get())) == 0 or len(str(soyad.get())) == 0 or len(str(mail.get())) == 0 or len(str(adres.get())) == 0 or len(str(passwd.get())) == 0 or len(str(numa.get())) == 0):
                    messagebox.showwarning("Uyari", "Lutfen zorunlu alanlari bos birakmayiniz.")
                else:
                    if(not(str(tc.get()).isdigit())):
                        messagebox.showwarning("Uyari", "T.C. Kimlik Numarasi yanlis girilmistir.\nLutfen tamami sayi oldugundan emin olun.")
                    elif(not(str(numa.get()).isdigit())):
                        messagebox.showwarning("Uyari", "Telefon numarasi yanlis girilmistir.\nLutfen tamami sayi oldugundan emin olun.")    
                    elif(len(str(tc.get())) != 11):
                        messagebox.showwarning("Uyari", "T.C. Kimlik Numarasi yanlis girilmistir.\nLutfen 11 karakter oldugundan emin olun.")
                    elif(str(mail.get()).find("@") == -1):
                        messagebox.showwarning("Uyari", "E-mail yanlis girilmistir.\nLutfen e-mail dogru oldugundan emin olun.")
                    else:
                        has = hashlib.sha3_512()
                        has.update(str.encode(f"{passwd.get()}"))
                        mycurs.execute("CALL setMusteri(%s, %s, %s, %d, %s, %s,%s);", (str(tc.get()), str(ad.get()), str(soyad.get()), int(numa.get()), str(mail.get()), str(has.hexdigest()), str(adres.get())))
                        rspReg = messagebox.askokcancel("Kayitlanma","Kaydiniz basariyla tamamlanmistir.\nLutfen sisteme giris yapiniz.")
                        if rspReg == True :
                            kay.destroy()
                        elif rspReg == False :
                            kay.destroy()
                            logi.destroy()
            '''
            h = hashlib.sha3_512()
            h.update(str.encode(f"{passwd.get()}"))
            print(h.hexdigest())
            '''
            Button(kay, text="Kayit ol",relief = GROOVE,activebackground="blue", command=kayit).grid(row=14, column=11)

        def openBuy():
            def openSetting():
                ayar = Tk()
                ayar.title("Ayarlar")
                ayar.geometry("500x400+400+200")
                ayar.resizable(True, True)
                ayar.bind("<Escape>", lambda event: ayar.destroy())
                Label(ayar, text = "").grid(row=5, column=12)
                Label(ayar, text = "").grid(row=8, column=12)
                Label(ayar, text = "Sifre Guncelleme", font=("Times New Roman TUR", 12, "bold")).grid(row=10, column=10)
                Label(ayar, text = "----------", font=("Times New Roman TUR", 12, "bold")).grid(row=12, column=10)
                Label(ayar, text = "Eski Parola*").grid(row=14, column=9)
                Label(ayar, text = "Yeni Parola*").grid(row=15, column=9)
                esif = Entry(ayar,show="*")
                esif.grid(row=14, column=10)
                ysif = Entry(ayar,show="*")
                ysif.grid(row=15, column=10)
                def goster():
                    if(selea.get()== 1):
                        esif.config(show="")
                        ysif.config(show="")
                    else:
                        esif.config(show="*")
                        ysif.config(show="*")
                selea = IntVar(ayar) 
                shwa = Checkbutton(ayar, text="Sifreleri Goster", onvalue=1, offvalue=0, variable=selea, command=goster)
                shwa.grid(row=16, column=10)


                def gkontrol():
                    if(len(str(esif.get())) > 0 and len(str(ysif.get())) > 0):
                        if(str(esif.get()) == str(ysif.get())):
                            messagebox.showwarning("Uyari", "Ayni sifreleri girdiniz.")
                        else:
                            try:
                                mycurs.execute(f"CALL upPass('a@a.com', %s);", (str(ysif.get()),))
                                 
                            except mysql.connector.Error as e:
                                print ("Error code:", e.errno)
                                print ("SQLSTATE value:", e.sqlstate)
                                print ("Error message:", e.msg)      
                            messagebox.showinfo("Sifre Guncelleme", "Sifreniz basarili bir sekilde guncellenmistir.")
                            ayar.destroy()
                    elif(len(str(esif.get())) == 0 and len(str(ysif.get())) != 0 or len(str(esif.get())) != 0 and len(str(ysif.get())) == 0):
                        messagebox.showwarning("Uyari", "Lutfen zorunlu alanlari bos birakmayiniz.")

                Button(ayar, text="Guncelle",relief = GROOVE,activebackground="blue", command=gkontrol).grid(row=18, column=11)
                

            def openOrder():
                order = Tk()
                order.title("Özgür Mağaza")
                order.geometry("500x400+400+200")
                order.resizable(True, True)
                order.bind("<Escape>", lambda event: order.destroy())
                buy.destroy()
                Button(order, text="Ayarlar",relief = GROOVE,activebackground="blue", command=openSetting).pack(anchor=NE)
                Button(order, text="Cikis Yap",relief = GROOVE,activebackground="blue", command=order.destroy).pack(anchor=NE)
                sip = Text(order, height= 30 , width= 200)
                sip.pack(padx= 10, pady= 10, anchor=NW)
                Label(order, text = "Siparis Iptal*", font=("Times New Roman TUR", 12, "bold")).pack(anchor=SW)
                Label(order, text = "!Asagidaki alana iptal etmek istediginiz siparisin ID'sini giriniz.!").pack(anchor=SW)
                sipId = Entry(order)
                sipId.pack(anchor=SW)

                def siptal():
                    if (len(str(sipId.get())) == 0):
                        messagebox.showwarning("Uyari", "Lutfen siparis id alanini bos birakmayiniz.")
                    else:   
                        rspIp = messagebox.askokcancel("Siparis Iptal", f"{str(sipId.get())} nolu siparisiniz iptal etmek istediginizden emin misiniz.")
                        if rspIp == True :
                            mycurs.execute(f"CALL Siptal({int(sipId.get())});")
                            messagebox.showinfo("Siparis Iptal", f"{str(sipId.get())} nolu siparisiniz iptal edilmistir.")
                        elif rspIp == False :
                            messagebox.showwarning("Siparis Iptal", "Siparisinizin iptal islemi iptal edilmistir.")
                        
                Button(order, text="Siparis Iptal Et",relief = GROOVE,activebackground="blue", command=siptal).pack(anchor=SW)
            
            #if kad == or passw ==
            try:
                mycurs.execute(f"CALL getPass(%s, %s);",(email.get(), passw.get()))
                result = mycurs.fetchall()
                if (result != "True"):
                    logi.destroy()
            except mysql.connector.Error as e:
                print ("Error code:", e.errno)
                print ("SQLSTATE value:", e.sqlstate)
                print ("Error message:", e.msg)
            
            buy = Tk()
            buy.title("Özgür Mağaza")
            buy.geometry("500x400+400+200")
            buy.resizable(True, True)
            buy.bind("<Escape>", lambda event: buy.destroy())
            logi.destroy()
            Button(buy, text="Siparislerim",relief = GROOVE,activebackground="blue", command=openOrder).grid(row=0, column=10)
            Button(buy, text="Ayarlar",relief = GROOVE,activebackground="blue", command=openSetting).grid(row=0, column=11)
            Button(buy, text="Cikis Yap",relief = GROOVE,activebackground="blue", command=buy.destroy).grid(row=0, column=12)

            sVal1 = StringVar(buy)
            sVal2 = StringVar(buy)
            sVal3 = StringVar(buy)
            Label(buy, text = "Urunlerin Listesi", font=("Times New Roman TUR", 12, "bold")).grid(row=0, column=1)
            #Label(buy, text = "----------").grid(row=1, column=1)
            Label(buy, text = "Librem 14 Version 1:").grid(row=2, column=1)
            Label(buy, text = """\tScreen: 14″ matte 1920×1080
            \tCPU: Intel Core i7 10710U, 6 cores & 12 threads
            \tRAM: up to 64GB
            \tGPU: Intel UHD Graphics 620
            \tStorage: 2 x NVMe-capable M.2 slots
            """).grid(row=3, column=1)

            sPc = Spinbox(buy, from_=0, to=10, increment=1,textvariable=sVal1, justify=CENTER)
            sPc.grid(row=3, column=5)

            Label(buy, text = "=========").grid(row=4, column=1)

            Label(buy, text = "Librem Mini Version 2:").grid(row=5, column=1)
            Label(buy, text = """\tProcessor: Intel Core i7-10510U (Comet Lake), Active (fan) Cooling, 4 Cores, 8 Threads, up to 4.9GHz
            \tGraphics: Intel UHD Graphics 620
            \tMemory: DDR4-2400, 2 SO-DIMM slots, Max 64GB Support, 1.2V DDR4 L2133/2400MHz
            \tStorage: 1 SATA III 6Gbps SSD/HDD (7mm), 1 M.2 SSD (SATA III/NVMe x4)
            \tVideo: 1 HDMI 2.0 4K@60Hz, 1 DisplayPort 1.2 4K@60Hz
            \tUSB Ports: 4 x USB 3.0, 2 x USB 2.0, 1 x USB Type C 3.1
            \tAudio: 3.5mm AudioJack (Mic-in & Headphone-out combo)
            \tNetworking: 1 RJ45 (Gigabit Ethernet LAN), with optional WiFi Atheros ATH9k Module, 802.11n (2.4/5.0 GHz)
            \tBluetooth: Ar3k Bluetooth 4.0 (optional)
            """).grid(row=6, column=1)

            sMini = Spinbox(buy, from_=0, to=10, increment=1,textvariable=sVal2, justify=CENTER)
            sMini.grid(row=6, column=5)

            Label(buy, text = "=========").grid(row=7, column=1)

            Label(buy, text = "Librem 5 BM818-E1:").grid(row=8, column=1)
            Label(buy, text = """\tDisplay : 5.7″ IPS TFT screen @ 720×1440
            \tProcessor: i.MX8M (Quad Core) max. 1.5GHz
            \tMemory: 3GB
            \tStorage : 32 GB eMMC internal storage
            \tWireless : 802.11abgn 2.4 Ghz / 5Ghz + Bluetooth 4
            \tBaseband : Broadmobi BM818 w/ single nanosim tray on replaceable M.2 card
            \tSmartcard: Reader with 3FF card slot (microSIM card size)
            \tSound : 1 earpiece speaker, 3.5mm headphone jack
            \tExternal Storage: microSD storage expansion
            \tFront Camera: 8 MPixel
            \tBack Camera: 13 MPixel w/ LED flash
            \tUSB Type C: USB 3.0 data, Charging (Dual-Role Port), Video out
            \tBattery: User replaceable – 4,500 mAh""").grid(row=9, column=1)

            sPhone = Spinbox(buy, from_=0, to=10, increment=1,textvariable=sVal3, justify=CENTER)
            sPhone.grid(row=9, column=5)

            def al():
                urad = ["Librem 14 Version 1", "Librem Mini Version 2", "Librem 5 BM818-E1"]
                ufiyat = list()
                try:
                    for i in range(3):
                        mycurs.execute(f"CALL getUFiyat(%s);",(urad[i],))
                        result = mycurs.fetchall()
                        ufiyat.append(result)
                        
                except mysql.connector.Error as e:
                    print ("Error code:", e.errno)
                    print ("SQLSTATE value:", e.sqlstate)
                    print ("Error message:", e.msg)
                tutar = ( int(sPc.get()) * ufiyat[0] ) + ( int(sMini.get()) * ufiyat[1] ) + ( int(sPhone.get()) * ufiyat[2] )
                rspBuy = messagebox.askyesno("Siparis Onay",f"""Siparisinizi onayliyor musunuz?

Librem 14 Version 1 = {ufiyat[0]} $ x {str(sPc.get())}
Librem Mini Version 2 = {ufiyat[1]} $ x {str(sMini.get())}
Librem 5 BM818-E1 = {ufiyat[2]} $ x {str(sPhone.get())}
+
----------------------------------------
Toplam Tutar =\t {tutar} $ """)
                if rspBuy == True :
                    if (str(sPc.get()) == "0" and str(sMini.get()) == "0" and str(sPhone.get()) == "0"):
                        messagebox.showinfo("Siparis", "Siparisiniz onaylanmistir.\nKargo ucreti tahsil edilecektir.")
                    else:    
                        messagebox.showinfo("Siparis", "Siparisiniz onaylanmistir.\n1 Hafta icersinde teslim edilecektir.")
                elif rspBuy == False :
                    sVal1.set("0")
                    sVal2.set("0")
                    sVal3.set("0")
                    
            Button(buy, text="Satin Al",relief = GROOVE,activebackground="blue", command=al).grid(row=10, column=12)

        logi = Tk()
        logi.title("Özgür Mağaza")
        logi.geometry("500x400+400+200")
        logi.resizable(True, True)
        main.destroy()
        logi.bind("<Escape>", lambda event: logi.destroy())
        Label(logi, text = "", ).grid(row=0, column=0)
        Label(logi, text = "", ).grid(row=1, column=1)
        Label(logi, text = "", ).grid(row=2, column=2)
        Label(logi, text = "", ).grid(row=3, column=3)
        Label(logi, text = "", ).grid(row=4, column=0)
        Label(logi, text = "", ).grid(row=4, column=1)
        Label(logi, text = "", ).grid(row=4, column=2)
        Label(logi, text = "", ).grid(row=4, column=3) 
        Label(logi, text = "", ).grid(row=4, column=4)
        Label(logi, text = "", ).grid(row=4, column=5)
        Label(logi, text = "", ).grid(row=4, column=6)
        Label(logi, text = "", ).grid(row=4, column=7)
        Label(logi, text = "", ).grid(row=4, column=8)
        Label(logi, text = "E-mail").grid(row=4, column=9)
        Label(logi, text = "Parola").grid(row=5, column=9)
        email = Entry(logi)
        email.grid(row=4, column=10)
        passw = Entry(logi, show="*")
        passw.grid(row=5, column=10)
        def goster():
            if(sele.get()== 1):
                passw.config(show="")
            else:
                passw.config(show="*")
        sele = IntVar(logi) 
        shw = Checkbutton(logi, text="Sifreyi Goster", onvalue=1, offvalue=0, variable=sele, command=goster)
        shw.grid(row=7, column=10)
        
        Button(logi, text="Giris Yap",relief = GROOVE,activebackground="blue", command=openBuy).grid(row=8, column=11)
        Button(logi, text="Kayit ol",relief = GROOVE,activebackground="blue", command=openReg).grid(row=9, column=12)

    main = Tk()
    main.title("Özgür Mağaza")
    main.geometry("500x400+400+200")
    main.resizable(True, True)
    main.bind("<Escape>", lambda event: main.destroy())

    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "Magazamiza Hosgeldiniz", font=("Times New Roman TUR", 12, "bold")).pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Button(main, text="Giris Yapiniz",relief = GROOVE,activebackground="blue", command=openLogin).pack()
    Button(main, text="Hakkimizda",relief = GROOVE,activebackground="blue", command=openInfo).pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "").pack()
    Label(main, text = "*Magzamizda sadece ozgur urunler vardir.*").pack()

    main.mainloop()

openMain()
mydb.close()
