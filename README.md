## PowerShell에서 권한풀기
Set-ExecutionPolicy Unrestricted

## 파이썬 가성환경
python -m venv venv

## activate : 활성화  / deactivate : 비활성화
venv/Scripts/activate

## 장고 설치
pip install django
pip install djangorestframework

## 장고 버전 확인
django-admin --version

## 장고 프로젝트 생성
django-admin startproject config .

## 개발용 서버 실행 명령어
python manage.py runserver

## 새로운 프로그램 패키지 만들기
python manage.py startapp burgers

## 프로그램 패키지 적용
python manage.py migrate

## 설치된 항목
pip list

python manage.py startapp(앱이름)
python manage.py createsuperuser : 관리자계정 생성

python manage.py makemigrations
python manage.py migrate
-> 데이터베이스 수정 후 사용

python manage.py runserver : 서버 실행

## Burger 클래스의 마이그레이션

## 1. 마이그레이션 파일 생성
python manage.py makemigrations burgers

## 2. 마이그레이션 파일을 데이터베이스에 적용
python manage.py migrate burgers

## 3. 데이터베이스 변경사항 생성
python manage.py makemigrations

## 4. 생성되어 있는 데이터베이스 변경사항 적용
python manage.py migrate

## 5. 장고에서 이미지(ImageField)를 다루려면 Pillow 설치 필
pip install Pillow
pip install 'Pillow<10'   # 10버전미만 서
>> 에러 로그
(venv) PS D:\006. 프로젝트\004. 개인 프로젝트\029. Python_Django> python manage.py makemigrations
SystemCheckError: System check identified some issues:

ERRORS:
blog.Post.thumbnail: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".


## 장고 Admin 계정 생성
python manage.py createsuperuser

## 장고 python shell
python manage.py shell

## python amdin 아이디
admin // admin
