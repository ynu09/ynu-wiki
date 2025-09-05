# ROS2 Foxy

## <h2 style="font-weight: 900;">1️⃣Foxy 설치</h2>

[🔗https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)

- 기본 테스트

    ![기본테스트](/ynu-wiki/images/ubuntu/basic_test.png)

## <h2 style="font-weight: 900;">2️⃣bashrc 설정</h2>

![bashrc](/ynu-wiki/images/ubuntu/bashrc.png)

1. foxy 설정 스크립트 소싱 

        $ gedit ~/.bashrc
        
        source /opt/ros/foxy/setup.bash 추가
        
        $ source ~/.bashrc

2. 자주 쓰는 단축키 소싱

        $ gedit ~/.bashrc
        
        alias gr='gedit ~/.bashrc' 추가
        alias nr='nano ~/.bashrc' 추가
        alias sr='source ~/.bashrc' 추가
        
        $ source ~/.bashrc