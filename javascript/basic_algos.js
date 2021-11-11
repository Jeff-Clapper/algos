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

//Credit Card Validation: Recreate Luhn Formula (formula steps were provided)
function isCreditCardValid(digitArr){
    var total = digitArr[digitArr.length-1]
    digitArr.length -= 1
    
    for(var ind = digitArr.length-1;ind >= 0; ind-=2) {
        digitArr[ind]*=2
    }
    
    for(var ind = 0; ind < digitArr.length; ind++){
        if(digitArr[ind] > 9) {
            digitArr[ind] -= 9
        }
        total += digitArr[ind]
    }
    if(total % 10 == 0){
        return true
    }
    else {
        return false
    }
}

//Remove Blanks: Create a function that, given a string, returns all of that string’s contents, but without blanks. If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".
function removeBlanks(phrase){
    phrase = phrase.split("")
    for(var index = phrase.length-1; index >= 0; index--){
        if (phrase[index] == " ") {
            for(var ind = index; ind < phrase.length; ind++) {
                phrase[ind] = phrase[ind+1];
            }
            phrase.length -= 1 
        }
    }
    phrase = phrase.join("")
    return phrase
}

//Get Digits: Create a JavaScript function that given a string, returns the integer made from the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.
function getDigits(phrase){
    phrase.split("");
    results = []
    for(var index = 0; index < phrase.length; index++) {
        if(parseInt(phrase[index]) % 1==0){
            results.length += 1
            results[results.length-1] = phrase[index]
        }
    }
    results = results.join("")
    results = parseInt(results)
    return results
}

//Acronyms: Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". Given "Live from New York, it's Saturday Night!", return "LFNYISN".
function acronyms(phrase) {
    phrase = phrase.split(" ")
    results = []
    for(var ind = 0;ind < phrase.length; ind++) {
        results.push(phrase[ind][0].toUpperCase())
    }
    results = results.join("")
    return results
}

//Count Non-Spaces: Accept a string and return the number of non-space characters found in the string. For example, given "Honey pie, you are driving me crazy", return 29 (not 35).
function countNonSpaces(phrase) {
    var count = 0;
    for(var index = 0;index < phrase.length; index++) {
        if (phrase[index] !== " ") {
            count++
        }
    }
    return count
}

//Remove Shorter Strings: Given a string array and value (length), remove any strings shorter than the length from the array. 
function removeShorterStrings(phrase,length) {
    phrase = phrase.split(" ");
    console.log(phrase)
    for(var index = phrase.length-1; index >= 0; index--) {
        if(phrase[index].length < length){
            for(var ind = index; ind < phrase.length-1; ind++){
                phrase[ind] = phrase[ind+1];
            }
            phrase.length -=1
        }
    }
    return phrase.join(" ")
}

//given string, returns that string with characters reversed.
function reverseString(statement) {
    var results = ""
    for(var char = statement.length-1; char >= 0; char--) {
        results += statement[char]
    }
    return results
}

// Build a standalone function to remove strings of even lengths from a given array.
function removeEven(arr) {
    for(var ind = arr.length-1; ind >=0; ind--){
        if (arr[ind].length % 2 === 0){
            for(var index = ind; index < arr.length-1;index++ ){
                arr[index] = arr[index+1]
            }
            arr.length--
        } 
    }
    return arr
}

// Given a positive integer that is less than 4000, return a string containing that value in Roman numeral representation
function numToRome(number) {
    modern = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romans = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    results = ""

    var ind = 0
    while (number > 0){
        if(number >= modern[ind]) {
            results += romans[ind]
            number-=modern[ind]
        }
        else{
            ind++
        }
    }
    return results
}

// Given a string containing a Roman numeral representation of a positive integer, return the integer
function romanToInt(roman) {
    var convert = {"M":1000, "CM":900,"D":500, "CD": 400, "C": 100,"XC":90,"L": 50,"XL": 40,"X":10, "IX": 9,"V": 5,"IV": 4,"I": 1}
    var prev 
    var results = 0
    for(var ind=roman.length-1;ind>=0;ind--){
        if(convert[roman[ind]] < prev) {
            results -= convert[roman[ind]]
            prev = convert[roman[ind]]
        }
        else {
            results += convert[roman[ind]]
            prev = convert[roman[ind]]
        }
    }
    return results
}