public class VigereneCipher {
    
    public String[] generateTable() {
        String alphabetRoot = "abcdefghijklmnopqrstuvwxyz";
        String cipher[] = new String[26];

        for (int i=0; i < 26; i++) {
            String pt1 = alphabetRoot.substring(i, alphabetRoot.length());
            String pt2 = alphabetRoot.substring(0, i);
            String alphabetTarget = pt1.concat(pt2);
            cipher[i] = alphabetTarget;
            
        }

        return cipher;
    }

    private String switchAlphabetRoot(int times) {
        String alphabetRoot = "abcdefghijklmnopqrstuvwxyz";

        String pt1 = alphabetRoot.substring(times, alphabetRoot.length());
        String pt2 = alphabetRoot.substring(0, times);
        String alphabetTarget = pt1.concat(pt2);

        return alphabetTarget;
    }

    public String encrypt(String keyWord, String message) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        int x, y; 
        char[] encryptedMessage = new char[message.length()];

        for (int i=0; i < keyWord.length(); i++) {
           x = alphabet.indexOf(keyWord.charAt(i));
           y = alphabet.indexOf(message.charAt(i));
           encryptedMessage[i] = switchAlphabetRoot(y).charAt(x);
        }

        return new String(encryptedMessage);
    }
}
