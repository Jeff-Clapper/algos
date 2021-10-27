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

//Nth-to-Last: Return the element that is N-from-array’s-end. Given ([5,2,3,6,4,9,7],3), return 4. If the array is too short, return null.
function xFromEnd(arr,num) {
    if ((arr.length >= num) && (num > -1)) {
        return arr[arr.length-num]
    }
    return null
}

//Nth-Largest: Liam has "N" number of Green Belt stickers for excellent Python projects. Given arr and N, return the Nth-largest element, where (N-1) elements are larger. Return null if needed.
function xLargest(arr,num) {
    if ((arr.length >= num)&&(num >=0)) {
        sortArray(arr);
        return arr[arr.length-num]
    }
    return null
}

function sortArray(arr) {
    for(ind=0; ind<arr.length-1; ind++) {
        count++
        if(arr[ind]>arr[ind+1]) {
            holder = arr[ind]
            arr[ind]=arr[ind+1]
            arr[ind+1] = holder
            sortArraya(arr)
            return arr
        }
    }
}

//Skyline Heights:Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending away. Array [-1,7,3]
//would represent three buildings: first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. 
//Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().
function visibleBuildings(arr) {
    var currMax = 0;
    var buildings = 0
    for(var ind=0;ind<arr.length;ind++) {
        if (arr[ind] > currMax) {
            currMax = arr[ind];
            arr[buildings] = arr[ind];
            buildings++;
        }
    }
    arr.length = buildings;
    return arr;
}