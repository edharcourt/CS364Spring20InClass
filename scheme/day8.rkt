#lang racket

; s - list of lists
(define (cons-into-each x s)
  (if (null? s)
    null
    (cons (cons x (first s)) (cons-into-each x (rest s)))
  )
)

; study question: rewrite cons-into-each using map

(define (pow s)
  (if (null? s)
      (list null)  ; '(())
      (let (
            (p (pow (rest s)))
           )
        (append p (cons-into-each (first s) p))
      )
  )
)

; function filter keeps all items in  list that satisfy
; the predicate pred?
(define (filter pred? lst)
  (if (null? lst)
      null
      (if (pred? (first lst))
          (cons (first lst) (filter pred? (rest lst)))
          (filter pred? (rest lst)))))

;(define (lt3 x) (< x 3)) 
(define lt3
  (lambda (x) (< x 3)))

(define lty
  (lambda (y)
    (lambda (x) (< x y))))

; op is a binary operator
(define (curry op)
  (lambda (x) (lambda (y) (op x y))))

(define add1 ((curry +) 1))

; assume lst is a list of numbers with no duplicates
(define (quick gt lst)
  (if (null? lst)
      null
      (let* (
            (pivot (first lst))
            (le (compose not gt))
            (lt (lambda (x y) (and (not (equal? x y)) (le x y))))
            (left   (filter ((curry gt) pivot) lst))
            (right  (filter ((curry lt) pivot) lst))
            (pivots (filter ((curry equal?) pivot) lst))
            )
        (append (quick gt left) pivots (quick gt right))
      )
  )
)
