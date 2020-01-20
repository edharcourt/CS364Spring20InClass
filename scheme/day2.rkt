#lang racket
; define the function investment
(define inv (lambda (c r t n) (* c (expt (+ 1 (/ r n)) (* t n)))))

(define (inv2 c r t n) (* c (expt (+ 1 (/ r n)) (* t n))))

((lambda (x) (* x x)) (+ 3 7))

; conditions

(define pass-fail (lambda (average) (if (< average 60) "fail" "pass")))

(define (gpa average)
  (if (>= average 90)
      4
      (if (>= average 80)
          3
          (if (>= average 70)
              2
              (if (>= average 60)
                  1
                  0
              )
          )
      )
  )
)

(define (gpa2 average)
  (cond ((>= average 90) 4)
        ((>= average 80) 3)
        ((>= average 70) 2)
        ((>= average 60) 1)
        (else 0)
  )
)

; Sometimes it is helpful to give a name to a value for readability
(define (area-circ r)
  (let ((pi 3.14159265))
    (* pi (sqr r))
  )
)

; let is called a "special form", it is not primitive and can be
; defined in term of a lambda
(define (area-circ2 r)
  ((lambda (pi) (* pi (sqr r))) 3.14159265)
)

; compute the sum from 1 to n
(define (sum-n n)
  (if (= n 0)
      0
      (+ (sum-n (- n 1)) n)))

; compute x^y = x * x^(y-1)
; base case y = 0 then x^0 = 1
; precondition: conditions on the parameters for the function to
;               work properly.
; We need the most general precondition that we can state.
;  Weakest precondition
; y must be a non-negative integer
; x must be a number
(define (pow x y)
  (if (= y 0)
      1
      (* x (pow x (- y 1)))))

(define (sod n)
  (if (= n 0)
      0
      (+ (remainder n 10) (sod (quotient n 10)))))













