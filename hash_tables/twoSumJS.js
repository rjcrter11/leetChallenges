/*
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:

Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/
console.log('Hello')
const twoSum = (nums, target) => {
    const prev = {}

    for (let i = 0; i < nums.length; i++) {
        const current = nums[i];
        const needed = target - current;
        const idx2 = prev[needed];

        if (idx2 != null) return [idx2, i];
        else prev[current] = i
    }
}

twoSum([2, 7, 11, 15]);