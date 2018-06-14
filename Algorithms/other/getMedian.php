<?php

    function getMedian (array $numberList) {
        sort($numberList);
        $sizeOfNumberList = sizeof($numberList);
        if ($sizeOfNumberList % 2 == 0) {
            return ($numberList[$sizeOfNumberList / 2] + $numberList[$sizeOfNumberList / 2 - 1]) / 2;
        }
        return $numberList[($sizeOfNumberList - 1) / 2 ];
    }
