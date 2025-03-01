#!/usr/bin/env python3
# Twitter Auto-Follow Bot
# Telif Hakkı (c) 2025 [ADIN]
# Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.

import tweepy
import time
import random
import datetime
import logging
from dotenv import load_dotenv
import os

# Logging ayarları
logging.basicConfig(filename='twitter_follow_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# .env dosyasından API anahtarlarını yükle
load_dotenv()

# Twitter API kimlik bilgileri
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# API anahtarlarının varlığını kontrol et
if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN]):
    raise ValueError("Lütfen .env dosyasındaki tüm API anahtarlarını doldurun.")

# Kimlik doğrulama
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY,
                       consumer_secret=API_SECRET, access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)


# Takip fonksiyonu
def follow_users(search_query, max_follows=50, min_follower_ratio=0.5):
    followed_count = 0
    tweets = tweepy.Cursor(api.search_tweets, q=search_query, lang="tr", tweet_mode="extended").items(100)

    for tweet in tweets:
        if followed_count >= max_follows:
            print("Maksimum takip sayısına ulaşıldı.")
            break

        user = tweet.user
        username = user.screen_name
        followers_count = user.followers_count
        following_count = user.friends_count

        # Bot veya düşük kaliteli hesapları filtrele
        if followers_count < 50 or following_count == 0:
            logging.info(f"{username} düşük takipçi sayısı nedeniyle atlandı.")
            continue

        follower_ratio = followers_count / (following_count + 1)
        if follower_ratio < min_follower_ratio:
            logging.info(f"{username} düşük takipçi/takip oranı nedeniyle atlandı.")
            continue

        # Zaten takip ediliyor mu kontrol et
        if api.get_friendship(source_screen_name=api.get_user(screen_name=api.get_me().screen_name).screen_name,
                              target_screen_name=username)[0].following:
            logging.info(f"{username} zaten takip ediliyor.")
            continue

        try:
            client.follow_user(target_user_id=user.id)
            followed_count += 1
            logging.info(f"{username} takip edildi. (Takipçi: {followers_count}, Takip: {following_count})")
            print(f"{followed_count}. {username} takip edildi.")
            time.sleep(random.uniform(5, 15))  # Spam önlemek için gecikme
        except tweepy.TweepError as e:
            logging.error(f"Hata: {username} takip edilemedi - {str(e)}")
            continue

    print(f"Toplam {followed_count} kullanıcı takip edildi.")


# Ana fonksiyon
if __name__ == "__main__":
    print("Otomatik takip başlıyor...")
    search_query = "#python -filter:retweets"  # Özelleştirilebilir
    max_follows = 50  # Maksimum takip sayısı
    min_follower_ratio = 0.5  # Minimum takipçi/takip oranı

    try:
        follow_users(search_query, max_follows, min_follower_ratio)
    except KeyboardInterrupt:
        print("\nDurduruldu.")
    except Exception as e:
        print(f"Bir hata oluştu: {str(e)}")
    print("İşlem tamamlandı. Detaylar 'twitter_follow_log.txt' dosyasında.")