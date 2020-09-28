#lang racket                            

(define n (read))

(define a
  (for/sum ([i (in-range 1 n)])
    (quotient (- n 1) i)))

(print a)
