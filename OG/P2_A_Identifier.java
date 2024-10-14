import java.util.*;

class ident {
    static boolean isValid(String str, int n) {

        // If first character is invalid
        if (!((str.charAt(0) >= 'a' && str.charAt(0) <= 'z')
                || (str.charAt(0) >= 'A' && str.charAt(0) <= 'Z')))
            return false;

        // Traverse the string for the rest of the characters
        for (int i = 1; i < str.length(); i++) {
            if (!((str.charAt(i) >= 'a' && str.charAt(i) <= 'z')
                    || (str.charAt(i) >= 'A' && str.charAt(i) <= 'Z')
                    || (str.charAt(i) >= '0' && str.charAt(i) <= '9')
                    || str.charAt(i) == '_'))
                return false;
        }

        // String is a valid identifier
        return true;
    }

    public static void main(String args[]) {
        System.out.println("Saail Chavan KFPMSCCS016\n");
        System.out.println("Enter a string");
        Scanner c = new Scanner(System.in);
        String str = c.nextLine();
        int n = str.length();

        if (isValid(str, n))
            System.out.println("Identifier");
        else
            System.out.println("Not an Identifier");
    }
}
