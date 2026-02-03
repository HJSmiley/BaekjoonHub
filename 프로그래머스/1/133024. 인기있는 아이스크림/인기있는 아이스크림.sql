-- 코드를 입력하세요
# 상반기에 판매된 아이스크림의 맛(FLAVOR)을 총주문량(TOTAL_ORDER)을 기준으로 내림차순 정렬하고
# 총주문량이 같다면 출하 번호(SHIPMENT_ID)를 기준으로 오름차순 정렬
SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID;