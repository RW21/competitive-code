import java.util.HashMap;
import java.util.Map;

class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> hashmap = new HashMap();

        for (int i : nums){
            if (hashmap.containsKey(i)){
                hashmap.remove(i);
            }else{
                hashmap.put(i,1);
            }
    }
    return hashmap.keySet().iterator().next();

}
}