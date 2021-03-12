def solution(phone_book):
    answer = True
    dict = {}
    phone_book.sort(key=len)
    tmp_len = len(phone_book[0])
    for i in range(len(phone_book)):
        if tmp_len != len(phone_book[i]):
            for j in range(i,len(phone_book)):
                if hash(phone_book[j][:tmp_len]) in dict.keys():
                    answer = False
                    return answer
            tmp_len = len(phone_book[i])
            
        dict[hash(phone_book[i])] = phone_book[i]
            
    return answer