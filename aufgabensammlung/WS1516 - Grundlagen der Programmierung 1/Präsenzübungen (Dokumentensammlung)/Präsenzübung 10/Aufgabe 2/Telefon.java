/**
 * Implementiert eine Telefonnummer.
 */
class Telefon implements HasKey {

    String name;
    int telefonnr;

    /**
     * Legt ein neues Telefon-Objekt an.
     */
    Telefon(String n, int tel) {
        name = n;
        telefonnr = tel;
    }

    public String getKey() {
        return name;
    }

    public String toString() {
        return "( " + name + " : " + telefonnr + " )";
    }
}