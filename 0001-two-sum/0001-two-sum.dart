class Solution {
  List<int> twoSum(List<int> nums, int target) {
    Map<int,int> indexes = {};

    for(int i=0;i<nums.length;i++){
        if(indexes.containsKey(nums[i])){
            int? index = indexes[nums[i]];
            return [index!,i];
        }else{
            indexes[target-nums[i]] = i;
        }
    } 
    return [];   
  }
}