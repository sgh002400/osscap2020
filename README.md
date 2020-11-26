## 2020 오픈소스 프로젝트
## Smart Alarm / 스마트 알람
현대인은 시간이 중요합니다. 효율적인 시간을 사용하기 위해 생활패턴 조절이 필수적이라는걸 알게되었다. 일반적인 알람은 눌러서 끄는게 대부분이기에 사용자가 잠에서 확실히 깨어나지 못하는 경우가 많다. 간편하게 알람을 끄는 방식의 단점을 생각하여 스마트 알람을 구상하게되었다.

- 간단한 실행 안내
프로그램 실행 순서는 01_face_dataset.py, 02_face_training.py, alarmclock_mediumversion.py를 순서대로 실행시킨다. 01_face_dataset.py로 대상의 이름과 얼굴 img를 저장한다. 02_face_training.py로 위 이미지를 학습시킨다. alarmclock_mediumversion.py에선 알람시계기능과 LED Matrix에UI를 띄우는 역할을 한다. 이후 알람시간이 되면 얼굴이 인식된 후 ESC를 누를때 까지 알람이 안꺼지게 만들었다.

### Installing / 설치

아래 사항들이 설치가 되어있어야합니다.
- Open CV
- Python3
- Pygame
- opencv-contrib-python
- opencv-python


### Running the tests / 테스트의 실행
-구체적으로

- $sudo python3 01_face_dataset.py
> 01_face_dataset.py를 실행시켜서 이름 id를 입력한 후, 카메라를 통해 자신의 얼굴이 인식되면 img파일로 총 30장이 저장됩니다.

- $sudo python3 02_face_training.py
> 02_face_training.py를 실행시키면 이미지 파일들을 불러와서 이를 recognizer.train()을 통해 학습시킨 후 결과를 recognizer.write()을 통해 trainer.yml 파일로 저장시킨다.

- $sudo python3 alarmclock_mediumversion.py
> alarmclock_mediumversion.py을 실행시키면 LED matrix에 UI가 나오게 되며 번호를 통해 원하는 설정을 고를 수 있다. 1.알람시간설정, 2.알람노래설정, 3.볼륨크기설정, 4.종료로 되어있다.

>   > 1 - 1. 알람시간을 선택하면 사용자의 이름을 입력받고 알람이 울릴 시간, 분을 입력한다. 이때 시간은 24, 분은 60 이상의 수를 넣으면 다시 입력한다. 그 후 time 모듈을 통해 현재시간을 가져온 후 설정한 시간과의 차이를 초로 바꾸어 time.sleep으로 설정시간때까지 기다린다. 이떄 설정한 시간은 LED matrix에서 ALARM 옆에 띄워진다.

>   > 1 - 2. time.sleep이 끝나면 sample_recognition.py에서 face_recognition함수를 이용하여 카메라를 키고, 얼굴이 인식될 때까지 알람이 울리게된다. 알람이 울리기전에 입력해둔 사용자의 이름과 인식된 얼굴의 이름이 일치하면 ESC를 눌러 알람을 끈다.

>   > 2. 알람노래를 선택하고나면 어떠한 wav파일을 사용할건지 번호를 입력해야한다. 번호를 입력하면 기본wav파일로 설정된 sound에 결정한 wav바꿔넣어서 후에 울릴 알람노래를 바뀐다. 고른 번호는 LED martix에서 MUSIC옆에 띄워진다.

>   > 3. 볼륨크기를 선택하면 알람이 울릴 소리를 어느정도의 크기로 설정할지 0 ~ 1사이에서 정한다. 설정한 소리의 크기는 LED martix에서 VOLUMN옆에 띄워진다.

>   > 4. 알람프로그램을 종료시킨다.


### Built With / 누구랑 만들었나요?
- 신지환 - OpenCV와 카메라를 통해 얼굴인식하기, 인식된 사람의 이름과 인식률 띄우기
- 김명진 - 알람소스코드 수정과 LED matrix를 통해 화면띄우기, 알람노래설정, 볼륨크기설정, 
- 송지호 - 알람코드와 노래재생코드 병합

### 느낀점
