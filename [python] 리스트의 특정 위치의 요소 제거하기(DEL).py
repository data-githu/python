# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:40:27 2020

@author: Owner
"""

■ 108. 리스트의 특정 위치의 요소 제거하기 (del)


※ del메소드와 remove 메소드의 차이?
둘다 리스트 안의 요소를 삭제하는 것인데
remove는 요소명으로 삭제하는 것이고
del은 리스트의 인덱스 번호로 삭제하는 것입니다.

예제 : 
a = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
del(a[4])
print(a)

문제320. 아래의 a리스트에서 목성을 지우시오
a = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
del(a[a.index('목성')])
print(a)