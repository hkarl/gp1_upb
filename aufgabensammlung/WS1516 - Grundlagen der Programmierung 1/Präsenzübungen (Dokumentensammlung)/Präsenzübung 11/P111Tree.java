class Tree
{ 
  int wert ; 
  Tree left, right ; 
  Tree( int i, Tree l, Tree r ) { wert=i ; left=l ; right=r ; }
  String inOrder() { return 
                             ( left==null ? "" : left.inOrder() )  
                             + " " + wert + " " + 
                             ( right==null ? "" : right.inOrder() ) ; 
                   } 

  void insert( int i ) 
  {  if ( i<=wert ) 
          if (left==null) left = new Tree( i , null , null ) ; 
          else left.insert( i ) ; 
     else
          if (right==null) right = new Tree( i , null , null ) ; 
          else right.insert( i ) ; 
  }
}

public class P111Tree
{
   public static void main( String[] args )  // hier startet das Programm 
   {
	Tree t=new Tree( Integer.parseInt( args[0]), null, null ) ; 
	for (int i=1; i<args.length ; i++) 
		t.insert( Integer.parseInt( args[i])) ; 
     System.out.println( t.inOrder() ) ; 
     
   }
}

