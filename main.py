import pyautogui
import keyboard
import time

def read_config():
    # config txt 가져오기.
    with open("config.txt", "r", encoding="utf-8") as file:
        message = file.read().strip()
    return message

def main():
    message = read_config()
    running = True

    while running:
        if keyboard.is_pressed("F3"):
            # F3 키를 누르면 반복해서 입력.
            while True:
                keyboard.write(message)
                pyautogui.press('enter')
                time.sleep(0.1)  # 입력 간 딜레이.
                if keyboard.is_pressed("F4"):
                    # F4 키가 눌리면 반복을 중단.
                    break

if __name__ == "__main__":
    main()
