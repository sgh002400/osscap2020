## 2020 오픈소스 프로젝트
## Smart Alarm / 스마트 알람


#### 간단한 실행 안내
1. 프로그램 실행 순서는 01_face_dataset.py, 02_face_training.py, SmartAlarmLED.py를 순서대로 실행시켜야한다. 
2. 01_face_dataset.py로 자신의 번호를 입력한 뒤 카메라를 응시하여 얼굴 데이터를 jpg파일로 저장한다.
3. 02_face_training.py로 위 이미지를 학습시킨다. 
4. SmartAlarmLED.py에선 알람시계기능과 LED Matrix에 UI를 띄우는 역할을 한다. 이후 알람시간이 되면 얼굴이 인식된 후 ESC를 누를때까지 알람이 울리게 만들었다.

### Installing / 설치, 사용

- Open CV (http://www.3demp.com/community/boardDetails.php?cbID=235)
- opencv-python
- Numpy
- os
- Pi-camera (https://blog.naver.com/ljy9378/221431122137)
- 3.5mm speaker
- Pygame
```
$ sudo apt install python3-pip
$ pip3 install pygame
```

### Running the tests / 테스트의 실행
-구체적인 실행 안내

```
$ sudo raspi-config
```
1. System Options -> S2 Audio -> 1 Headphones
> 외장 스피커를 사용하므로 raspi 초기설정을 위와 같이 해줘야한다.

2. Camera -> enabled 
> 카메라 작동시에 첫번째는 잘 작동되지만, 두번째 시도 떄 Assertion failed 오류가 뜬다면 ``` $ sudo modprobe bcm2835-v4l2 ```를 입력하고 ``` $ sudo nano /etc/modules ```를 입력한 후 해당 파일 내의 맨 마지막 줄에 bcm2835-v4l2를 입력한 후 저장하면 해결 된다.

```
$ git clone https://github.com/sgh002400/osscap2020.git
```

```
$ cd osscap2020/final
```

```
$ python3 01_face_dataset.py
```
> enter user id end press <return> ==>     
  숫자 id를 입력하고 카메라에 얼굴을 대고있으면 OpenCV의 haarcascades가 카메라를 통해 사용자 얼굴을 인식하여 카메라 화면을 캡쳐하고 이를 dataset directory에 jpg파일로 저장한다.   
  인식의 정확도를 높이기 위해 얼굴과 카메라의 거리나 각도를 약간씩 움직이면서 30장을 찍는다. id 1, 2는 이미 표본이 존재하므로 3부터 입력을 권장한다.

```
$ python3 02_face_training.py
```
>  dataset directory의 jpg 파일들을 불러와 학습시킨 후 결과를 trainer directory에 trainer.yml 파일로 저장시킨다.

```
$ python3 SmartAlarmLED.py
```
>    Please input user name(Juyoung / Myungjin / Professor / Juhyung / Giljin):      
  사용자 이름을 괄호에 나와있는 철자로 입력한다.  
  
>    1.Set alarm   2.Set alarm tone  3.Set alarm size   4. Exit      
  1.알람시간 설정, 2.알람노래 설정, 3.알람크기 설정, 4.종료

-    1 (Set alarm)    
     HOUR (24 hour time): 0에서 24 사이의 정수를 입력한다.      
     MINUTE : 0에서 60 사이의 정수를 입력한다. (0에서 9일 경우 앞에 0을 붙이면 안된다)      
     시간범위를 초과한 정수를 넣으면 다시 입력해야한다.    
     알람이 울림과 동시에 카메라가 켜지며, 얼굴이 인식될 때까지 알람이 울리게된다.    
     알람이 울리기전에 입력해둔 사용자의 이름(user_name)과 face_recognition함수에서 인식된 얼굴의 이름(return_name)이 일치하면 ESC를 눌렀을 때 알람이 꺼진다.   
     만약 user_name != return_name -> ESC를 누르면 카메라는 다시작동되고 알람도 계속 울린다.

-    2 (Set alarm tone)   

     1. K-pop 1  2. K-pop 2  3. Miliatary   
     Select the alarm sound: 알람음을 1~3 사이의 정수로 입력한다.
    
-    3 (Set alarm size)   
      Please enter the size of the alarm: 알람음의 크기를 0~10사이의 정수로 입력한다.

-    4 (Exit)   
      알람 프로그램을 종료시킨다.

### Note / 시연시 참고사항
- 01_face_dataset.py에서 id는 김강희 교수님,주영 조교님, 길진 조교님 순서대로 3~5번입니다.
- 사용자 이름에서 강희 교수님은 Professor, 주영 조교님은 Juhyung, 길진 조교님은 Giljin입니다.
- 유의사항 1: 얼굴을 찍을때 찍는 사람의 헤어스타일에 따라 인식이 달라질 정도로 헤어스타일은 큰 비중을 차지하고 있다. 여러 사용자 중 자신과 비슷한 헤어스타일을 가진 사람이 있다면 인식할 때 왔다갔다하며 헷갈려한다. 그러니 자신의 헤어스타일에 유의하며 찍어야한다.
- 유의사항 2: 사진을 찍은 곳에서 장소를 이동시키지 않는게 좋다. haarcascades 알고리즘은 얼굴 주위의 명암 차이를 저장하여 누군지 알아보는 것이기에 사진 찍은 곳에서의 조명 아래에서 테스트를 해야 사용자를 좀 더 잘 인식할 수 있다.
