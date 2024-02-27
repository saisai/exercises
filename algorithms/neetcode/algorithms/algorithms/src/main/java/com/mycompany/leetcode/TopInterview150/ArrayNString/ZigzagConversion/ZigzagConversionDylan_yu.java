package com.mycompany.leetcode.TopInterview150.ArrayNString.ZigzagConversion;

public class ZigzagConversionDylan_yu {

    public String convert(String s, int nRows) {
        char[] c = s.toCharArray();
        int len = c.length;
        StringBuffer[] sb = new StringBuffer[nRows];
        for(int i = 0; i < sb.length; i++) sb[i] = new StringBuffer();

        int i = 0;
        while(i < len) {
            for(int idx = 0; idx < nRows && i < len; idx++) // verticlly down
                sb[idx].append(c[i++]);
            for(int idx = nRows - 2; idx >= 1 && i < len; idx--) // obliquely up
                sb[idx].append(c[i++]);
        }

        for(int idx = 1; idx < sb.length; idx++)
            sb[0].append(sb[idx]);
        return sb[0].toString();
    }

    public static void main(String[] args) {
        String s = "PAYPALISHIRING";
        int numRows = 3;
        ZigzagConversionDylan_yu obj = new ZigzagConversionDylan_yu();
        System.out.println(obj.convert(s, numRows));
    }
}
