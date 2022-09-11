CREATE DATABASE Magaza;
USE Magaza;

/*Tablolari eklemek icin
Not: Ilk Yildirima bir kere basmaniz halinde otomatik tum hepsi eklenecektir.
*/
CREATE TABLE Musteriler (
    TC_No DECIMAL(11) NOT NULL CHECK(LENGTH(TC_No) = 11),
    Ad VARCHAR(255) NOT NULL,
    Soyad VARCHAR(255) NOT NULL,
    Numara INT  UNIQUE,
    Email VARCHAR(255) UNIQUE NOT NULL CHECK(Email LIKE "%@%"),
    Parola CHAR(128) NOT NULL,
    Adres VARCHAR(11) NOT NULL,
    
    PRIMARY KEY (TC_No)
);

CREATE TABLE Urunler (
    UID INT AUTO_INCREMENT NOT NULL,
    UrunAdi VARCHAR(255) NOT NULL,
    UrunAdet INT NOT NULL,
    UrunFiyat INT NOT NULL,
    
    PRIMARY KEY (UID)
);

CREATE TABLE Siparis (
    SID INT AUTO_INCREMENT NOT NULL,
    TC_No DECIMAL(11) NOT NULL,
    UID INT NOT NULL,
    Adet INT NOT NULL,
    STarih VARCHAR(100) NOT NULL,
    
    PRIMARY KEY (SID),
    FOREIGN KEY (UID) REFERENCES Urunler(UID),
    FOREIGN KEY (TC_No) REFERENCES Musteriler(TC_No)
);

/*Musteri kendi bilgilerini almak ister ise
CALL getMus(TC_NO);
*/
DELIMITER $$
CREATE PROCEDURE getMus(
	IN tc DECIMAL(11)
)
BEGIN
SELECT * FROM Musteriler
WHERE TC_No = tc;
END $$
DELIMITER ;

/* Urunleri getirmek icin ayrica view olarakta eklenmistir.
CALL getUrun();
*/
DELIMITER $$
CREATE PROCEDURE getUrun()
BEGIN
SELECT * FROM Urunler;
END $$
DELIMITER ;

/*Siparis bilgilerini almak icin
CALL getSip("E-mail adresiniz");
*/
DELIMITER $$
CREATE PROCEDURE getSip(
	IN mail VARCHAR(255)
)
BEGIN
SELECT Siparis.SID AS `Siparis ID`, Urunler.UID AS `Urun ID`, Urunler.UrunAdi AS `Urun Adi`, Siparis.Adet, Siparis.STarih AS `Satin Alindigi Tarih`
FROM Siparis INNER JOIN Musteriler INNER JOIN Urunler
WHERE Siparis.TC_No = Musteriler.TC_No AND Musteriler.Email = mail AND Siparis.UID = Urunler.UID
ORDER BY Siparis.STarih DESC;
END $$
DELIMITER ;

/*Urun ID degerini almak icin
CALL getUID("Urun_Adi");
*/
DELIMITER $$
CREATE PROCEDURE getUID(
	IN uad VARCHAR(255)
)
BEGIN
SELECT UID FROM Urunler
WHERE UrunAdi = uad;
END $$
DELIMITER ;

/*Urunun fiyatini gormek icin
CALL getUFiyat("Urun_Adi");
*/
DELIMITER $$
CREATE PROCEDURE getUFiyat(
	IN uad VARCHAR(255)
)
BEGIN
SELECT UrunFiyat FROM Urunler
WHERE UrunAdi = uad;
END $$
DELIMITER ;

/*Bu yeni parola ve login isleminde kontrol amacli eklenmistir.Tabi isteyen kullanici parolasini gormek icin kullanabilir.
CALL getPass("E-mail adresiniz", "Sifreniz");
*/
DELIMITER $$
CREATE PROCEDURE getPass(
	IN mail VARCHAR(255), par CHAR(128)
)
BEGIN
SELECT IF(Parola = par, "True", "False") AS `Ayni mi?`
FROM Musteriler
WHERE Email = mail; 
END $$
DELIMITER ;

/*Urunun stok durumunu ogrenmek icin
CALL getStok(Urun_ID);
*/
DELIMITER $$
CREATE PROCEDURE getStok(
	IN ud INT
)
BEGIN
SELECT UID AS `Urun ID`,  UrunAdi AS `Urun Adi`,  UrunAdet `Urun Adeti` FROM Urunler
WHERE UID = ud;
END $$
DELIMITER ;

/*Urun bilgilerini tabloya eklemek icin
CALL setUrun("Urun_Adi", Adeti, Fiyat);
*/
DELIMITER $$
CREATE PROCEDURE setUrun(
	IN uad VARCHAR(255),usay INT, ufi INT
)
BEGIN
INSERT INTO Urunler (UrunAdi, UrunAdet, UrunFiyat)
VALUES (uad, usay, ufi);
END $$
DELIMITER ;

CALL setUrun("Librem 14 Version 1", 1000, 1370);
CALL setUrun("Librem Mini Version 2", 1000, 799);
CALL setUrun("Librem 5 BM818-E1", 1000, 1299);

/*Not: Urunler hataya sebep vermemek icin onceden eklenmistir.*/

/*Musteri bilgilerini tabloya ekelem icin
CALL setMusteri(TC_NO, "Ad", "Soyad", Numara, "E-mail", "Sifre", "Adres_Kodu");
*/
DELIMITER $$
CREATE PROCEDURE setMusteri(
	IN tc DECIMAL(11),ad VARCHAR(255),soyad VARCHAR(255),numara INT,email VARCHAR(255),sifre CHAR(128),adres VARCHAR(11)
)
BEGIN
INSERT INTO Musteriler
VALUES (tc,ad,soyad,numara,email,sifre,adres);
END $$
DELIMITER ;

/*Siparis girmek icin
CALL setSip(TC_NO,Urun_ID,Urun_Adeti);
*/
DELIMITER $$
CREATE PROCEDURE setSip(
	IN tc DECIMAL(11),uid INT,adet INT
)
BEGIN
INSERT INTO Siparis (TC_NO, UID, Adet, STarih)
VALUES (tc, uid, adet,NOW());
END $$
DELIMITER ;

/*Siparis iptal etmek icin
CALL Siptal(Siparis_ID);
*/
DELIMITER $$
CREATE PROCEDURE Siptal(
	IN sid INT
)
BEGIN
DELETE FROM Siparis
WHERE SID = sid;
END $$
DELIMITER ;

/*Stok guncelleme urunler satin alindiginda stok adetinden dusurmek icin kullaniyoruz.*/
DELIMITER $$
CREATE TRIGGER stokGun
AFTER INSERT ON Siparis FOR EACH ROW
BEGIN
UPDATE Urunler
SET UrunAdet = UrunAdet - NEW.Adet
WHERE UID = NEW.UID;
END $$
DELIMITER ;

/*Iptal edilen siparisin tekrar stok adet miktarini arttirmak degistirmek icin*/
DELIMITER $$
CREATE TRIGGER stokEs
AFTER DELETE ON Siparis FOR EACH ROW
BEGIN
UPDATE Urunler
SET UrunAdet = UrunAdet + OLD.Adet
WHERE UID = OLD.UID IN (SELECT * FROM Siparis 
						WHERE SID = OLD.SID
                    );
END $$
DELIMITER ;

/*Parolamizi guncellemek icin
CALL upPass("E-mail adresiniz", "Parolaniz");
*/
DELIMITER $$
CREATE PROCEDURE upPass(
	IN mai VARCHAR(255), pas CHAR(128)
)
BEGIN
UPDATE Musteriler
SET Parola = pas
WHERE Email = mai and Parola != pas;
END $$
DELIMITER ;

/*Urun bilgileri view kollanarak gormek icin
SELECT * FROM urunView;
*/
CREATE VIEW urunView AS
SELECT UID AS `Urun ID`, UrunAdi AS `Urun Adi`, UrunAdet AS `Urun Adet`, UrunFiyat AS `Urun Fiyat`
FROM Urunler;


/*STOK ARTISI RAPORU ICIN EKLEMEK ISTENIR ISE
CREATE TABLE StokArtis (
	STID INT AUTO_INCREMENT NOT NULL,
    UID INT NOT NULL,
    Adet INT NOT NULL,
    SATarih DATETIME NOT NULL,
    
    PRIMARY KEY (STID),
    FOREIGN KEY (UID) REFERENCES Urunler(UID)
);
*/

/*Bakim ve onarim icin asagidaki kodlari calistirabilirsiniz.
ANALYZE TABLE Musteriler;
ANALYZE TABLE Urunler;
ANALYZE TABLE Siparis;

REPAIR TABLE Musteriler;
REPAIR TABLE Urunler;
REPAIR TABLE Siparis;
*/
