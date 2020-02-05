#lang racket

; create a list of pairs s.t. we pair x with
; each element in s
(define (cart1 x s)
  (if (null? s)
    null
    (cons (list x (first s)) (cart1 x (rest s)))
  )
)

; Can we write cart1 using fold? :-)))))

(define (CART1 x s)
  (foldl (lambda (y r) (cons (list x y) r))  null s)
)

(define (cp s1 s2)
  (if (null? s1)
      null
      (append (cart1 (first s1) s2)  (cp (rest s1) s2))))

; One question on homework will be to write cp using foldr/l

; A second question will be to write cps that takes a list of sets
; and returns the cartesian product of all of the setrs
; For example, sets A, B, C, D      A X B X C X D
; (cps '(A B C D))   ; list of sets is a list of lists
;    a) write recursively
;    b) write using foldr/l


