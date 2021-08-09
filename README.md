# :church: INTO THE LIGHT CHURCH MANAGE

---

[![Start](https://img.shields.io/badge/START-2021.06.29-blue.svg)](./START)

---

## 기획 계기

- 개척교회를 운영하게 되면서 상용화된 교적관리 프로그램을 사용하기엔 성도의 수가 적고, 비용문제도 만만치 않다고 생각되었고, 그에 따라 나의 실력을 향상 시킬 겸 직접 만들어 보고싶다는 생각을 하게됨.

## 어떻게 만들건데?

- 일단.. 가장 익숙한 파이썬을 이용하고, Flask Web Frame work를 사용할 예정.

---



## DB 설계

- USER : 웹 사이트에 회원으로서, 교적을 조회 및 수정할 권리를 가진 사람
  1. id : 사용자 ID
  2. password : 사용자 PW
- MEMBER : 교회 성도
  1. name : 이름
  2. age : 나이
  3. sex : 성별
  4. birthday : 생년월일
  5. contact : 연락처
  6. address : 주소
  7. job : 직업
  8. email : 이메일 주소
  9. baptism : 침례여부
  10. marriage : 결혼여부
  11. prevchurch : 이전 교회
  12. create_date : 등록일자



## UI 설계

- 디자인중..



## 추가 할 기능

- 자동 로그아웃 기능 / 2021.07.10
- 달력을 만들어 성도들의 생일을 표시하는 기능 / 2021.07.12



## reference

- [점프 투 플라스크](https://wikidocs.net/book/4542)