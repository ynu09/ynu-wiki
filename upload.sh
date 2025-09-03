#!/bin/bash

# 현재 상태 확인
git status

# 소스 코드 커밋 & 푸시
git add .
git commit -m "update"
git push origin master

# mkdocs 웹사이트 배포
mkdocs gh-deploy
