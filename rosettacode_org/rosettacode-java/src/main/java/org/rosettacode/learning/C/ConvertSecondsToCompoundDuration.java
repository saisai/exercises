package org.rosettacode.learning.C;

public class ConvertSecondsToCompoundDuration {
    private String duration(int seconds) {
        StringBuilder string = new StringBuilder();
        if(seconds >= 604_800 /* 1 wk */) {
            string.append("%,d wk".formatted(seconds / 604_800));
        }
        if(seconds >= 86_400 /* 1 d */) {
            if(!string.isEmpty()) string.append(", ");
            string.append("%d d".formatted(seconds / 86_400));
            seconds %= 86_400;
        }
        if (seconds >= 3600 /* 1 hr */) {
            if (!string.isEmpty()) string.append(", ");
            string.append("%d hr".formatted(seconds / 3600));
            seconds %= 3600;
        }
        if (seconds >= 60 /* 1 min */) {
            if (!string.isEmpty()) string.append(", ");
            string.append("%d min".formatted(seconds / 60));
            seconds %= 60;
        }
        if (seconds > 0) {
            if (!string.isEmpty()) string.append(", ");
            string.append("%d sec".formatted(seconds));
        }
        return string.toString();
    }

    private static long addUnit(StringBuilder sb, long sec, long unit, String s) {
        long n;
        if((n = sec / unit) > 0) {
            sb.append(n).append(s);
            sec %= (n * unit);
        }
        return sec;
    }

    private static void compound(long seconds) {
        StringBuilder sb = new StringBuilder();

        seconds = addUnit(sb, seconds, 604800, " wk, ");
        seconds = addUnit(sb, seconds, 86400, " d, ");
        seconds = addUnit(sb, seconds, 3600, " hr, ");
        seconds = addUnit(sb, seconds, 60, " min, ");
        addUnit(sb, seconds, 1, " sec, ");

        sb.setLength(sb.length() > 2 ? sb.length() - 2 : 0);

        System.out.println(sb);
    }

    public static void main(String[] args) {
        ConvertSecondsToCompoundDuration obj = new ConvertSecondsToCompoundDuration();
        System.out.println(obj.duration(7259));
        System.out.println(obj.duration(86400));
        System.out.println(obj.duration(6000_000));

        compound(7259);
        compound(86400);
        compound(6000_000);
    }
}
