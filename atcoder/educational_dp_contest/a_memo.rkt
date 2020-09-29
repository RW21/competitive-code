#lang racket

(define n (read))

(define h
  (for/vector ([i (in-range n)])
    (read)))

(define (min a b)
  (if (< a b) a b))

(define vec (make-vector n #f))
(vector-set! vec 0 0)
(vector-set! vec 1 (abs (- (vector-ref h 0) (vector-ref h 1))))

(define (f i)
  (cond
    [(vector-ref vec i) (vector-ref vec i)]
    [else (begin
            (vector-set! vec i
                         (min (+ (f (sub1 i))
                                 (abs (- (vector-ref h i) (vector-ref h (sub1 i)))))
                              (+ (f (- i 2))
                                 (abs (- (vector-ref h i) (vector-ref h (- i 2)))))))
            (vector-ref vec i))]))

(print (f (sub1 n)))
