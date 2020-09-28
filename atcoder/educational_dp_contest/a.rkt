#lang racket

(define n (read))

(define h
  (list->vector
     (for/list ([i (in-range n)])
       (read))))

(define (min a b)
  (if (< a b)
      a
      b))

(define dp
  (let ([vec (make-vector n)])
    (vector-set! vec 1 (abs (- (vector-ref h 1) (vector-ref h 0))))
    (for ([i (in-range 2 n)])
      (vector-set! vec i (min
                          (+ (vector-ref vec (sub1 i)) (abs (- (vector-ref h i)
                                                               (vector-ref h (sub1 i)))))
                          (+ (vector-ref vec (- i 2)) (abs (- (vector-ref h i)
                                                              (vector-ref h (- i 2))))))
                   )) vec)
  )

(print (vector-ref dp (sub1 n)))
