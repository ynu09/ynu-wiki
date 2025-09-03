# 나만의 웹사이트 제작

## <h2 style="font-weight: 900;">1️⃣mkdocs 프로젝트 생성</h2>

### mkdocs 설치

    $ pip3 install mkdocs mkdocs-material
    $ mkdocs --version

### 새 mkdocs 프로젝트 생성

    $ mkdocs new 프로젝트명
    $ cd 프로젝트명

<img src="/ynu-wiki/images/website/project-1.png" width="450"/>

- 프로젝트 생성 시, 폴더 안에 기본 구조가 생성됩니다. 

        mysite/
            mkdocs.yml # 사이트 설정 파일
            docs/
                index.md # 사이트 작성 파일 (마크다운 ; 노션 느낌) 

    <img src="/ynu-wiki/images/website/project-2.png" width="270"/>

### 로컬(내 PC)에서 사이트 확인

```$ mkdocs serve```

<img src="/ynu-wiki/images/website/serve.png" width="800"/>

페이지 수정사항을 실시간으로 확인할 수 있습니다.

## <h2 style="font-weight: 900;">2️⃣GitHub 저장소 생성</h2>

### GitHub 처음 사용하는 경우, 토큰 생성 

[https://blog.pocu.academy/ko/2022/01/06/how-to-generate-personal-access-token-for-github.html](https://blog.pocu.academy/ko/2022/01/06/how-to-generate-personal-access-token-for-github.html)

### Repository 만들기

1. GitHub 접속 → New Repository
2. 이름 입력 (예: ynu-wiki)

    <img src="/ynu-wiki/images/website/github-1.png" width="600"/>

3. 생성 후, 깃허브 사이트 적어두기 (예: https://github.com/ynu09/ynu-wiki.git)

## <h2 style="font-weight: 900;">3️⃣프로젝트 GitHub 연결</h2>

### 사용자 정보 설정

    $ git config --global user.name ynu09
    $ git config --global user.email xxxxx@gmail.com
    $ git config -l
        user.name=ynu09
        user.email=xxxxx@gmail.com

### 깃허브 연결
프로젝트 파일에 들어가서 진행합니다. (예: $ cd ynu-wiki)  
사이트 주소는 <span style="color: red;">'2️⃣GitHub 저장소 생성-Repository 만들기'</span>에서 적어둔 주소입니다. 

    $ git init 
        # 처음 한번만 (초기세팅) 
        # Initialized empty Git repository in /home/ymo/ynu-wiki/.git/
    $ git add . 
        # 생성/수정한 파일들 추가
    $ git commit -m "update" 
        # [master (root-commit) d27299a] update
    $ git branch -M master
    $ git remote add origin https://github.com/USERNAME/mysite.git 
    $ git push origin master

### GitHub Pages 배포 설정
아래 명령어를 입력하면 docs 내용 빌드 및 gh-pages를 branch로 푸시합니다. 

```$ mkdocs gh-deploy```

- 적용됐는지 확인합니다. 
    
    ![github-2](/ynu-wiki/images/website/github-2.png)  
    ![github-3](/ynu-wiki/images/website/github-3.png)  

## <h2 style="font-weight: 900;">4️⃣웹사이트 작성</h2>

### 뼈대 만들기

1. mkdocs.yml 수정  
    
    : 목차가 생성됩니다.

        site_name: Ynu Wiki
        site_url: https://ynu09.github.io/ynu-wiki/ # 이미지 경로 영향
        theme:
        name: material
        palette:
            primary: 'brown'
        logo: '/ynu-wiki/images/24.png' # 로고 이미지 경로

        nav:
        - 홈: index.md
        - Ubuntu: 
            - Virtual Box 세팅: ubuntu/virtual_box.md
            - Ubuntu 세팅: ubuntu/setting.md
        - Website: website.md

    - site_url을 지정해야 이미지 경로를 다음과 같이 작성할 수 있습니다.  
    예: <span style="color: red;">/ynu-wiki</span>/images/ubuntu/hangul.png

    - palette-primary는 사이트 색상입니다. 
    - logo는 사이트를 상징할 로고입니다. 이미지 경로를 지정해주면 됩니다. 
    - nav는 목차를 생성해주는 부분입니다. 각 페이지의 경로를 지정해줍니다. 

2. docs/index.md 수정 

    : 메인홈 내용을 작성합니다. 

        # 연우의 지식창고🧠

        안녕하세요!  
        24년동안 모은 다양한 지식과 자료를 정리한 공간입니다👋🏻

        <img src="/ynu-wiki/images/24.png" alt="24" width="200"/>

        ### 카테고리 

        - Ubuntu(Virtual Box)
        - 나만의 웹사이트 제작

        ---

        > "지식을 기록하고 공유하면, 더 많은 아이디어와 성장으로 돌아온다"  
        > "모르면 ChatGPT한테 적극적으로 물어보자"  
        > – 연우 
    
    - '#' 는 가장 큰 제목, '##'는 중간 제목, '###'는 작은 제목입니다.
    - '---'는 구분선입니다. 
    - 이미지 경로에서 'alt'는 이미지 이름이며, width로 크기를 조절할 수 있습니다. 

### 내용 만들기 
1. docs 폴더 내에 모델별로 폴더를 만듭니다. 
    
    예: go2, g1, z1
    
2. 각 모델 폴더별로 .md 파일을 작성합니다.

        ├── docs
        │  ├── index.md # 메인 페이지: 홈
        │  ├── g1
        │  │   ├── develop_manual.md # 개발 가이드
        │  │   ├── education.md # 납품교육 - 조종기/앱

### 수정한 내용 업데이트 
1. shell script 파일 만들기
    
    ```$ nano upload.sh```

2. upload.sh 파일에 내용 입력

        #!/bin/bash

        # 현재 상태 확인
        git status

        # 소스 코드 커밋 & 푸시
        git add .
        git commit -m "update"
        git push origin master

        # mkdocs 웹사이트 배포
        mkdocs gh-deploy

3. 권한 주기

    ```$ chmod +x upload.sh```

4. 스크립트 실행

    ```$ ./upload.sh```