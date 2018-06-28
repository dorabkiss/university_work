public class KMPStringMatch extends StringMatch {

    int[] computePrefix(String pattern) {
        int m = pattern.length();
        int[] prefixTable = new int[m];
        prefixTable[0] = 0;
        int k = 0;
        for (int q = 1; q < m; q++) {
            while (k > 0) {
                counter.add(2);
                if (pattern.charAt(k) != pattern.charAt(q)) {
                    k = prefixTable[k - 1];
                } else break;
            }
            if (pattern.charAt(k) == pattern.charAt(q)) {
                k = k + 1;
            }
            counter.add(2);
            prefixTable[q] = k;
        }
        return prefixTable;
    }

    public int match(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();

        if (m == 0) return 0;
        if (n < m) return -1;

        int[] prefixTable = computePrefix(pattern);
        int q = 0;  // Number of chars matched in pattern

        for (int i = 0; i < n; i++) {
            while (q > 0) {
                counter.add(2);
                if (text.charAt(i) != pattern.charAt(q)) {
                    // Fall back in the pattern
                    q = prefixTable[q - 1];  // max overlap
                } else break;
            }
            if (text.charAt(i) == pattern.charAt(q)) {
                // Next char matched, increment position
                q = q + 1;
            }
            counter.add(2);
            if (q == m) {
                return i - m + 1; // match found
            }
        }
        return -1;  // Not found
    }
}

