package com.mycompany.leetcode.randomly.dfs;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class KeysAndRoomsBeingHuman94 {
    private void dfs(List<Integer> keysInRoom, int room, List<List<Integer>> rooms, boolean[] visited) {
        visited[room] = true;

        for(Integer i : keysInRoom) {
            if(!visited[i]) {
                dfs(rooms.get(i), i, rooms, visited);
            }
        }
    }

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean visited[] = new boolean[rooms.size()];
        dfs(rooms.get(0), 0, rooms, visited);

        for(int i=0;i<visited.length;i++) {
            if(!visited[i]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Integer[][] rooms2D = {{1},{2},{3},{}};
        List<List<Integer>> rooms = Arrays.stream(rooms2D)
                .map(Arrays::asList)
                .collect(Collectors.toList());
        KeysAndRoomsBeingHuman94 obj = new KeysAndRoomsBeingHuman94();
        System.out.println(obj.canVisitAllRooms(rooms));
    }
}


// https://stackoverflow.com/questions/11447780/convert-two-dimensional-array-to-list-in-java
// https://leetcode.com/u/beingHuman94/
// https://leetcode.com/problems/keys-and-rooms/solutions/1395642/java-dfs-0ms-100-a-tale-of-two-friends-dfs-and-visited-boolean-array/