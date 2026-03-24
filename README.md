# MCP Öğrenci Sandbox'ı

Python öğrenmek için hazırlanmış 4 zorlu kod dosyası içeren bir proje. Temiz kod yazma, hata ayıklama ve güvenlik konularında beceri geliştirmeye odaklanır.

## 📚 Proje Hakkında

Bu sandbox (oyun alanı), her biri farklı programlama zorluklarını gösteren 4 Python dosyasından oluşur:

1. **spaghetti_logic.py** - Kod kalitesi ve modülerlik
2. **failing_calculator.py** - Hata yönetimi ve hata ayıklama
3. **secret_leak.py** - Güvenlik ve şifre yönetimi
4. **mystery_module.py** - Kod analizi ve dokümantasyon

---

## 🎯 Dosyalar ve Zorluklar

### 1. spaghetti_logic.py
**Zorluk**: Karışık, tek parça kodu modüler ve bakımı kolay fonksiyonlara dönüştürmek.

**Orijinal Problemler**:
- Kötü değişken isimleri (res, d, val, s)
- Karışık sorumluluklar (hesaplama, formatlama, loglama)
- Dokümantasyon yok
- Tek tek parçaları test etmek zor

**Uygulanan Çözüm**:
- Tek sorumluluklı fonksiyonlara ayrıldı
- `calculate_total()` - çarpma işlemini yapar
- `format_total()` - çıktı metinlerini formatlar
- `log_results()` - dosya yazma işlemini yönetir
- Kapsamlı açıklama metinleri eklendi

**Çalıştırma**:
```bash
python -c "from spaghetti_logic import process_data; print(process_data([10, 20, 30]))"
```

---

### 2. failing_calculator.py
**Zorluk**: Belirli girdilerde çöken çalışma zamanı hatasını bulup düzeltmek.

**Orijinal Problem**:
```
ZeroDivisionError: division by zero
print(average_ratios([10, 5, 0]))  # Liste içinde 0 olduğunda çöker
```

**Kök Neden**:
- Fonksiyon `100 / numbers[i]` işlemini sıfır kontrolü yapmadan yapıyor

**Uygulanan Düzeltme**:
- Sıfır değerleri filtrele: `valid_numbers = [num for num in numbers if num != 0]`
- Hata yönetimi ve doğrulama ekle
- Tüm sayılar sıfır olursa mantıklı varsayılan değer döndür
- Dokümantasyon ile birim test desteği eklendi

**Çalıştırma**:
```bash
export AWS_SECRET_KEY=test_key
python failing_calculator.py
# Çıktı: Result: 15.0, Success! No division by zero error.
```

**Test Örnekleri**:
```bash
# Normal durum
python -c "from failing_calculator import average_ratios; print(average_ratios([10, 5]))"

# Sıfır ile (şimdi güvenli)
python -c "from failing_calculator import average_ratios; print(average_ratios([10, 5, 0]))"

# Özel durum: tüm sıfırlar
python -c "from failing_calculator import average_ratios; print(average_ratios([0, 0, 0]))"
```

---

### 3. secret_leak.py
**Zorluk**: Güvenli şifre yönetimi uygulamak ve gizli bilgi sızıntılarını önlemek.

**Orijinal Güvenlik Problemleri** ❌:
- AWS gizli anahtarı kaynak kodunda sabit yazılı
- Sırlar sürüm kontrolünde (GitHub) görünür
- Tam şifreler log'larda yazdırılır
- Repo erişimi olan herkes şifreleri çalabilir

**Uygulanan Güvenlik Düzeltmeleri** ✅:
- Şifreleri ortam değişkenlerinden yükle
- Güvenli loglama (sadece ilk 8 karakteri göster)
- Eksik şifreler için uygun hata yönetimi
- `.gitignore` `.env` dosya commit'lerini engeller
- Geliştiriciler için `.env.example` şablonu

**Kullanım**:

1. Kurulum:
```bash
cp .env.example .env
# .env dosyasını düzenleyip gerçek AWS şifrelerinizi ekleyin
# AWS_SECRET_KEY=gercek_anahtariniz_buraya
```

2. Ortam değişkeni ile çalıştırma:
```bash
export AWS_SECRET_KEY=AKIA_GERCEK_ANAHTARINIZ_BURAYA
python secret_leak.py
# Çıktı: INFO:__main__:Connecting to AWS (key starts with: AKIA_GER...)
```

**Güvenlik En İyi Uygulamaları**:
- `.env` dosyasını asla git'e göndermeyin (`.gitignore` ile korunur)
- Yerel geliştirme için ortam değişkenlerini kullanın
- Üretimde gizli bilgi yöneticileri kullanın (AWS Secrets Manager, HashiCorp Vault)
- Sadece hassas olmayan anahtar önizlemelerini log'layın
- Şifrelerin sağlandığını kullanmadan önce doğrulayın

Detaylı güvenlik analizi için `SECURITY_FIXES.md` dosyasına bakın.

---

### 4. mystery_module.py
**Zorluk**: Okunması zor bir fonksiyonu anlamak ve dokümante etmek.

**Ne Yapar**:
`fn_x(a, b, c)` fonksiyonu **ikinci derece denklemleri** ikinci derece denklem formülü kullanarak çözer.

**Çözülen Formül**:
```
Denklem: ax² + bx + c = 0
Diskriminant: d = b² - 4ac
Çözümler (kökler): x = (-b ± √d) / 2a
```

**Örnekler**:
```python
# x² - 5x + 6 = 0  →  (x-2)(x-3)=0  →  kökler: (3, 2)
fn_x(1, -5, 6)  # Döner: (3.0, 2.0)

# x² + 1 = 0  →  gerçek çözüm yok
fn_x(1, 0, 1)   # Döner: None (diskriminant < 0)
```

**Önemli İçgörü**: Matematiksel bağlamı anlamak gizemli kodu açık hale getirir!

---

## 📋 Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.7+
- Git
- GitHub CLI (isteğe bağlı, repo yönetimi için)

### İndirme ve Çalıştırma
```bash
git clone https://github.com/iklimcelebi/mcp-student-sandbox.git
cd mcp-student-sandbox

# Tüm dosyaları test et
python spaghetti_logic.py
python failing_calculator.py
python secret_leak.py
```

---

## 🔐 Güvenlik Yapılandırması

### Ortam Değişkenleri
Git'e gönderilmeyen bir `.env` dosyası oluşturun:
```bash
cp .env.example .env
# Gerçek şifrelerinizle düzenleyin
AWS_SECRET_KEY=AKIA_GERCEK_ANAHTARINIZ_BURAYA
AWS_ACCESS_KEY=ASIA_GERCEK_ANAHTARINIZ_BURAYA
```

### .gitignore
Otomatik olarak göz ardı edilen korumalı dosyalar:
- `.env` - Yerel gizli bilgiler
- `__pycache__/` - Python derlenmiş dosyalar
- `*.log` - Log dosyaları
- `.vscode/`, `.idea/` - IDE klasörleri

---

## 📚 Öğrenilecek Beceriler

Bu sandbox'ı tamamladıktan sonra şunları anlayacaksınız:

✅ **Temiz Kod**: Modülerlik, tek sorumluluk, isimlendirme kuralları
✅ **Hata Ayıklama**: Kök nedenleri bulma, hata yönetimi, test etme
✅ **Güvenlik**: Şifre yönetimi, gizli bilgi koruması, en iyi uygulamalar
✅ **Kod Analizi**: Karmaşık fonksiyonları anlama, matematiksel kavramlar

---

## 📖 Dokümantasyon

- `SECURITY_FIXES.md` - Detaylı güvenlik analizi ve çözümler
- `.env.example` - Ortam değişkeni şablonu
- `.gitignore` - Git hariç tutma kuralları

---

## 🤝 Katkıda Bulunma

Bu bir öğrenme sandbox'ı. Serbestçe:
- Daha fazla refactor yapın
- Test örnekleri ekleyin
- Dokümantasyonu iyileştirin
- Farklı yaklaşımlar deneyin

---

## 📝 Lisans

Eğitim projesi - öğrenme amaçlı serbestçe kullanın.

---

## 🔗 Kaynaklar

- [PEP 8 - Python Stil Rehberi](https://www.python.org/dev/peps/pep-0008/)
- [OWASP - Şifre Yönetimi](https://owasp.org/)
- [Python Loglama En İyi Uygulamaları](https://docs.python.org/3/howto/logging.html)
- [İkinci Derece Denklem Formülü](https://en.wikipedia.org/wiki/Quadratic_formula)

---

**Mutlu Öğrenmeler!** 🚀
