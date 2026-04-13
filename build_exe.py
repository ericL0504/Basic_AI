import PyInstaller.__main__
import os
import customtkinter

# Get the directory of customtkinter assets
ctk_path = os.path.dirname(customtkinter.__file__)

PyInstaller.__main__.run([
    'study_assistant.py',
    '--onefile',
    '--noconsole',
    '--name=AI_Study_Assistant',
    '--add-data', f"{ctk_path};customtkinter",
    '--icon=NONE', # 아이콘이 있다면 파일 경로 입력
    '--clean',
])

print("\n--- 빌드 완료! ---")
print("dist 폴더 안에 AI_Study_Assistant.exe 파일이 생성되었습니다.")
