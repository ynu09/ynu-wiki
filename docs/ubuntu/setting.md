# Ubuntu 세팅

### 참고 사이트
[1] [[Ubuntu 20.04] 우분투 한글입력 방법 (한글키 호환)](https://freeablelab.tistory.com/138) 

## <h2 style="font-weight: 900;">1️⃣한글키 입력 활성화</h2>

1. 다음 명령어를 입력하여 업그레이드 및 재부팅합니다.

        $ sudo apt update
        $ sudo apt upgrade ibus-hangul
        $ reboot 

2. 우분투 '설정' > '지역 및 언어' > '입력 소스' > '+' 에 들어가서 '한국어'에서 '한국어(Hangul)'을 찾아 추가합니다. 

3. '한국어(Hangul)' 옆에 톱니바퀴를 눌러서 한영전환키에 '한영키(Alt_R)'를 추가해줍니다.  
    '추가' 누르고 한영키 누르면 추가됩니다.  
    <img src="/ynu-wiki/images/ubuntu/hangul.png" width="350"/>
