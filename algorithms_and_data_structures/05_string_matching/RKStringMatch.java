public class RKStringMatch extends StringMatch {
    // d is the number of characters in input alphabet
    public final static int d = 256;

    public int match(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int i;
        int j;
        int p = 0; // hash value for pattern
        int t = 0; // hash value for text
        int h = 1;

        if (n < m) return -1; // no match is possible

        // value of h would be pow(d, M-1)%256 - for use in removing leading digit
        for (i = 0; i < m - 1; i++) {
            h = (h * d) % 256;
        }

        // calculate the hash value for pattern and first window of text
        for (i = 0; i < m; i++) {
            counter.add(2);
            p = (d * p + pattern.charAt(i)) % 256;
            t = (d * t + text.charAt(i)) % 256;
        }

        // slide the pattern over the text by one
        for (i = 0; i <= n - m; i++) {
            // check the hash values of current window of text and pattern
            // if the hash values match then check characters one by one
            if (p == t) {
                // check characters one by one
                for (j = 0; j < m; j++) {
                    counter.add(2);
                    if (text.charAt(i + j) != pattern.charAt(j)) {
                        break;
                    }
                }
                // if p == t and pattern[0...m-1] = txt[i, i+1, ...i+m-1]
                if (j == m) {
                    return i;
                }
            }

            // calculate the hash value for next window of text
            // remove leading digit, add trailing digit
            // rolling hash
            if (i < n - m) {
                t = (d * (t - text.charAt(i) * h) + text.charAt(i + m)) % 256;

                // we might get negative value of t, convert it to positive
                if (t < 0) {
                    t = t + 256;
                }
            }
        }
        return -1;
    }
}
