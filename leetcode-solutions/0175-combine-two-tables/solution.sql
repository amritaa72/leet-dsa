# Write your MySQL query statement below
select Person.firstName, Person.lastname, address.city, address.state
FROM PERSON LEFT JOIN ADDRESS ON PERSON.PERSONID=ADDRESS.PERSONID
