# Ubuntu 세팅

## <h2 style="font-weight: 900;">1️⃣한글키 입력 활성화</h2>

### 참고 사이트
[🔗[Ubuntu 20.04] 우분투 한글입력 방법 (한글키 호환)](https://freeablelab.tistory.com/138) 

1. 다음 명령어를 입력하여 업그레이드 및 재부팅합니다.

        $ sudo apt update
        $ sudo apt upgrade ibus-hangul
        $ reboot 

2. 우분투 '설정' > '지역 및 언어' > '입력 소스' > '+' 에 들어가서 '한국어'에서 '한국어(Hangul)'을 찾아 추가합니다. 

3. '한국어(Hangul)' 옆에 톱니바퀴를 눌러서 한영전환키에 '한영키(Alt_R)'를 추가해줍니다.  
    '추가' 누르고 한영키 누르면 추가됩니다.  
    <img src="/ynu-wiki/images/ubuntu/hangul.png" width="350"/>

4. 재부팅 후, 한글과 영문 전환이 잘 되는지 확인합니다. 

## <h2 style="font-weight: 900;">2️⃣필요한 패키지 설치</h2>

1. VScode 설치

    - .deb 형식의 VScode를 다운받습니다.  
        
        [🔗https://code.visualstudio.com/download](https://code.visualstudio.com/download)

    - Downloads 폴더로 들어가 다운받은 .deb 파일을 설치합니다.

        ```$ sudo dpkg -i code_xxxxx_amd64.deb```
    
2. Terminator 설치 

        $ sudo apt update
        $ sudo apt install terminator -y

3. Chrome 설치

    - Downloads 폴더로 들어가 다운받은 .deb 파일을 설치합니다.

            $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
            $ sudo apt install ./google-chrome-stable_current_amd64.deb

4. Tree 설치(폴더 구조 확인용)  
    
    ```$ sudo apt install tree```

5. python, pip, git 라이브러리 설치

        $ sudo apt update
        $ sudo apt install python3 python3-pip git -y

    - 확인

            $ python3 --version
            $ pip3 --version
            $ git --version

6. Gazebo 설치

        $ sudo apt update
        $ sudo apt install ros-foxy-gazebo-ros-pkgs

        # 실행
        $ gazebo
