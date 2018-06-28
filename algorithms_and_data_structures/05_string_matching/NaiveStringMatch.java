public class NaiveStringMatch extends StringMatch {
    public int match(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();

        for (int i = 0; i <= n - m; i++) {
            int j;
            for (j = 0; j < m; j++) {
                counter.add(2);
                if (text.charAt(i + j) != pattern.charAt(j)) {
                    break;
                }
            }// mismatch found, break the inner loop
            if (j == m) {
                return i;
            }// match found, i = pattern start index in text
        }
        return -1; // not found
    }
}
