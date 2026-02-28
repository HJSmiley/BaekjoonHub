-- 코드를 입력하세요
SELECT DISTINCT A.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR AS A
LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS B
ON A.CAR_ID = B.CAR_ID
# 자동차 종류가 '세단'인 자동차들 중 10월에 대여를 시작한 기록이 있는 자동차 ID 리스트를 출력
WHERE A.CAR_TYPE LIKE "세단" AND B.START_DATE LIKE "%-10-%"
# 자동차 ID 리스트는 중복이 없어야 하며, 자동차 ID를 기준으로 내림차순
ORDER BY A.CAR_ID DESC;
