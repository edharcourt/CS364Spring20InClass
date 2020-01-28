#lang racket

(define l (cons 1 (cons 2 null)))

; Scheme has pairs

(define p (cons 1 2))

; lists are pairs but pairs are not lists

(define lon '(1 2 3 4 5))

; Write a function that adds 1 to each item in a list and returns
; the new list
(define (increment lon)
  (if (null? lon)
      null
      (cons (+ 1 (first lon)) (increment (rest lon)))))

(define (scale10 lon)
  (if (null? lon)
      null
      (cons (* 10 (first lon)) (scale10 (rest lon)))))

(define (map f lot)
  (if (null? lot)
      null
      (cons (f (first lot)) (map f (rest lot)))))

(define lol '((1 2 3) (1) () (6 7 8 9)))

; O(length lst1)
(define (append lst1 lst2)
  (if (null? lst1)
      lst2
      (cons (first lst1) (append (rest lst1) lst2))))

(define lon1 '(1 2 3))
(define lon2 '(4 5))

; bad reverse  O(n^2) reverse
(define (reverse-bad lst)
  (if (null? lst)
      '()
      (append (reverse-bad (rest lst)) (list (first lst)))))

; iterative reverse
(define program
'(define (reverse lst)
  (define (reverse1 lst acc)
    (if (null? lst)
        acc
        (reverse1 (rest lst) (cons (first lst) acc))))
  (reverse1 lst '()))
)

; sample s-list
(define blob '((2 3 4) "hello" (1 (99 87)) () apple))

; write a function sum-s-list that add all the numbers that
; appear in an s-list
; recursion over an s-list
(define (sum-s-list s-list)
  (if (null? s-list)
      0
      (if (number? (first s-list))
          (+ (first s-list) (sum-s-list (rest s-list)))
          (if (list? (first s-list))
              (+ (sum-s-list (first s-list)) (sum-s-list (rest s-list)))
              (sum-s-list (rest s-list))))))

; use a let to clean up code above. exercise






