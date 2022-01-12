# Indonesia Constitution Question Answering System (Telegram Bot)

## *Quick Start*

### 0. Prerequisities

Pastikan python telah terpasang:

```bash
python3 --version
# Python 3.6.9
```
Jika perintah `python3` gagal , silahkan pasang terlebih dahulu.

Pastikan `git` telah terpasang dengan menjalankan perintah berikut:
```bash
git --version
# git version 2.17.1
```
Jika perintah `git` gagal, silahkan pasang terlebih dahulu.

### 1. Clone repository dengan `git`

Jalankan perintah berikut untuk menyalin *source code* dengan `git`:

```bash
git clone https://github.com/rochimfn/tanyahukum-bot.git
```
### 2. Masuk ke direktori

```
cd tanyahukum-bot
```

### 3. Memasang dependensi

**WARNING:** Perintah berikut akan memasang library secara **global**.

Tidak disarankan untuk production!
```
pip install -r requirements.txt
```

### 4. Mengatur token telegram pada `.env`

Buat berkas `.env` dan isi dengan token telegram bot. Token telegram bot dapat diminta dari [https://t.me/botfather](https://t.me/botfather)

Contoh:

```.env

TOKEN='100000:BBB....q'
```

### 5. Menjalankan `main.py`

```bash
python3 main.py vps
```

## Pemasangan dengan `docker`

Buat berkas `.env` dan isi dengan token telegram bot. Token telegram bot dapat diminta dari [https://t.me/botfather](https://t.me/botfather)

Contoh berkas `.env`:

```.env

TOKEN='100000:BBB....q'
```

Build container image:

```bash
cd tanyahukum-bot
docker build -t user/qa-bot .
```

Jalankan container:

```
docker run --name "qa_bot_container" -e "TOKEN=100000:BBB....q" -d user/qa-bot
```

## Pemasangan dengan `docker-compose`

Buat berkas `.env` dan isi dengan token telegram bot. Token telegram bot dapat diminta dari [https://t.me/botfather](https://t.me/botfather)

Contoh berkas `.env`:

```.env

TOKEN='100000:BBB....q'
```

Build container image:

```bash
cd tanyahukum-bot
docker-compose up -d
```

## Pemasangan pada heroku

```.env

TOKEN='100000:BBB....q'
```

Build container image:

```bash
cd tanyahukum-bot
heroku create
heroku config:set TOKEN=100000:BBB....q
git push heroku main
```