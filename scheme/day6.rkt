#lang racket

; reduce a list of things to a single value
(define (reduce f id lst) 
  (if (null? lst)
      id
      (f (first lst) (reduce f id (rest lst)))))

; rewrite reduce so that it processes arguments
; from left to right (iteratively)
(define (reducel f acc lst)
  (if (null? lst)
      acc
      (reducel f (f (first lst) acc) (rest lst))))


(define (append lst1 lst2)
  (if (null? lst1)
      lst2
      (cons (first lst1) (append (rest lst1) lst2))))

; tests lists
(define gryffindor '("Harry" "Ron" "Hermion"))
(define slytherin '("Draco" "Crab" "Goyle"))
(define nums '(1 2 3 4 5))

(define (len lst)
  (foldr (lambda (x r) (+ 1 r)) 0 lst))


(define (map f lot)
  (if (null? lot)
      null
      (cons (f (first lot)) (map f (rest lot)))))

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

(define (mycons x l)
  (cons (string-upcase x) l))

; Write map using foldr
(define (mymap f lst)
  (foldr (lambda (x r) (cons (f x) r)) null lst))


; (map first (map rest grades))
; Sample Hogwarts data
(define grades1 '(
     (first (rest ("Hermione" 99 99 100 100)))
     (first (rest ("Ron" 50 65 78 23)))
     (first (rest ("Harry" 88 95 76 80)))
     (first (rest ("Draco" 1 2 3 4)))
 ))

; function compose defined as o
(define (o f g)
  (lambda (x) (f (g x))))

; HW frequency dictionary
(define freq '( ("a" 123)
                ("z" 3)
                ("e" 493)
                ("q" 1)
               )
)

; find max frequency in the frequency dictionary
(foldl max (cadar freq) (map cadr (rest freq)))

(define (widget p1 p2)
  (if (> (cadr p1) (cadr p2))
      p1
      p2))

; write an expression to find the character
; with the highest frequency
(foldl widget (car freq) (rest freq))

