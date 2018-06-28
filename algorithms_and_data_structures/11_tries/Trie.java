public class Trie {
    public Trie[] children;
    private final char lastChar = '{';

    public Trie() {
        children = new Trie[27];
    }

    /* Adds a word to the trie.
     * @param s word to add
     */
    public void insert(String s) {
        char[] theWord = s.toCharArray();
        Trie t = this;
        for (char c : theWord) {
            t = addLetter(t, c);
        }
        addLetter(t, lastChar);

    }

    /* Adds a letter to the Trie
     * @param t Trie
     * @param c letter to add
     * @return
     * The newly created child Trie of the input Trie in the index of the input character's value minus the offset (= 'a').
     */
    public Trie addLetter(Trie t, char c) {
        if (t.children[c - 'a'] == null)
            t.children[c - 'a'] = new Trie();
        return t.children[c - 'a'];
    }

    /* finds a word in the Trie
     * @param s word to find
	 * @return true if found, false otherwise
	 */
    public boolean query(String s) {
        char[] chars = s.toCharArray();
        Trie t = this;
        for (char c : chars) {
            if (t.children[c - 'a'] == null)
                return false;
            t = t.children[c - 'a'];
        }
        if (t.children[26] == null)
            return false;
        return true;
    }
}


// each node is a 27-element array of Trie objects

// If the set of strings contained in the trie contains a string whose next character at this point is c,
// then the corresponding element of the array should be the child Trie;
// if it does not contain any such string, the corresponding element of the array should be null

// As a special case, you will need to handle the end-of-word character, which we will take as being {

// You will need some kind of non-null Trie to store in the end-of-word (27th) position,
// but you should never need to look inside that Trie.

