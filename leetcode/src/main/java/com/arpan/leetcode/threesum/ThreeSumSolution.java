package com.arpan.leetcode.threesum;

import java.util.*;
import java.util.stream.Collectors;

public class ThreeSumSolution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;

        Set<Integer> numSet = new HashSet<>();
        Arrays.stream(nums).forEach(numSet::add);

        Map<Integer, List<Integer>> twoSum = new HashMap<>();
        int sum = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {

                sum = -(nums[i] + nums[j]);
                System.out.println("Pair: " + nums[i] + " " + nums[j] + " Sum: " + sum);
                twoSum.put(sum, Arrays.asList(nums[i], nums[j]));
            }
        }

        Set<Triplet> tripletSet = new HashSet<>();
        twoSum.forEach((k, v) -> {
            if (numSet.contains(k)) {
                List<Integer> triplets = new ArrayList<>(v);
                triplets.add(k);
                Collections.sort(triplets);
                tripletSet.add(new Triplet(triplets));
            }
        });

        return tripletSet.stream().map(triplet -> Arrays.asList(triplet.a, triplet.b, triplet.c)).collect(Collectors.toList());
    }

    class Triplet {
        int a;
        int b;
        int c;

        public Triplet(List<Integer> nums) {
            this.a = nums.get(0);
            this.b = nums.get(1);
            this.c = nums.get(2);
        }

        @Override
        public boolean equals(Object obj) {
            if (obj instanceof Triplet) {
                Triplet other = (Triplet) obj;
                return this.a == other.a &&
                    this.b == other.b &&
                    this.c == other.c;
            }
            return false;
        }

        @Override
        public int hashCode() {
            return 31 * a + 59 * b + 101 * c;
        }
    }
}
