Analytic Deployment Model

Data yang digunakan adalah dataset Credit Scoring. Dari data tersebut dilakukan klasifikasi menggunakan algoritma Random Forest untuk menentukan apakah seorang customer di bulan berikutnya akan terlambat bayar atau tidak. Variabel yang digunakan adalah:
1. Limit Balance,
2. Pembayaran Pertama (0 = tidak terlambat, 1 = terlambat 1 bln, dst),
3. Pembayaran Kedua (0 = tidak terlambat, 1 = terlambat 1 bln, dst)

Adapun model klasifikasi tersebut disimpan pada model_randomforest.pkl yang dijalankan pada Flask_app.py
Kemudian untuk menggunakan model tersebut pada data baru, kita menggunakan request.py.
