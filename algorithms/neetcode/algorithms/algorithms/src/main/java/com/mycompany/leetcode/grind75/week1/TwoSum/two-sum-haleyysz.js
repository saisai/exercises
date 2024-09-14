
const twoSumMap = (nums, target) => {
  let map = new Map();

  for(let i = 0; i < nums.length; i++) {
    if(map.has(target - nums[i])) {
      return [map.get(target - nums[i]), i];
    } else {
      map.set(nums[i], i);
    }
  }

  return [];
}

const twoSumObject = (nums, target) => {
  let hash = {};

  for(let i = 0 ;i < nums.length; i++) {
    const n = nums[i];
    if(hash[target - n] != undefined)  {
      return [hash[target - n], i];
    }
    hash[n] = i;
  }

  return [];
};

const nums = [2,7,11,15], target = 9;

console.log(twoSumMap(nums, target));

console.log(twoSumObject(nums, target));

