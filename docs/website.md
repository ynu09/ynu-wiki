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