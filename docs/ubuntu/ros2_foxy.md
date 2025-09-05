# ROS2 Foxy

## <h2 style="font-weight: 900;">1️⃣Foxy 설치</h2>

공식 설치 가이드: [🔗https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)

1. 버전 확인

        $ echo $ROS_DISTRO
        foxy


2. 기본 테스트 - 노드 통신 

    <span style="color: red;">ros2 run [패키지명] [실행파일명]</span> 

    ![기본테스트](/ynu-wiki/images/ubuntu/basic_test.png)
    
    - 패키지: 노드들의 묶음 
    - 노드: 독립된 프로그램

        ```$ ros2 node list```   
        
        → 현재 실행중인 노드 이름 확인(예: /turtlesim)

        ```$ ros2 node info [노드명]```   

        → 현재 실행중인 노드 정보 확인
    
    - publisher(talker): 정보 보내는 자
    - subscriber(listener): 정보 받는 자

3. 통신 방식 3가지

    1. Topic(msg): publisher-subscriber

        ```$ ros2 topic list```

    2. Service(srv)

        ```$ ros2 service list```

        - 행동 요청 ↔ 결과 반환

    3. Action

        ```$ ros2 action list``` 
        
        - feedback 존재 

---

## <h2 style="font-weight: 900;">2️⃣bashrc 설정</h2>

![bashrc](/ynu-wiki/images/ubuntu/bashrc.png)

1. foxy 환경설정 스크립트 소싱 

        $ gedit ~/.bashrc (수정)
        
        source /opt/ros/foxy/setup.bash 추가
        
        $ source ~/.bashrc (적용)

2. 자주 쓰는 단축키 등록

        $ gedit ~/.bashrc (수정)
        
        alias gr='gedit ~/.bashrc' 추가
        alias nr='nano ~/.bashrc' 추가
        alias sr='source ~/.bashrc' 추가
        
        $ source ~/.bashrc (적용)

---

## <h2 style="font-weight: 900;">3️⃣turtlesim</h2>

1. turtlesim 설치 (ROS2 설치 시 이미 설치됐을 수 있음)

        $ sudo apt update
        $ sudo apt install ros-foxy-turtlesim

2. 설치된 패키지 확인 

        $ ros2 pkg executables turtlesim 
        
        turtlesim draw_square
        turtlesim mimic
        turtlesim turtle_teleop_key
        turtlesim turtlesim_node

3. 실행

    <img src="/ynu-wiki/images/ubuntu/turtlesim.png" width="300"/>

        # 터미널1 (프로그램 실행)
        $ ros2 run turtlesim turtlesim_node

        # 터미널2 (키보드 조작)
        $ ros2 run turtlesim turtle_teleop_key

---

## <h2 style="font-weight: 900;">4️⃣rqt</h2>

실행: ```$ rqt```

---

## <h2 style="font-weight: 900;">5️⃣WS/Package 만들기</h2>

![package](/ynu-wiki/images/ubuntu/package.png)

---

1. ws 생성
: 테스트로 workspace 이름을 'test_ws'로 지정한다. 

    ```$ mkdir -p /test_ws/src``` 

2. pkg 생성

        $ cd ~/test_ws/src
        
        # Python 
        $ ros2 pkg create --build-type ament_python <package_name>

        # C++
        $ ros2 pkg create --build-type ament_cmake <package_name>

3. 생성한 pkg들 빌드

    1. 전체 빌드

            $ cd ~/test_ws
            $ colcon build --symlink-install 
    
    2. 하나의 패키지만 빌드

            $ cd ~/test_ws
            $ colcon build --packages-select <package_name>

    3. 패키지 구성 확인

            $ cd ~/test_ws/src/<package_name>
            $ ls
                package.xml  resource  setup.cfg  setup.py  test  <package_name>

4. setup 파일 소싱

        $ cd ~/test_ws
        $ ls
            build install log src
        
        $ source install/setup.bash