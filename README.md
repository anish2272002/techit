# TechIT Website Repository
## Virtualenv Setup
step 1) Make sure you have python(and pip) installed in your system <br/>
step 2) Upgrade pip using **pip install --upgrade pip** <br/>
step 3) To Install Virtualenv type <br/>
        - Windows: **python -m pip install virtualenv** <br/>
        - Mac: **python3 -m pip install virtualenv** <br/>
step 4) Create a Virtualenv using <br/>
        - Windows: **python -m venv TechITEnv** <br/>
        - Mac: **python3 -m venv TechITEnv** <br/>
step 5) Activate virtualenv <br/>
        **cd TechITEnv** <br/>
        - Windows: **Scripts\activate** <br/>
        - Mac: **source bin/activate** <br/>
step 6) Clone git repo with **git clone https://github.com/TechIT-Developer-Community/website.git** <br/>
step 7) Install Packages with <br/>
        - Windows: **python -m pip install -r website\requirements.txt** <br/>
        - Mac: **python3 -m pip install -r website/requirements.txt** <br/>

## Start local development server <br/>
step 1) Go to TechITEnv\website\techit\Settings.py File <br/>
step 2) Comment(as required by you) <br/>
        - import django_heroku <br/>
        - SECRET_KEY = os.environ.get("secret_key") <br/>
        - AWS_ACCESS_KEY_ID = os.environ.get("aws_access_key_id") <br/>
        - AWS_SECRET_ACCESS_KEY = os.environ.get("aws_secret_access_key") <br/>
        - AWS_STORAGE_BUCKET_NAME = os.environ.get("aws_storage_bucket_name") <br/>
        - AWS_S3_FILE_OVERWRITE = False <br/>
        - AWS_DEFAULT_ACL = None <br/>
        - DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage" <br/>
        - AWS_S3_REGION_NAME = 'ap-south-1' <br/>
        - AWS_S3_ADDRESSING_STYLE = 'virtual' <br/>
        - AWS_S3_SIGNATURE_VERSION = 's3v4' <br/>
        - django_heroku.settings(locals()) <br/>
step 3) Comment out **SECRET_KEY = 'django-insecure-g+mu#9h=anaz^#yyq#c03xqd^=6kcp@+j1=%n2px_=smy-#k1v'** <br/>
step 4) Set **DEBUG = True** <br/>
step 5) Go to TechITEnv\website\ <br/>
step 6) Run <br/>
        - windows: **python manage.py runserver** <br/>
        - mac: **python3 manage.py runserver** <br/>
step 7) Go to **http://127.0.0.1:8000** <br/>
step 8) PEACE V_V <br/>