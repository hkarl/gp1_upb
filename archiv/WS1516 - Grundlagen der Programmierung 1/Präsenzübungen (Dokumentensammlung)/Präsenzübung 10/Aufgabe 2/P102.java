public class P102 {

    public static void main(String[] args) {

		Telefon[] telefonbuch = new Telefon[] {
                new Telefon("Cedric", 12345),
                new Telefon("Sven", 54321),
                new Telefon("Natalie", 12321),
                new Telefon("Thim", 32123),
                new Telefon("Marius", 12312),
                new Telefon("Alex", 32132),
                new Telefon("Oliver", 32131),
                new Telefon("Jonas", 12123)
        };

        sort(telefonbuch);

        for (int i = 0; i < telefonbuch.length; i++) {
            System.out.println(telefonbuch[i]);
        }
        System.out.println("---------------------------------");
    }

    /**
     * Sortiert ein Array von Objekten mit Schluessel.
     */
    static void sort(HasKey[] array) {
        for (int links = 0; links < array.length - 1; links++) {
            int kleinstes = links;
            for (int aktuell = links + 1; aktuell < array.length; aktuell++) {
                if (array[aktuell]
					.getKey()
					.compareTo(array[kleinstes]
					.getKey()) < 0) {
						kleinstes = aktuell;
                }
            }
            tausche(array, kleinstes, links);
        }
    }

    /**
     * Vertauscht zwei Elemente eines Arrays.
     */
    static void tausche(HasKey[] array, int index1, int index2) {
        HasKey hilf = array[index1];
        array[index1] = array[index2];
        array[index2] = hilf;
    }
}
