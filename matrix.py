matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]

# 변수 설정
matrix_len = 0

# matrix 리스트 길이 측정
for mat in matrix:
    matrix_len += 1
print(matrix_len)

# matrix 내 개별 리스트 길이 측정
for number in matrix:
    # matrix 내 개별 리스트 길이 변수 설정 (number = 각각의 리스트, temporary_len = 각각의 리스트 내 요소 개수)
    temporary_len = 0
    for num in number:
        temporary_len += 1
    if temporary_len <= 4:
        print(f'{number} 리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')
    else:
        continue

# matrix 리스트를 순회하는 for문
for mat in range(len(matrix)):
    # matrix 리스트 내 개별 리스트를 순회하는 for문
    for number in range(len(matrix[mat])):
        print(f'matrix의 {mat}, {number}번째 요소의 값은 {matrix[mat][number]}입니다.')
        number += 1
    mat += 1