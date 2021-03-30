# 개요

## 목적
- django를 이용한 auto trading system 구축.

## 실행환경 및 라이브러리
- Python : 3.8.7
- django : 3.0.2
- os : windows10, windows server 2019
- 각 라이브러리는 requirements_org.txt 참조.

## 사용된 vscode 확장
- Python
- Jupyter
- Pylance
- Python Extended
- Python Docstring Generator

# 프로젝트 세팅법
## 32bit 가상화 (cmd)
- 프로젝트 디렉토리에서 수행
python -m venv Py387_32
- pyenv.cfg 파일 수정
home = C:\Users\user\AppData\Local\Programs\Python\Python38-32
include-system-site-packages = false
version = 3.8.7
- 활성화
cd (프로젝트 디렉토리 경로)\VirtualEnv\Py387_32\Script
activate
- 라이브러리 설치
pip install blockchain
pip install django

## Django 프로젝트 생성 (cmd)
- 32bit 환경으로 변경
'32bit 가상화'의 활성화 부분 참고.
- 프로젝트 디렉토리에서 수행
VirtualEnv\Py387_32\Scripts\django-admin.exe startproject auto_trade_web
- app 생성
cd auto_trade_web
python manage.py startapp application
- 실행
python auto_trade_web\manage.py runserver 8080
- vscode 실행은 .vscode 폴더의 launch.json 참고 (settings.json을 참고하여 32bit 환경으로 실행되도록 수정.)