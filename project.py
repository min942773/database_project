## -*- coding:utf-8 -*-

import pyodbc

cnxn = pyodbc.connect('DRIVER={MySQL ODBC 3.51 Driver};SERVER=localhost;DATABASE=pet_hospital;UID=root;PWD=0000;charset=UTF8',unicode_results=True)
cursor = cnxn.cursor()


def menu():
    print("*****메뉴*****")
    print("1. 병원 등록")
    print("2. 병원 검색")
    print("3. 병원 조회")
    print("4. 병원 삭제")
    print("5. 리뷰 등록")
    print("6. 리뷰 조회")
    print("7. 즐겨찾기에 추가")
    print("8. 마이페이지")
    print("9. 종료")

    choice = input("원하시는 메뉴를 선택해주세요 : ")
    
    return int(choice)

def welcome():
    print("************************************")
    print("Animal Care에 오신 것을 환영합니다.")
    print("************************************")
    print("회원이시라면 1. 로그인, 회원이 아니시라면 2. 회원가입을 선택해주세요.")
    choice = input("입력 : ")
    
    return int(choice)

def login():
    print("*****로그인*****")
    id = input("ID : ")
    password = input("password : ")
    cursor.execute("SELECT id, name FROM member WHERE id = '%s' AND password = '%s'" %(id, password))
    row = cursor.fetchall()
    if len(row) < 1 :
        print("틀렸습니다. 다시 입력해주세요.")
        return id, 0
    if row[0][0] == id:
        print("%s님 환영합니다." %(row[0][1]))
        return id, 1

def join():
    print("*****회원가입*****")
    cursor.execute("ALTER TABLE member CONVERT TO CHARSET utf8;")
    id = input("원하시는 ID를 입력하세요 : ")
    password = input("원하시는 비밀번호를 입력하세요 : ")
    name = input("이름을 입력하세요 : ")
    age = int(input("나이를 입력하세요 : "))
    address = input("주소를 입력하세요 : ")
    cursor.execute("INSERT INTO `member` (`id`, `password`, `name`, `age`, `address`) VALUES ('%s', '%s', '%s', '%d', '%s')" %(id, password, name, age, address))
    cnxn.commit()

def insert_hos():
    print("*****병원 등록*****")
    cursor.execute("ALTER TABLE hospital CONVERT TO CHARSET utf8;")
    in_name = input("병원 이름 : ")
    in_address = input("병원 주소 : ")
    in_contact = input("병원 연락처 : ")
    cursor.execute("SELECT contact FROM hospital WHERE contact = '%s'" %(in_contact))
    row = cursor.fetchall()
    if len(row) < 1 :
        cursor.execute("INSERT INTO `hospital` (`contact`, `member_id`, `name`, `address`) VALUES ('%s', '%s', '%s', '%s')" %(in_contact, mem_id, in_name, in_address))
        cnxn.commit()
    else :
        print("이미 존재하는 병원입니다.")


def search_by_name():
    print("*****병원 검색*****")
    name = input("검색 : ")
    cursor.execute("SELECT name, address, contact, rate FROM hospital WHERE name LIKE '%%%s%%'" %(name))
    row = cursor.fetchall()
    for i in range(len(row)):
        print("병원 이름 : ", row[i][0], "\t병원 주소 : ", row[i][1], "\t병원 연락처 : ", row[i][2], "\t별점 : ", row[i][3])

def view_hospital():
    print("*****병원 조회*****")
    cursor.execute("SELECT name, address, contact, rate FROM hospital")
    row = cursor.fetchall()
    for i in range(len(row)):
        print("병원 이름 : ", row[i][0], " 병원 주소 : ", row[i][1], " 병원 연락처 : ", row[i][2], "별점 : ", row[i][3])

def delete_hospital():
    print("*****병원 삭제*****")
    contact = input("삭제할 병원의 연락처를 입력하세요 : ")
    cursor.execute("SELECT name FROM hospital WHERE contact = '%s'" %(contact))
    row = cursor.fetchall()
    answer = input("'%s'가 맞습니까? Y/N : " %(row[0][0]))
    if(answer == 'Y'):
        cursor.execute("DELETE FROM `pet_hospital`.`hospital` WHERE `contact`='%s'" %(contact))
        cnxn.commit()
    else:
        print("처음부터 다시 시도해주세요.")

def view_review():
    print("*****리뷰 조회*****")
    contact = input("리뷰를 볼 병원의 연락처를 입력하세요 : ")
    cursor.execute("SELECT * FROM review WHERE hos_contact = '%s'" %(contact))
    row = cursor.fetchall()
    for i in range(len(row)):
        print("-----------------------------")
        print("리뷰 번호 : ", row[i][0])
        print("작성자 : ", row[i][1])
        print("별점 : ", row[i][5])
        print("글 제목 : ", row[i][2])
        print("글 내용 : ", row[i][3])
        print()
        view_comment(row[i][0])
    print("-----------------------------")
    comment_review = input("리뷰에 댓글을 남기겠습니까? Y/N : ")
    if comment_review == 'Y':
        add_comment()
        
def write_review():
    print("*****리뷰 작성*****")
    cursor.execute("ALTER TABLE review CONVERT TO CHARSET utf8;")
    contact = input("리뷰를 작성할 병원의 연락처를 입력하세요 : ")
    cursor.execute("SELECT name FROM hospital WHERE contact = '%s'" %(contact))
    row = cursor.fetchall()
    if len(row) < 1 :
        print("틀렸습니다. 다시 입력해주세요.")
    else :
        print(row[0][0], "가 맞습니까? Y/N")
        answer = input()
        if answer == 'Y':
            title_in = input("제목 : ")
            body_in = input("내용 : ")
            rate_in = input("별점 : ")
            print("작성이 완료되었습니다.")
            cursor.execute("INSERT INTO `review` (`member_id`, `title`, `body`, `hos_contact`, `rate`) VALUES ('%s', '%s', '%s', '%s', '%s')" %(mem_id, title_in, body_in, contact, rate_in))
            cnxn.commit()
            rate_update(contact)
        else:
            print("리뷰 작성을 실패하였습니다.")

def rate_update(contact):
    cursor.execute("SELECT rate FROM review WHERE hos_contact = '%s'" %(contact))
    row = cursor.fetchall()
    sum = 0.0
    for i in range(len(row)):
        sum += float(row[i][0])
    avg = sum / len(row)
    cursor.execute("UPDATE `hospital` SET `rate`='%s' WHERE `contact`='%s'" %(str(avg), contact))
    cnxn.commit()
    

def add_favorite():
    print("*****즐겨찾기 추가*****")
    contact = input("즐겨찾기 할 병원의 연락처를 입력하세요 : ")
    cursor.execute("SELECT name FROM hospital WHERE contact = '%s'" %(contact))
    row = cursor.fetchall()
    if len(row) < 1 :
        print("틀렸습니다. 다시 입력해주세요.")
    else :
        print(row[0][0], "가 맞습니까? Y/N")
        answer = input()
        if answer == 'Y':
            cursor.execute("INSERT INTO `favorite` (`member_id`, `hospital_contact`) VALUES ('%s', '%s')" %(mem_id, contact))
            cnxn.commit()
        else:
            print("추가하지 못했습니다. 다시 진행해주세요.")

def my_page():
    print("*****마이 페이지*****")
    print("1. 내가 작성한 리뷰 보기")
    print("2. 즐겨찾기 목록 보기")
    print("3. 즐겨찾기 삭제하기")
    answer = input("입력 : ")

    return int(answer)
    
def my_reviews():
    cursor.execute("SELECT title, body, hos_contact FROM review WHERE member_id = '%s'" %(mem_id))
    row = cursor.fetchall()
    if len(row) < 1:
        print("작성한 리뷰가 없습니다.")
    for i in range(len(row)):
        print("-----------------------------")
        print("제목 : ", row[i][0])
        print("병원 연락처 : ", row[i][2])
        print("내용 : ", row[i][1])
        print("-----------------------------")

def my_favorites():
    print("*****즐겨찾기 목록*****")
    cursor.execute("SELECT b.name, a.hospital_contact FROM favorite a INNER JOIN hospital b ON a.member_id = '%s' AND b.contact = a.hospital_contact" %(mem_id))
    row = cursor.fetchall()
    for i in range(len(row)):
        print("병원 이름 : ", row[i][0], "연락처 : ", row[i][1])

def delete_favorite():
    print("*****즐겨찾기 삭제*****")
    contact = input("즐겨찾기에서 삭제할 병원의 전화번호를 입력하세요 : ")
    cursor.execute("SELECT name FROM hospital WHERE contact = '%s'" %(contact))
    row = cursor.fetchall()
    if len(row) > 0:
        answer = input("'%s'가 맞습니까? Y/N : " %(row[0][0]))
        if answer == 'Y':
            cursor.execute("DELETE FROM `favorite` WHERE `hospital_contact`='%s'" %(contact))
        else :
            print("삭제하지 못했습니다. 다시 진행해주세요.")
    else  :
        print("즐겨찾기한 병원이 없습니다.")

def view_comment(review_num):
    cursor.execute("SELECT member_id, body FROM comment WHERE review_num = '%s'" %(review_num))
    row = cursor.fetchall()
    for i in range(len(row)):
        print("└ ", row[i][0], " : ", row[i][1])

def add_comment():
    print("*****댓글 달기*****")
    cursor.execute("ALTER TABLE comment CONVERT TO CHARSET utf8;")
    review_num = input("댓글을 달 리뷰의 번호를 입력해주세요 : ")
    body = input("댓글을 입력해주세요 : ")
    cursor.execute("INSERT INTO `comment` (`review_num`, `member_id`, `body`) VALUES ('%s', '%s', '%s')" %(review_num, mem_id, body))
    cnxn.commit()

def wrong_insert():
    print("잘못된 입력입니다. 다시 시도해주세요.")

cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf8')
cnxn.setencoding(encoding='utf8')
cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
mem_id = ''

while True: # welcome 페이지, 로그인/회원가입을 할 수 있음
    welcome_input = welcome()
    if welcome_input == 2 : # 회원가입 선택 시
        join() # 회원 가입
        mem_id, login_input = login() # 로그인
    elif welcome_input == 1: # 로그인 선택 시
        mem_id, login_input = login() # 로그인
    else:
        login_input = 0 # 예외처리를 위한 변수 설정
        wrong_insert() # 잘못된 입력 처리
    if login_input == 1: #제대로 로그인 한 경우
        break
while True:
    menu_input = menu() # 메뉴 출력 및 입력 받기
    if menu_input == 1 :
        insert_hos() # 병원 등록
    elif menu_input == 2:
        search_by_name() # 병원 검색
    elif menu_input == 3:
        view_hospital() # 등록된 모든 병원 조회
    elif menu_input == 4:
        delete_hospital() # 병원 삭제
    elif menu_input == 5:
        write_review() # 리뷰 등록
    elif menu_input == 6:
        view_review() # 병원에 따른 리뷰 조회
    elif menu_input == 7:
        add_favorite() # 즐겨찾기 추가
    elif menu_input == 8:
        my_page_input = my_page() # 마이페이지 화면 출력
        if my_page_input == 1:
            my_reviews() # 내 리뷰 조회
        elif my_page_input == 2:
            my_favorites() # 내 즐겨찾기 목록 조회
        elif my_page_input == 3:
            delete_favorite() # 즐겨찾기 삭제
        else:
            wrong_insert() # 잘못된 입력 처리
    elif menu_input == 9:
        print("BYE") 
        break # 프로그램 종료 
