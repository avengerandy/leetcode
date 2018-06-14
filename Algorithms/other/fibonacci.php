<?php

    function fibonacciByDynamicProgramming (int $indexOfFibonacci) {
        $fibonacci = [0, 1];
        for($i = 2; $i <= $indexOfFibonacci; $i++){ 
            $fibonacci[$i] = $fibonacci[$i-1] + $fibonacci[$i-2];
        }
        return $fibonacci[$indexOfFibonacci];
    }

    function fibonacciByRecursive (int $indexOfFibonacci) {
        if ($indexOfFibonacci == 0) {
            return 0;
        }
        if ($indexOfFibonacci == 1) {
            return 1;
        }
        return fibonacciByRecursive($indexOfFibonacci - 1) + fibonacciByRecursive($indexOfFibonacci - 2);
    }
