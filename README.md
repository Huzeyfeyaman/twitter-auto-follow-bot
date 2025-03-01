## Lisans
Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakabilirsiniz.

# Twitter Auto-Follow Bot
Bu proje, Twitter'da belirli kriterlere göre kullanıcıları otomatik olarak takip eden bir Python script'idir. Eğitim amaçlı geliştirilmiş olup, Twitter API (v2) ve `tweepy` kütüphanesi kullanılarak çalışır. **Lütfen bu aracı etik ve Twitter'ın kullanım kurallarına uygun şekilde kullanın.**

## Özellikler
- Belirli bir hashtag veya anahtar kelimeye göre kullanıcıları takip eder.
- Bot hesapları filtrelemek için takipçi/takip oranı kontrolü.
- Günlük takip limiti belirleme.
- İşlemleri bir log dosyasına kaydeder (`twitter_follow_log.txt`).
- Twitter spam algılamasını önlemek için rastgele gecikmeler.

## Gereksinimler
- Python 3.x
- Twitter Developer hesabı ve API erişimi (API Key, Secret, Access Token, Bearer Token).
- Gerekli kütüphane: `tweepy` (`pip install tweepy`)

## Kurulum
1. `pip install tweepy python-dotenv`
2. `.env` dosyası oluşturun:
3. Bu repository'yi klonlayın:
   ```bash
   git clone https://github.com/Huzeyfeyaman/twitter-auto-follow-bot.git
   cd twitter-auto-follow-bot
