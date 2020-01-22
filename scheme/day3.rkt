#lang racket

(let ((a 10) (b 11)) (+ a b))

; translate the let definition above into a lambda expression
; where 10 and 11 bind to a and b

((lambda (a b) (+ a b)) 10 11) 

(let ((a 10)) (let ((b 11)) (+ a b)))

; translate this into lambda notation

((lambda (a) ((lambda (b) (+ a b)) 11)) 10)
 

; (define (% a b) (remainder a b))
(define % remainder)

(define // quotient)

; linearly recursive 
(define (sod n)
  (if (= n 0)
      0
      (+ (% n 10) (sod (// n 10)))))

; ;iteratively recursive
(define (sum-of-digits n)
  (define (sod1 n acc)
    (if (= n 0)
        acc
        (sod1 (// n 10) (+ acc (% n 10)))))
  
  (sod1 n 0))


(define (pow x y)
  (if (= y 0)
      1
      (* x (pow x (- y 1)))))

; rewrite pow into an iterative power function.
(define (power x y)
  (define (pow x y acc)
    (if (= y 0)
        acc
        (pow x (- y 1) (* acc x))))
  (pow x y 1))

; list
(define loc '(9 1 8 89 "hello" (4 3 "fred") 2 3.14159))

; compute the length of the list of type T
(define (len lot)
  (if (null? lot)
      0
      (+ 1 (len (rest lot)))))

; rewrite len so it is iteratively recursive

; write a function list-of-numbers that returns true if the
; list passed contains only numbers
(define (list-of-numbers? lot)
   (if (null? lot)
       true
       (and (number? (first lot)) (list-of-numbers? (rest lot)))))

; iteratively recursive
(define (lon? lot)
  (if (null? lot)
      true
      (if (not (number? (first lot)))
          false
          (lon? (rest lot)))))












