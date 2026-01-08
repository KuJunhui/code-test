import re

example_string = "a1!,b22@@;c333### d4$"

# 문자열에서 패턴 전부 추출
def re_findall(str):
    score_list = re.findall(r'\d{1,2}', str)
    bonus_list = re.findall(r'[abc]', str)
    option_list = re.findall(r'[!@#]', str)

    return score_list, bonus_list, option_list

# 패턴을 다른 문자로 치환
def re_sub(str):
    change_list = re.sub(r'a1', 'A1', str)
    delete_num_list = re.sub(r'\d', '', str)
    delete_space_list = re.sub(r'\s+', '', str)

    return change_list, delete_num_list, delete_space_list

# 정규식 기준으로 문자열 분리
def re_split(str):
    split_list = re.split(r'[,;\s]', str)

    return split_list

def re_match(str):
    num = int(re.match(r'\d{1,2}', str).group())

    return num

# 여러개의 점 -> 1개 점
new_id = re.sub(r'\.+', '.', example_string)

# 양쪽 끝 점 제거
new_id = new_id.strip('.')
# 오른쪽 점 제거
new_id = new_id.rstrip('.')
# 왼쪽 점 제거
new_id = new_id.lstrip('.')

# 음수 필터링
str = re.findall(r'-?\d', 'abc -12 and 34 and --56')
str2 = re.findall(r'-?\d+', 'abc -12 and 34 and --56')
# print(str)
# print(str2)

print(re_findall(example_string))
print(re_sub(example_string))
print(re_split(example_string))
print(re_match("0S"))