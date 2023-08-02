import pandas as pd

# A 파일과 B 파일의 경로 설정
file_a_path = './python/A_file.xlsx'
file_b_path = './python/B_file.xlsx'

# A 파일과 B 파일을 pandas DataFrame으로 읽기
df_a = pd.read_excel(file_a_path, engine='openpyxl', header=None)  # header=None으로 열 이름 무시
df_b = pd.read_excel(file_b_path, engine='openpyxl')

# A 파일의 학교 이름들을 리스트로 추출
school_names_a = df_a.iloc[:, 0].tolist()

# G행이 존재하는 경우에만 학교 이름을 추출
if '학교이름' in df_b.columns:
    school_names_b = df_b['학교이름'].tolist()
else:
    school_names_b = []

# df_b 파일에서 A 파일에 해당하는 학교 이름이 있는 행들만 추출하여 새로운 DataFrame 생성
matched_rows_df = df_b[df_b['학교이름'].isin(school_names_a)]

# A 파일에 해당하지 않는 학교 이름이 있는 행들을 추출하여 새로운 DataFrame 생성
no_result_df = df_b[~df_b['학교이름'].isin(school_names_a)]
no_result_df['학교이름'] = 'no_result'  # 새로운 DataFrame에 'no_result' 학교 이름 추가

# 결과를 새로운 엑셀 파일로 저장
output_file_path = './output.xlsx'
matched_rows_df.to_excel(output_file_path, index=False, engine='openpyxl')

# 'no_result'라는 학교 이름을 가진 DataFrame을 새로운 파일로 저장
no_result_file_path = './no_result.xlsx'
no_result_df.to_excel(no_result_file_path, index=False, engine='openpyxl')

print("크롤링 및 작업이 완료되었습니다.")
