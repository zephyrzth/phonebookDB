gunakan python3.8 atau yang lebih baru
buatlah dulu lingkungan virtual environment
1. virtualenv venv
2. source venv/bin/activate
3. anda sudah berada dalam linkungan virtualenv
4. jalankan instalasi modul pip install -r requirements
5. jalankan dengan python Service.py
6. lihatlah file testing.txt untuk testing

Untuk deployment, docker harus terinstall terlebih dahulu
membangun docker image
- docker build -t my-phonebook-service:latest .

menjalankan docker image menjadi docker container dengan nama PHONEBOOK
- docker run -d -p 32000:32000 --name PHONEBOOK my-phonebook-service:latest
