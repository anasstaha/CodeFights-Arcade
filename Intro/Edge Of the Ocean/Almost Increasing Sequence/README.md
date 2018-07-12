Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

__Example__

    For sequence = [1, 3, 2, 1], the output should be
    almostIncreasingSequence(sequence) = false.

    There is no one element in this array that can be removed in order to get a strictly increasing sequence.

    For sequence = [1, 3, 2], the output should be almostIncreasingSequence(sequence) = true.

    You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

__Input/Output__

* __[execution time limit] 4 seconds (py3)__

* __[input] array.integer sequence__

    Guaranteed constraints:<br />
    2 ≤ sequence.length ≤ 105, <br />
    -105 ≤ sequence[i] ≤ 105.

__[output] boolean__

   Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.