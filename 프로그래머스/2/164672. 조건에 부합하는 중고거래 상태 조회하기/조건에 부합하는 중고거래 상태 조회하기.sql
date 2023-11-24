-- 코드를 입력하세요
SELECT  BOARD_ID, WRITER_ID, TITLE,PRICE ,CASE 
                                           WHEN STATUS= "RESERVED"
                                           THEN "예약중"
                                           WHEN STATUS = "DONE"
                                           THEN "거래완료"
                                           ELSE "판매중"
                                           END AS STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE = "2022-10-05"
ORDER BY BOARD_ID DESC