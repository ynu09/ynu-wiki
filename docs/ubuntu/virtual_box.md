# Virtual Box 환경 준비 

## <h2 style="font-weight: 900;">1️⃣Ubuntu Image 다운로드</h2>

1. 아래 링크로 접속합니다.  

    [🔗https://releases.ubuntu.com/focal/](https://releases.ubuntu.com/focal/)

2. Desktop image(64-bit PC (AMD64) desktop image)를 다운로드합니다.

---

## <h2 style="font-weight: 900;">2️⃣Virtual Box 설치</h2>

1. 아래 링크로 접속합니다.

    [🔗https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)

2. Windows hosts를 클릭해서 설치 파일을 받습니다.

    ![VB 설치 이미지](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FJa7Lw%2FbtsPgBdgBGu%2FAAAAAAAAAAAAAAAAAAAAAE_FAgxUpmvCgeyWlqDmJYX4Isc556c2Mr0Reqs71e0y%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1759244399%26allow_ip%3D%26allow_referer%3D%26signature%3DfRRfwOmtXnV4wlA3mTNOBj%252BRH1I%253D)

3. Virtual Box와 Extension Pack을 설치합니다. (파일 더블클릭)

    ![VB 설치 이미지2](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcBm4jT%2FbtsPgZrwNGP%2FAAAAAAAAAAAAAAAAAAAAAEmNaIzFFsXBj5Z0hWZBRG41ZLEV8cvk8sPyZvAFBmnF%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1759244399%26allow_ip%3D%26allow_referer%3D%26signature%3DBr7OcS4xTmljFH%252Fl%252BIKb0kRT1aU%253D)

---

## <h2 style="font-weight: 900;">3️⃣Virtual Box에 Ubuntu 설치</h2>

### 참고 사이트
[1] [Virtual Box 에 Ubuntu 20.04 LTS 설치하기](https://truelifer.medium.com/virtual-box-%EC%97%90-ubuntu-20-04-lts-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-71ab044eb4f8)  
[2] [Oracle VM VirtualBox에 Ubuntu 22.04 LTS 설치하기](https://powerdeng.tistory.com/254)  
[3] [[Virtualbox] 화면 크기 조절](https://changun516.tistory.com/144)

1. '새로 만들기(N)'를 클릭합니다.
2. 가상환경 이름을 지어주고, OS, OS Distribution, OS Version이 사진과 같이 설정됐는지 체크합니다.  

    ⚠️ <span style="color: red;">가상환경 이름 작성 시, 빈칸이 없도록 합니다!</span>

    <img src="/ynu-wiki/images/ubuntu/install-1.png" width="650"/>

3. 설정이 끝났으면 '완료(F)' 버튼을 누릅니다. 
4. Oracle VM VirtualBox에서 설정 버튼을 클릭하여 이후 과정을 진행합니다.

    - '저장소'에서 컨트롤러 IDE 밑에 비어있음을 클릭합니다.
    - 광학 드라이브의 아이콘을 눌러 가상 광학 디스크 선택/만들기를 선택합니다.
            
        <img src="/ynu-wiki/images/ubuntu/install-2.png" width="650"/>

    - 추가 버튼을 누른 뒤 다운받은 ISO파일을 선택합니다.
    - '디스플레이'에서 'Graphics Controller'를 'VBoxVGA'로 변경합니다.(화면 크기 조정)  
         
        <img src="/ynu-wiki/images/ubuntu/install-3.png" width="650"/>

        이후 가상화면 접속 후, '보기-가상화면1’에서 크기 조정 가능합니다.  

5. Oracle VM VirtualBox에서 '시작' 버튼을 클릭하여 Ubuntu를 설치합니다.