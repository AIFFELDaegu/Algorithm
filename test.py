import re

def solution(new_id):
    
    #first
    new_id = new_id.lower()
    #second 
    #���ĺ� �ҹ���, ����, ����, ����, ��ħǥ ġȯ
    nid = re.compile('[0-9a-z_.-]+')
    new_id = nid.findall(new_id)
    new_id = ''.join(new_id)

    #thrid 
    #���� ��ħǥ �ϳ��� ��ȯ
    while '..' in new_id:
        new_id = new_id.replace('..','.')

    #fourth
    new_id = new_id.strip('.')


    # if len(new_id) > 1 :
    #     if new_id[0] == '.' :
    #         new_id = new_id[1:]
    
    #     if new_id[-1] == '.' :
    #         new_id = new_id[0:-1]
        

    #fifth
    if new_id == '':
        new_id = 'a'

    #sixth
    if len(new_id) > 15 :
        new_id = new_id[0:15]
        if new_id[14] == '.':
            new_id = new_id[0:14]

    #seventh
    if len(new_id) < 3 :
        if len(new_id) == 1 :
            new_id = new_id + new_id + new_id
        if len(new_id) == 2 :
            new_id = new_id + new_id[1]
        
        
    answer = new_id
    return answer