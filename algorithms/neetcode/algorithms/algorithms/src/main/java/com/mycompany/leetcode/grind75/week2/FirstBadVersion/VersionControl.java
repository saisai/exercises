package com.mycompany.leetcode.grind75.week2.FirstBadVersion;

public class VersionControl {
    int firstBadVersion;
    boolean isBadVersion(int version) {
        if (version >= firstBadVersion) {
            return true;
        }
        return false;
    }
}

