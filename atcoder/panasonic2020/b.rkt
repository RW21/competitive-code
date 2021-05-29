#lang racket

(define h (read))
(define w (read))

(display (ceiling (/ (* h w) 2)))
