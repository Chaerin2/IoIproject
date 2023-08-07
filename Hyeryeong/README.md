#  데이터 가공
* musinsa_data.csv : 기존의 데이터에서 column 명을 영문으로 변경
* musinsa_fin.ipynb : 필요한 데이터 가공
  * data2 : 불필요한 column('c_number', 'c_name', 'link', 'size') 제거
  * result_dict : key값_제품번호(c_number)와 value값_제품명(c_name), 이미지링크(link)을 매핑한 딕셔너리 데이터
