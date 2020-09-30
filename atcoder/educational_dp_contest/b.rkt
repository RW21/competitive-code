#lang racket

(define n (read))
(define k (read))

(define h
  (for/vector ([i (in-range n)])
    (read)))

(define vec (make-vector n #f))
(vector-set! vec 0 0)

(define (f i)
  (cond
    [(vector-ref vec i) (vector-ref vec i)]
    [else (begin
            ; find best
            (vector-set! vec i
                         (apply min
                          (for/list ([j (in-range 1 (add1 k))]
                                     #:when (>= (- i j) 0))
                            (+ (f (- i j))
                               (abs (- (vector-ref h i) (vector-ref h (- i j))))))))
            (vector-ref vec i))]))

(print (f (sub1 n)))
            
