class Node<E>
{
    E data;
    Node<E> link;

    Node(E d, Node<E> n)
    {
        data = d;
        link = n;
    }
}

class LinList<E>
{
    static int length = 0; // static-Variablen duerfen nicht vom Typ E sein 
    Node<E> start = null;

    public void add(E x)
    {
        length++;
        if (start == null)
        {
            start = new Node<E>(x, null);
        }
        else
        {
            Node<E> pos = start;
            while (pos.link != null)
            {
                pos = pos.link;
            }
            pos.link = new Node<E>(x, null);
        }
    }

    public void drucke()
    {
        Node<E> e = start;
        System.out.println("------------------------");
        while (e != null)
        {
            System.out.print(e.data + " ");
            e = e.link;
        }
        System.out.println();
    }

    public boolean finde(E x)
    {
        Node<E> e = start;
        boolean xGefunden = false;

        while (!xGefunden && e != null)
        {
            xGefunden = e.data.equals(x);
            e = e.link;
        }

        return xGefunden;
    }
}

class Test43GenericList
{
    public static void main(String[] args)
    {
        LinList<Integer> l = new LinList<Integer>();

        l.add(new Integer(1));
        l.add(new Integer(0));
        l.drucke();
        if (l.finde(0))
        {
            System.out.println("0 drin");
        }

        LinList<String> sl = new LinList<String>();

        sl.add(new String("Uni"));
        sl.add(new String("Paderborn"));
        sl.drucke();
        if (sl.finde("Paderborn"))
        {
            System.out.println("Paderborn drin");
        }
    }
}