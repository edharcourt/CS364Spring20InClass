#lang racket

(define SQR (λ (x) (* x x)))

; Write the function f2c in Scheme c = 5/9*(f - 32)

(define f2c (lambda (f) (* (/ 5 9) (- f 32))))

; define the function investment
(define inv (lambda (c r t n) (* c (expt (+ 1 (/ r n)) (* t n)))))
