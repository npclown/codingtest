def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        tmp = ""
        true_and_false = True
        for tree in skill_tree:
            if tree in skill:
                tmp += tree
                if skill[:len(tmp)] != tmp:
                    true_and_false = False
                    break
        if true_and_false:
            answer += 1
    return answer