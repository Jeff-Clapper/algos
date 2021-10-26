// Remove Neg: given array, remove negatives and return original array
function removeNegatives(arr) {
    for(var ind=arr.length-1;ind>=0; ind--) {
        // console.log('stuck in for')
        if(arr[ind] < 0) {
            // console.log('stuck in for-if')
            for(var index=ind; index < arr.length; index++) {
                // console.log('stuck in for-if-for')
                arr[index] = arr[index+1]
            }
            arr.length = arr.length-1
        }
    }
    return arr
}

//Second-to-Last: Return the second-to-last element of an array. Given [42,true,4,"Kate",7], return "Kate". If array is too short, return null.
function secondToLast(arr) {
    if (arr.length > 1) {
        return arr[arr.length-2]
    }
    return null
}

//Second-Largest: Return the second-largest element of an array. Given [42,1,4,Math.PI,7], return 7. If the array is too short, return null.
//WOULD LIKE TO REFINE INITIATION AS NULL/NONE IS > -1
function secondLargest(arr) {
    if (arr.length > 1 ){
        var largest = -100000000000000000000000000000000000000000000000000000000000
        var second_largest = -100000000000000000000000000000000000000000000000000000000000
        for(var ind = 0; ind<arr.length;ind++) {
            if (arr[ind] > largest){
                second_largest = largest
                largest = arr[ind]
            }
            else if(arr[ind] > second_largest) {
                second_largest = arr[ind]
            }
        }
        return second_largest
    }
    return null
}
