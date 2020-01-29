#lang racket
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
; rewtoe the above using a let to clean it up

(define expr '(+ (* 2 3) (- 4 5)))

; lookup-sym: takes a symbol and returns a function
(define (lookup-sym sym)
  (cond
    ((eq? sym '+) +)
    ((eq? sym '-) -)
    ((eq? sym '*) *)
    (else
       (error "Invalid symbol" sym))))

;(define (left expr) (first (rest expr)))
;(define (right expr) (first (rest (rest expr))))

(define left (compose first rest))
; (define right (compose first (compose rest rest)))
(define right (compose first rest rest))

; expr is an s-list 
(define (eval1 expr)
  (cond
     ((null? expr)
         (error "Invalid expression" expr))
     ((number? expr) expr)
     ((symbol? (first expr))
         ((lookup-sym (first expr))
              (eval1 (left expr))
              (eval1 (right expr))))
     (else
         (error "Invalid expression" expr))
  )
)
      
;(eval1 '(+ 1 2))

; Write a function that sums the numbers in a list
(define (sum lst)
  (if (null? lst)
      0
      (+ (first lst) (sum (rest lst)))))

(define (prod lst)
  (if (null? lst)
      1
      (* (first lst) (prod (rest lst)))))

; reduce a list of things to a single value
(define (reduce f id lst) 
  (if (null? lst)
      id
      (f (first lst) (reduce f id (rest lst)))))






  

