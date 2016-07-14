public class H52
{
    public static void main(String[] args)
    {
        final int groesse = Integer.parseInt(args[0]);
        int matrix[][] = new int[groesse][groesse];
        int zeile, spalte;

        // Teil 1: Matrix auffuellen - dies sollen Sie unveraendert lassen!
        for (zeile = 0; zeile < groesse; zeile++)
        {
            for (spalte = 0; spalte < groesse; spalte++)
            {
                matrix[zeile][spalte] = (spalte + 1) * 10 + (zeile + 1);
            }
        }

        // Teil 2: Matrix spiegeln - hier sollen Sie etwas programmieren!
        // ...

        // Teil 3: Matrix ausgeben - dies sollen Sie unveraendert lassen! 
        for (zeile = 0; zeile < groesse; zeile++)
        {
            for (spalte = 0; spalte < groesse; spalte++)
            {
                System.out.print("  " + matrix[zeile][spalte]);
            }
            System.out.println();
        }
    }
}