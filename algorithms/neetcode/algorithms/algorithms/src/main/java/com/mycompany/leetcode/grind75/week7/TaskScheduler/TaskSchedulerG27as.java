package com.mycompany.leetcode.grind75.week7.TaskScheduler;

public class TaskSchedulerG27as {
    public int leastInterval(char[] tasks, int n) {
        int[] counter = new int[26];
        int max = 0;
        int maxCount = 0;
        for(char task : tasks) {
            counter[task - 'A']++;
            if(max == counter[task - 'A']) {
                maxCount++;
            } else if(max < counter[task - 'A']) {
                max = counter[task - 'A'];
                maxCount = 1;
            }
        }

        int partCount = max - 1;
        int partLength = n - (maxCount - 1);
        int emptySlots = partCount * partLength;
        int availableTasks = tasks.length - max * maxCount;
        int idles = Math.max(0, emptySlots - availableTasks);

        return tasks.length + idles;
    }

    public static void main(String[] args) {
        TaskSchedulerG27as obj = new TaskSchedulerG27as();
        char[] tasks = {'A','A','A','B','B','B'};
        int n = 2;
        System.out.println(obj.leastInterval(tasks, n));
    }
}
