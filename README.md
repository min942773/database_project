## database_project

팀원 : [김민주](https://github.com/min942773), [양재연](https://github.com/reyeon1209)

## 1. 프로젝트 소개
### 프로젝트 선정 이유
반려 동물의 수는 증가하는데에 반해 반려동물 관련 서비스는 적은 것을 인지하여 이러한 프로젝트를 진행하게 되었다.

### 프로젝트 주제
전국의 동물 병원을 검색해서 병원 정보를 얻고, 병원 리뷰를 사용자들이 직접 등록할 수 있는 서비스

### 프로젝트 언어 및 환경
프로젝트 언어 : Python
DB : MySQL에서 제공하는 innoDB엔진

### 주요 기능
* 동물 병원 데이터 셋을 이용한 병원 검색 기능
* 동물 병원 정보 등록 및 삭제 기능
* 등록된 모든 병원 조회 기능
* 동물 병원에 대한 리뷰와 선호도(별점) 등록 기능
* 리뷰에 대한 댓글을 남길 수 있는 기능
* 사용자가 원하는 동물 병원을 즐겨찾기에 추가하는 기능
* 마이페이지를 통해 자신이 쓴 리뷰 조회, 즐겨찾기 목록 조회, 즐겨찾기 삭제 기능

### 화면 흐름도
![image](https://user-images.githubusercontent.com/46713032/69898757-c9d38880-13a0-11ea-9bd5-9aafea87488f.png)

## 2. 데이터베이스 설계
### 첨부 보고서
요구사항 분석, 테이블 명세서, 용어 사전, 도메인 기술서 등 자세한 설계 과정과 정규화 과정은 첨부된 [**보고서**](https://github.com/min942773/database_project/blob/master/Animal%20Care.pdf) 참고

### E-R 다이어그램
![image](https://user-images.githubusercontent.com/46713032/69898764-e7a0ed80-13a0-11ea-83ea-20204639b2ae.png)

### 릴레이션 스키마
![relation_schema](https://github.com/min942773/database_project/blob/master/images/image2.PNG?raw=true)

### 물리 ERD
![ERD](https://github.com/min942773/database_project/blob/master/images/image.png?raw=true)
