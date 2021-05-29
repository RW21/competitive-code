#lang racket

(define s (symbol->string (read)))

(define count-substring 
 (compose length regexp-match*))

(display (count-substring "ZONe" s))
