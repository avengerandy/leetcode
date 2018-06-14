<?php

    function isSubset($arr1, $arr2) {
        $map = [];
        foreach ($arr2 as $value) $map[$value] = $value;
        foreach ($arr1 as $value) {
            if(isset($map[$value])) unset($map[$value]);
        }
        return sizeof($map) == 0;
    }

    var_dump(isSubset(['A','B','C','D','E'], ['A','E','D']));
    var_dump(isSubset(['A','B','C','D','E'], ['A','D','Z']));
    var_dump(isSubset(['A','D','E'], ['A','A','D','E']));
