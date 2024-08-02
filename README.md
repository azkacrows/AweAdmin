# AweAdmin

## Deskripsi Proyek

AweAdmin adalah sebuah skrip sederhana yang ditulis dalam bahasa Python untuk menemukan admin panel pada situs web. Skrip ini melakukan bruteforce pada direktori yang mungkin dan mengembalikan kode respons HTTP. Anda dapat menambahkan direktori Anda sendiri dengan mengedit file "dir".

## Penggunaan

Gunakan skrip ini dengan hati-hati dan hanya untuk tujuan pembelajaran. Saya tidak bertanggung jawab atas segala kerusakan atau pelanggaran hukum yang mungkin terjadi akibat penggunaan skrip ini.

### Perintah

- `-t`, `--target`   - Target web server, misalnya "contoh.com"
- `-v`, `--verbose`  - Mengaktifkan mode verbose
- `-h`, `--help`     - Memunculkan bantuan

### Contoh Penggunaan

Jalankan perintah berikut untuk menjalankan skrip:

```sh
python AweAdmin.py -t targetsite.com -v
```

## Struktur Proyek

- `AweAdmin.py`
- `dir`
- `README.md`

### Penjelasan File

#### `AweAdmin.py`

File utama yang berisi logika untuk melakukan bruteforce direktori dan mengembalikan kode respons HTTP.

#### `dir`

File ini berisi daftar direktori yang akan dicoba oleh skrip. Anda dapat menambahkan direktori Anda sendiri dengan mengedit file ini.

#### `README.md`

File ini berisi deskripsi proyek, instruksi penggunaan, dan peringatan.

## Peringatan

Skrip ini dibuat hanya untuk tujuan pembelajaran dan penelitian. Penggunaan skrip ini pada situs web tanpa izin adalah ilegal dan dapat menyebabkan masalah hukum. Saya tidak bertanggung jawab atas segala kerusakan, pelanggaran hukum, atau konsekuensi lain yang mungkin terjadi akibat penggunaan skrip ini.

**Date**: Apr 6, 2019
