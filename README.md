# TechIT Website Repository
## Virtualenv Setup
step 1) Make sure you have python(and pip) installed in your system
step 2) Upgrade pip using **pip install --upgrade pip**
step 3) To Install Virtualenv type
        - Windows: **python -m pip install virtualenv**
        - Mac: **python3 -m pip install virtualenv**
step 4) Create a Virtualenv using
        - Windows: **python -m venv TechITEnv**
        - Mac: **python3 -m venv TechITEnv**
step 5) Activate virtualenv
        **cd TechITEnv**
        - Windows: **Scripts\activate**
        - Mac: **source bin/activate**
step 6) Clone git repo with **git clone https://github.com/TechIT-Developer-Community/website.git**
step 7) Install Packages with
        - Windows: **python -m pip install -r website\requirements.txt**
        - Mac: **python3 -m pip install -r website/requirements.txt**

## Start local development server
step 1) Go to TechITEnv\website\techit\Settings.py File
step 2) Comment(as required by you)
        - import django_heroku
        - SECRET_KEY = os.environ.get("secret_key")
        - AWS_ACCESS_KEY_ID = os.environ.get("aws_access_key_id")
        - AWS_SECRET_ACCESS_KEY = os.environ.get("aws_secret_access_key")
        - AWS_STORAGE_BUCKET_NAME = os.environ.get("aws_storage_bucket_name")
        - AWS_S3_FILE_OVERWRITE = False
        - AWS_DEFAULT_ACL = None
        - DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
        - AWS_S3_REGION_NAME = 'ap-south-1'
        - AWS_S3_ADDRESSING_STYLE = 'virtual'
        - AWS_S3_SIGNATURE_VERSION = 's3v4'
        - django_heroku.settings(locals())
step 3) Comment out **SECRET_KEY = 'django-insecure-g+mu#9h=anaz^#yyq#c03xqd^=6kcp@+j1=%n2px_=smy-#k1v'**
step 4) Set **DEBUG = True**
step 5) Go to TechITEnv\website\
step 6) Run 
        - windows: **python manage.py runserver**
        - mac: **python3 manage.py runserver**
step 7) Go to **http://127.0.0.1:8000**
step 8) PEACE V_V