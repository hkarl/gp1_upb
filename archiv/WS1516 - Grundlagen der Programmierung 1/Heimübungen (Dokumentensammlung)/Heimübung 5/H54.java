public class H54
{
    public static void main(String[] args)
    {
        final int anzJahre = 2, anzMonate = 12, anzWarengruppen = 3,
                  anzFilialen = 4;
        int verkaufszahlen[][][][] =
            new int[anzJahre][anzMonate][anzWarengruppen][anzFilialen];

        // Teil 1: Array mit zufälligen Werten befüllen -
        //         sollen Sie unverändert lassen!
        for (int i = 0; i < anzJahre; i++)
        {
            for (int j = 0; j < anzMonate; j++)
            {
                for (int k = 0; k < anzWarengruppen; k++)
                {
                    for (int l = 0; l < anzFilialen; l++)
                    {
                        verkaufszahlen[i][j][k][l] =
                            (int) (Math.random() * 10);
                    }
                }
            }
        }

        // Teil 2: Statistiken ausgeben - hier sollen Sie etwas programmieren 
        //...
    }
}
