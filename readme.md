# 개요

## 목적
- django를 이용한 auto trading system 구축.

## 실행환경 및 라이브러리
- Python : 3.8.7
- django : 3.1.7
- os : windows10, windows server 2019
- 각 라이브러리는 requirements.txt 참조.

## 사용된 vscode 확장
- Python
- Jupyter
- Pylance
- Python Extended
- Python Docstring Generator

# 프로젝트 세팅법
## 환경변수 등록
C:\(유저 디렉토리 경로)\AppData\Local\Programs\Python\Python38

## 라이브러리 일괄 설치
```
pip install -r requirements.txt
```

## (선택) vscode 설정
```
(settings.json)
"python.pythonPath": "C:\\(유저 디렉토리 경로)\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"

(launch.json)
"configurations": [
    {
        "name": "Python: Django",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}\\auto_trade_web\\manage.py",
        "args": [
            "runserver",
            "--noreload",
            "8080",
        ],
        "django": true
    }
]
```

## 32bit 가상화 (cmd)
- 프로젝트 디렉토리에서 수행
```
mkdir VirtualEnv
cd VirtualEnv
python -m venv Py387_32
```
- pyenv.cfg 파일 수정
```
home = C:\(유저 디렉토리 경로)\AppData\Local\Programs\Python\Python38-32
include-system-site-packages = false
version = 3.8.7
```
- 활성화
```
cd (프로젝트 디렉토리 경로)\VirtualEnv\Py387_32\Scripts
activate
```
- 라이브러리 설치
```
pip install blockchain==1.4.4
```

## Django 프로젝트 생성 (cmd)
- 프로젝트 디렉토리에서 수행
```
django-admin startproject auto_trade_web
```
- app 생성
```
cd auto_trade_web
python manage.py startapp application
```
- 실행
```
python auto_trade_web\manage.py runserver 8080
```
- mysql setting
auto_trade_web\auto_trade_web\db_settings.py.sample 파일을 복사 후 이름을 변경해 db_settings.py를 만들고 설정 변경.
- 마이그레이션
sql 폴더내의 schema.sql로 스키마 생성 후 auto_trade_web 경로에서 python manage.py migrate 실행