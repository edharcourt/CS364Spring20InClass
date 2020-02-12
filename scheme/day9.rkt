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

(define test (shuffle (for/list ([i 100]) i)))

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

; the only reason this works is because + can take three arguements
(treefold + 0 bst)

; counting the nodes in a tree
(treefold (lambda (root left right) (+ 1 left right)) 0 bst)

(define (treemap f t)
  (if (null? t)
      null
      (make-tree (f (root t))
                 (treemap f (left t))
                 (treemap f (right t)))))

