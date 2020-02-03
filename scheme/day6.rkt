#lang racket
(define (map f lot)
  (if (null? lot)
      null
      (cons (f (first lot)) (map f (rest lot)))))

(define (append lst1 lst2)
  (if (null? lst1)
      lst2
      (cons (first lst1) (append (rest lst1) lst2))))

; O(n) version of reverse.
; Iterative or linear? Uses extra stack as argument
; modified so accumulator is first argument
(define (reverse1 acc lst)
  (if (null? lst)
    acc
    (reverse1 (cons (first lst) acc) (rest lst))))

; Sample Hogwarts data
(define grades '(
     ("Hermione" 99 99 100 100)
     ("Ron" 50 65 78 23)
     ("Harry" 88 95 76 80)
     ("Draco" 1 2 3 4)
 ))



