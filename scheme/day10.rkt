#lang racket

; A binary search tree
;   1) is either empty
;   2) or contains data with a left binary search
;      tree and a right binary search tree
;   The data in the left node is "less than" the root and the
;   data in the right node is "greater than" the root

; helper functions

(define t1 '(3 () ()))
(define t2 (list 5 t1 (list 6 null null)))

;(define (root t) (first t))
;(define (left t) (first (rest t))) ;; cadr
(define root car)
(define left cadr)
(define right caddr)

; precond; left and right are binary trees
(define (make-tree root left right)
  (list root left right))

; precond: t is a binary search tree
;          data is a number (temporary assumption)
;          assume data not already in tree (can fix later)
(define (insert data t)
  (cond 
         [(null? t) (make-tree data null null)]
         [(< data (root t))
            (make-tree (root t) (insert data (left t)) (right t))]
         [(> data (root t))
            (make-tree (root t) (left t) (insert data (right t)))]
         [else
            (error "already exists in tree" data)]
  )
)

(define test (shuffle (for/list ([i 10]) i)))

; insert each item in list into a tree
; return resulting tree
(define (insert-all lst)
  (if (null? lst)
      null
      (insert (first lst) (insert-all (rest lst)))))


(define (insert-all-with-a-fold lst)
  (foldr insert null lst))

; t is a binary tree
; return the inorder list
(define (inorder t)
  (if (null? t)
      null
      (append (inorder (left t))
              (list (root t))
              (inorder (right t)))))
      
; write a function that computes the hieght of the binary
; tree
(define (height t)
  (if (null? t)
      -1
      (+ 1 (max (height (left t))
                (height (right t)))
      )
  )
)

(define (sum t)
  (if (null? t)
      0
      (+ (root t) (sum (left t)) (sum (right t)))))

(define (treefold op init t)
  (if (null? t)
      init
      (op (root t) (treefold op init (left t))
                   (treefold op init (right t)))))


(define bst (insert-all test))

; add up the values in a tree 
(treefold (lambda (root left right) (+ root left right)) 0 bst)

; the only reason this works is because + can take three arguments
(treefold + 0 bst)

; counting the nodes in a tree
(treefold (lambda (root left right) (+ 1 left right)) 0 bst)

(define (treemap f t)
  (if (null? t)
      null
      (make-tree (f (root t))
                 (treemap f (left t))
                 (treemap f (right t)))))

; quadratic equation
(define (quad a b c)
  (/ (+ (- b) (sqrt (- (* b b) (* 4 (* a c))))) (* 2 a)) 
)

; O(n^2) bad!
(define (preorder t)
  (if (null? t)
      null
      (append (list (root t))
              (preorder (left t))
              (preorder (right t))
      )
  )
)

; linearly recursive O(n) solution
(define (preorder2 t acc)
  (if (null? t)
      acc
      (cons (root t)
            (preorder2 (left t)
                       (preorder2 (right t) acc)))
  )
)

(define (leaf? t)
   (and (null? (left t)) (null? (right t))))
  
; iterative preorder
; stack - list of trees
; acc - list of items
; iteratively recursive because we are not building up
; function calls on the stack.
(define (preorder-iter stack acc)
  (if (null? stack)
    (reverse acc)  ; use good reverse O(n)
    (let* (
           (top (first stack))
           (newacc (cons (root top) acc))
          )
      (cond
          ; no children
        ((leaf? top)
           (preorder-iter (rest stack) newacc))

        ; left child only
        ((null? (right top))
           (preorder-iter (cons (left top) (rest stack)) newacc))  
          ; right child
        ((null? (left top))
           (preorder-iter (cons (right top) (rest stack)) newacc))  
          ; else both children
        (else
           (preorder-iter (cons (left top)
                                (cons (right top) (rest stack))) newacc)
        )
      )
    )
  )
)

; return 1 if a leaf 0 otherwise
(define (leaf t)
   (if (and (null? (left t)) (null? (right t))) 1 0))

(define (count-leaves t)
  (if (null? t)
      0
      (+ (leaf t) (count-leaves (left t)) (count-leaves (right t)))))
          

(define (atoms lst)
  (if (null? lst)
      null
      (if (not (list? (first lst)))
          (cons (first lst) (atoms (rest lst)))
          (atoms (rest lst)))))

(define lst '(1 2 "Hello" (4 5) 6 ()))

(define (is-bt? t)
  (cond
      ((null? t) true)
      ((not (list? t)) false)
      (((compose not =) (length t) 3) false)
      (else
          (and (is-bt? (left t)) (is-bt? (right t))))))




