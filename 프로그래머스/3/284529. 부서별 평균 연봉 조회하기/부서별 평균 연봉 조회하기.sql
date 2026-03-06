-- 코드를 작성해주세요

# HR_DEPARTMENT와 HR_EMPLOYEES 테이블을 이용해 부서별 평균 연봉을 조회
# 부서별로 부서 ID, 영문 부서명, 평균 연봉을 조회

# 평균연봉은 소수점 첫째 자리에서 반올림하고 컬럼명은 AVG_SAL
# 결과는 부서별 평균 연봉을 기준으로 내림차순 정렬

SELECT D.DEPT_ID, D.DEPT_NAME_EN, ROUND(AVG(E.SAL), 0) AS AVG_SAL
FROM HR_DEPARTMENT D
JOIN HR_EMPLOYEES E
ON D.DEPT_ID = E.DEPT_ID
GROUP BY E.DEPT_ID
ORDER BY AVG_SAL DESC;