<?php

    function nextFibonacciByDynamicProgramming($numberOfList) {
        $fibonacci = [0, 1, 1];
        $i = 2;
        foreach ($numberOfList as &$value) {
            if($fibonacci[$i] > $value) {
                $j = 1;
                while ($fibonacci[$i - $j] > $value) $j++;
                $value = $fibonacci[$i - $j + 1];
            } else {
                while ($fibonacci[$i] <= $value) {
                    $i++;
                    $fibonacci[$i] = $fibonacci[$i-1] + $fibonacci[$i-2];
                }
                $value = $fibonacci[$i];
            }
        }
        return $numberOfList;
    }

    var_dump(nextFibonacciByDynamicProgramming([13, 1, 8]));
    