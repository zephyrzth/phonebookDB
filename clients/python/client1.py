import requests
import os
import json

# dari file testing.txt
#untuk melihat daftar phonebook
# curl -X GET http://localhost:32000/phones
#untuk membuat record di phonebook
#  curl -X POST http://localhost:32000/phones  \
#  -d '{"nama": "Edinson Cavani", "alamat" : "Uruguay", "notelp": "781723"}' \
#  -H "Content-Type: application/json" \
#untuk mendapatkan detail record dengan berbasis id
# curl -X GET http://localhost:32000/phones/fe437958-2fa4-11eb-bf35-7fc0bd24c845
#
#untuk menghapus record dengan berbasis id
# curl -X DELETE http://localhost:32000/phones/fe437958-2fa4-11eb-bf35-7fc0bd24c845
#
#unutk mengupdate record dengan berbasis id
#  curl -X PUT http://localhost:32000/phones/fe437958-2fa4-11eb-bf35-7fc0bd24c845 \
#  -H 'Content-type: application/json' \
#  -d '{"nama": "Bruno Fernandes"}'

BASEURL = os.getenv("BASEURL") or 'http://localhost:32000'

def phonebook_list():
    #untuk melihat daftar isian phonebook menggunakan method GET
    URI=f"{BASEURL}/phones"
    r = requests.get(URI)
    #karena format kembalian dalam bentuk JSON, gunakan langsung method json yang telah disediakan
    #library requests
    if (r.status_code!=200):
        return "Gagal"
    else:
        try:
            data = r.json()['data']
            return [(row['id'],row['data'])  for row in data]
        except:
            return "Gagal"

def phonebook_detail(id=None):
    if (id is None):
        return False
    URI=f"{BASEURL}/phones/{id}"
    r = requests.get(URI)
    if (r.status_code!=200):
        return "Gagal"
    else:
        try:
            data = r.json()['data']
            mystring=f"""
            Detail data dari ID : {id} Adalah:
            
            Nama : {data['nama']}
            Alamat: {data['alamat']}
            No Telp: {data['notelp']}
            """
            return mystring
        except:
            return "Gagal"

def phonebook_add(nama='Kosong',alamat='Kosong',notelp='Kosong'):
    the_data=dict(nama=nama,alamat=alamat,notelp=notelp)
    URI=f"{BASEURL}/phones"
    #untuk keperluan ini, menggunakan data dalam bentuk json
    r = requests.post(URI,json=the_data)
    if (r.status_code!=200):
        return "Gagal"
    else:
        return r.content

if __name__=='__main__':
    #memperlihatkan daftar phonebook
    for i in phonebook_list():
        print(i)
    #memperlihatkan data detail dari record dengan id  fe437958-2fa4-11eb-bf35-7fc0bd24c845
    print(phonebook_detail('f7b4c656-2fab-11eb-bf35-7fc0bd24c845'))
    #tambah data
    phonebook_add('Jonathan Spector','Kedurus','123456')
    #cek kembali, memperlihatkan daftar phonebook
    for i in phonebook_list():
        print(i)

