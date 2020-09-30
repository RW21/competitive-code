#lang racket

(define n (read))
(define w (read))

(define weights (make-vector n))
(define values (make-vector n))

(for ([i (in-range (quotient (sub1 n) 2))])
  (vector-set! weights (* 2 i) (read))
  (vector-set! values (add1 (* 2 i)) (read)))

(define dp
  (for/vector ([i (add1 n)])
    (make-vector w)))

(for* ([i (in-range n)]
       [weight-sum (in-range w)])
  (cond
    [(> (vector-ref weights i) weight-sum)
     (vector-set! (vector-ref dp (add1 i)) weight-sum
                  (vector-ref (vector-ref dp i) weight-sum))]
    [else
     (vector-set! (vector-ref dp (add1 i)) weight-sum
                  (max
                   (vector-ref (vector-ref dp i) weight-sum)
                   (+ (vector-ref values i)
                      (vector-ref (vector-ref dp i) (-
                                                     weight-sum
                                                     (vector-ref weights i))))))]))

(print (vector-ref (vector-ref dp n) w))
