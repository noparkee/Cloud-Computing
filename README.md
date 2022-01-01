# Cloud-Computing
2021 COSE444

## 1. AWS-Lambda-S3
(실습 과제 1) AWS lambda를 통해서 특정 bucket에 올라가면, 정사각형으로 crop하고 환경변수 COLOR_OR_GRAY에 따라 흑백으로 변환 후 output bucket에 변환된 이미지 파일 업로드

### Files
- lambda_function.py   
이벤트 발생 시 처리할 함수
- make-square.zip
AWS-Lambda의 layer   
lambda_function 코드를 실행하기 위해 필요한 패키지, 현재는 이미지 변환을 위한 pillow package 파일만 있음.

### Lambda Environment
- python 3.8
- x86_64



## 2. Kubernetes
(실습 과제 3) .yaml 파일을 통한 쿠버네티스 다루기

### Files
- nginx_deployment_service.yaml: 아래 요구 사항을 만족하는 yaml 파일
  - Deployment 이름: nginx-deployment
  - Deployment 이미지: nginx
  - Pod replication 개수: 2
  - Service 이름: nginx-service
  - nginx-deployment와 nginx-service 연결

```sh
kubectl apply -f nginx_deployment_service.yaml
```
   

- ubuntu_printenv.yaml: 아래 요구 사항을 만족하는 yaml 파일
  - Pod 이름: printenv
  - image: ubuntu
  - namespace: my-ns
  - Pod 생성시 환경 변수를 출력한다. (printenv 명령어 사용)

```sh
kubectl apply -f ubuntu_printenv.yaml
kubectl logs -n my-ns printenv
```
yaml 파일로 쿠버네티스 기본 세팅 후, log를 통해 프린트된 환경 변수 확인
