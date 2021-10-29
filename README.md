# Cloud-Computing
2021 COSE444

## AWS-Lambda-S3
AWS lambda를 통해서 특정 bucket에 올라가면, 정사각형으로 crop하고 환경변수 COLOR_OR_GRAY에 따라 흑백으로 변환 후 output bucket에 변환된 이미지 파일 업로드

### Files
-lambda_function.py   
이벤트 발생 시 처리할 함수
- make-square.zip
AWS-Lambda의 layer   
lambda_function 코드를 실행하기 위해 필요한 패키지, 현재는 이미지 변환을 위한 pillow package 파일만 있음.

### Lambda Environment
- python 3.8
- x86_64
