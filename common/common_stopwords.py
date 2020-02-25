class CommonStopwords:

    def stop_words_region(self):
        stop_words = ['강원', '경기', '경남', '경북', '대구', '대전', '부산', '서울', '울산', '인천', '전남', ' 전북', '제주, 충남', '충북']
        return stop_words

    def stop_words_region_sub(self):
        stop_words = ['수원', '성남', '안양', '안산', '용인', '광명', '평택', '과천', '오산', '시흥', '군포', '의왕', '하남', '이천', '하남',
                      '안성', '김포', '화성', '광주', '여주', '부천', '고양', '의정부', '구리', '남양주', '파주', '양주', '포천', '연천'
                                                                                                      '가평', '춘천', '원주',
                      '강릉', '동해', '태백', '속초', '삼척', '홍천', '횡성', '영월', '평창', '정선', '철원',
                      '화천', '양구', '인제', '고성', '양양', '청주', '자치', '충주', '제천', '보은', '옥천', '영동', '진천', '괴산', '음성',
                      '단양', '증평', '천안', '공주', '보령', '아산', '서산', '논산', '계룡', '당진', '금산', '부여', '서천', '청양', '홍성',
                      '예산', '태안', '전주', '익산', '정읍', '남원', '김제', '완주', '진안', '무주', '장수', '순창',
                      '고창', '부안', '목포', '여수', '순천', '나주', '광양', '담양', '곡성', '구례', '고흥', '보성', '화순', '장흥', '강진',
                      '해남', '영암', '무안', '함평', '영광', '장성', '완도', '진도', '포항', '자치', '경주', '김천', '안동', '구미', '영주',
                      '영천', '상주', '문경', '경산', '의성', '청송', '영양', '영덕', '청도', '고령', '성주', '칠곡', '예천', '봉화', '울진',
                      '울릉', '창원', '진주', '통영', '사천', '김해', '밀양', '거제', '양산', '의령', '함안', '창녕', '고성', '남해', '하동',
                      '산청', '함양', '거창', '합천']
        return stop_words

    def stop_words_region_sub_map(self):
        stop_words = { '수원': '경기' ,'성남': '경기' ,'안양': '경기' , '안산': '경기' , '용인': '경기' , '광명': '경기' , '평택': '경기' ,
                       '과천': '경기' , '오산': '경기' , '시흥': '경기' , '군포': '경기' , '의왕': '경기' , '하남': '경기' , '이천': '경기' ,
                       '하남': '경기' ,'안성': '경기' , '김포': '경기' , '화성': '경기' , '광주': '경기' , '여주': '경기' , '부천': '경기' ,
                       '고양': '경기' , '의정부': '경기' , '구리': '경기' , '남양주': '경기' , '파주': '경기' , '양주': '경기' , '포천': '경기' , '연천': '경기',
                       '가평': '강원' , '춘천': '강원' , '원주': '강원' , '강릉': '강원' , '동해': '강원' , '태백': '강원' , '속초': '강원' ,
                       '삼척': '강원' , '홍천': '강원' , '횡성': '강원' , '영월': '강원' , '평창': '강원' , '정선': '강원' , '철원': '강원' ,
                        '화천': '강원' , '양구': '강원' , '인제': '강원' , '양양': '강원' ,
                       '청주': '충북' , '자치': '충북' , '충주': '충북' , '제천': '충북' , '보은': '충북' , '옥천': '충북' , '영동': '충북' ,
                       '진천': '충북' , '괴산': '충북' , '음성': '충북' ,'단양': '충북' , '증평': '충북' ,
                       '증평': '충남' , '천안': '충남' , '공주': '충남' , '보령': '충남' , '아산': '충남' , '서산': '충남' , '논산': '충남' ,
                       '계룡': '충남' , '당진': '충남' , '금산': '충남' , '부여': '충남' , '서천': '충남' , '청양': '충남' , '홍성': '충남' ,
                        '예산': '충남' , '태안': '충남' ,
                       '전주': '전북' , '익산': '전북' , '정읍': '전북' , '남원': '전북' , '김제': '전북' , '완주': '전북' , '진안': '전북' ,
                       '무주': '전북' , '장수': '전북' , '순창': '전북' ,'고창': '전북' , '부안': '전북' , '목포': '전북' , '여수': '전북' ,
                       '순천': '전남' , '나주': '전남' , '광양': '전남' , '담양': '전남' , '곡성': '전남' , '구례': '전남' , '고흥': '전남' ,
                       '보성': '전남' , '화순': '전남' , '장흥': '전남' , '강진': '전남' ,'해남': '전남' , '영암': '전남' , '무안': '전남' ,
                       '함평': '전남' , '영광': '전남' , '장성': '전남' , '완도': '전남' , '진도': '전남' ,
                       '포항': '경북' , '자치': '경북' , '경주': '경북' , '김천': '경북' , '안동': '경북' , '구미': '경북' , '영주': '경북' ,
                        '영천': '경북' ,'상주': '경북' , '문경': '경북' , '경산': '경북' , '의성': '경북' , '청송': '경북' , '영양': '경북' ,
                       '영덕': '경북' , '청도': '경북' , '고령': '경북' , '성주': '경북' , '칠곡': '경북' , '예천': '경북' , '봉화': '경북' ,
                       '울진': '경북' , '울릉': '경북' ,
                       '창원': '경남' , '진주': '경남' , '통영': '경남' , '사천': '경남' , '김해': '경남' , '밀양': '경남' , '거제': '경남' ,
                       '양산': '경남' , '의령': '경남' , '함안': '경남' , '창녕': '경남' , '고성': '경남' , '남해': '경남' , '하동': '경남' ,
                       '산청': '경남' , '함양': '경남' , '거창': '경남' , '합천': '경남' }
        return stop_words

    def stop_words_another(self):
        stop_words = ['축제', '행사', '문화', '프로그램', '참여', '올해', '이번', '시간', '시민', '에디터', '사진', '오늘', '사람', '지역',
                      '시작', '장소', '여기', '우리', '지금', '하나', '생각', '정말', '바로', '블로그', '페스티벌', '이용', '기간', '업체',
                      '홈페이지', '구경', '보고', '다시', '기록', '참고', '가격', '느낌', '준비', '네이버', '한번', '저희', '낚시', '호텔',
                      '방문', '자리', '하루', '먼저', '다른', '정도']
        return stop_words