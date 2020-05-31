## Requirements
Python 3.7.6  
xgboost==1.0.2  
ipython==7.13.0 
pandas==1.0.3 
numpy==1.18.2 
scipy==1.4.1  
scikit-learn==0.22.1  
(Harusnya latest version juga bisa) 

Di test di 12 threads Ryzen 5 3600, 16 GB RAM 

Duration (H:M:S): 00:50:01  
Private Score : 0.00941 
Public Score : 0.01137  

## Data
Data Kaggle CouponPP : https://www.kaggle.com/c/coupon-purchase-prediction/data 
Masukkan data Kaggle ke dalam folder input, kecuali : prefecture_locations.csv, pakai BOM-removed version yg disediakan 

## Run
Atur jumlah thread yang mau digunakan (default 12) di file d01_create_xgbdata.py, line 32   
Run "ipython batch.py" di folder "src" untuk generate dataset, train xgb, lalu buat prediksi submission   
Setelah selesai, submission dan model XGB disimpan di folder submission 

## Note
Code asli threecourse pakai kombinasi XGB dan Vowpal Wabbit, namun disini hanya memakai XGB   
https://github.com/threecourse/kaggle-coupon-purchase-prediction  
