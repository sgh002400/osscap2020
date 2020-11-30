## 2020 오픈소스 프로젝트
## Smart Alarm / 스마트 알람


#### 간단한 실행 안내
1. 프로그램 실행 순서는 01_face_dataset.py, 02_face_training.py, SmartAlarmLED.py를 순서대로 실행시켜야한다. 
2. 01_face_dataset.py로 id를 입력한 뒤 카메라를 응시하여 얼굴 데이터를 저장한다.
3. 02_face_training.py로 위 이미지를 학습시킨다. 
4. SmartAlarmLED.py에선 알람시계기능과 LED Matrix에 UI를 띄우는 역할을 한다. 이후 알람시간이 되면 얼굴이 인식된 후 ESC를 누를때까지 알람이 울리게 만들었다.

### Installing / 설치, 사용

아래 사항들이 설치, 사용 되었습니다.
- Open CV (http://www.3demp.com/community/boardDetails.php?cbID=235)
- Python3
- Pygame
- opencv-python
- Numpy
- os
- Pi-camera
- 3.5mm speaker


### Running the tests / 테스트의 실행
-구체적인 실행 안내

- $sudo raspi-config
1. System Options -> S2 Audio -> 1 Headphones
> 외장 스피커를 사용하므로 raspi 초기설정을 위와 같이 해줘야한다.

2. Camera -> enabled
> 카메라 연결하는 것부터 찍기 시작한다. 첫번째는 잘 작동되지만, 두번째 시도 떄 Assertion failed 오류가 뜬다면 sudo modprobe bcm2835-v4l2를 입력하고, sudo nano /etc/modules를 입력한 후 맨 마지막 줄에 bcm2835-v4l2를 입력한 후 저장한다.

- $git clone https://github.com/sgh002400/osscap2020.git

- $cd osscap2020

- $cd final

- $python3 01_face_dataset.py
> 01_face_dataset.py를 실행시켜서 id를 입력한다. 김강희 교수님은 3번, 주영 조교님은 4번, 길진 조교님은 5번입니다. 숫자 id를 입력하고 카메라에 얼굴을 대고있으면 OpenCV의 haarcascades가 카메라를 통해 사용자 얼굴을 인식하여 img파일로 저장한다. 이때 카메라 화면은 뜨지 않으며 얼굴이 인식되어 저장된 이미지만 뜨게된다. 만약 카메라에 인식이 안되어 저장이미지가 안뜬다면 얼굴과 카메라의 거리나 각도를 약간씩 움직이면된다. 위 저장된 이미지를 통해 학습시켜야 하므로 우리는 30장을 저장시킵니다.

- $python3 02_face_training.py
> 02_face_training.py를 실행시키면 이미지 파일들을 불러와서 이를 recognizer.train()을 통해 학습시킨 후 결과를 recognizer.write()을 통해 trainer.yml 파일로 저장시킨다.

- $python3 SmartAlarmLED.py
> SmartAlarmLED.py을 실행시키면 LED matrix에 UI가 나오게 되며 번호를 통해 원하는 설정을 고를 수 있다. 1.알람시간설정, 2.알람노래설정, 3.볼륨크기설정, 4.종료로 되어있다.

>   > 1 - 1. 알람시간을 선택하면 사용자의 이름을 영문으로 입력하고 알람이 울릴 시간, 분을 입력한다. 이때 시간은 24, 분은 60 이상의 수를 넣으면 다시 입력한다. 그 후 time 모듈을 통해 현재시간을 가져온 후 설정한 시간과의 차이를 초로 바꾸어 time.sleep으로 설정시간때까지 기다린다. 이떄 설정한 시간은 LED matrix에서 ALARM 옆에 띄워진다. 사용자 이름에서 강희 교수님은 Professor, 주영 조교님은 Juhyung, 길진 조교님은 Giljin입니다.

>   > 1 - 2. time.sleep이 끝나면 03_face_recognition.py에서 face_recognition 함수를 이용하여 카메라를 키고, 얼굴이 인식될 때까지 알람이 울리게된다. 알람이 울리기전에 입력해둔 사용자의 이름과 face_recognition함수에서 인식된 얼굴의 이름(return 값)이 일치하면 ESC를 눌러 알람을 끌 수 있다.

>   > 2. 알람노래를 선택하고나면 어떠한 wav파일을 사용할건지 번호를 입력해야한다. 번호를 입력하면 기본wav파일로 설정된 sound에 결정한 wav바꿔넣어서 후에 울릴 알람노래를 바뀐다. 고른 번호는 LED martix에서 MUSIC 옆에 띄워진다.

>   > 3. 볼륨크기를 선택하면 알람이 울릴 소리를 어느정도의 크기로 설정할지 1 ~ 10사이에서 정한다. 설정한 소리의 크기는 LED martix에서 VOLUMN 옆에 띄워진다.

>   > 4. 알람프로그램을 종료시킨다.


- 유의사항 1: 얼굴을 찍을때 찍는 사람의 헤어스타일에 따라 인식이 달라질 정도로 헤어스타일은 큰 비중을 차지하고 있다. 여러 사용자 중 자신과 비슷한 헤어스타일을 가진 사람이 있다면 인식할 때 왔다갔다하며 헷갈려한다. 그러니 자신의 헤어스타일에 유의하며 찍어야한다.

- 유의사항 2: 얼굴을 찍은 곳에서 장소를 이동시키지 않는게 좋다. 카메라는 빛에 의해 발생한 명암을 보고 인식되는사람이 누군지 알아보는 것이기에 얼굴을 찍는 곳과 알람으로 사용할 곳의 조명은 일정해야작동이 잘 된다. 얼굴을 찍은 후, 조명이 다른곳으로 가서 사용할려고 하면 인식이 안될 수 있다.


### Built With / 누구랑 만들었나요?
- 신지환
- 김명진
- 송지호
