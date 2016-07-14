class Bildschirm{

  Bildschirm(int z,int sp){ //erzeugt Bildschirmspeicher 
    zeilen = z; 
    spalten = sp; 
    arr = new char[zeilen][spalten]; 
	clear();
  }

  void punkt(int x,int y){ //speichert Punkt
    punkt(x,y,'*'); 
  }

  void hlinie(int xmin,int y,int xmax){ //speichert horizontale Linie
    punkt(xmin,y,'-'); 
    if(xmin<xmax){ 
      hlinie(xmin+1,y,xmax);
    }
  }

  void vlinie(int x,int ymin,int ymax){ //speichert vertikale Linie
    punkt(x,ymin,'|'); 
    if (ymin<ymax){
      vlinie(x,ymin+1,ymax);
    }
  }  

  void rechteck(int xmin,int ymin,int xmax,int ymax){ // speichert Rechteck
    clearRechteck(xmin,ymin,xmax,ymax) ; 
    hlinie(xmin,ymin,xmax);
    hlinie(xmin,ymax,xmax); 
    vlinie(xmin,ymin,ymax);
    vlinie(xmax,ymin,ymax); 
    punkt(xmin,ymin,'+');
    punkt(xmin,ymax,'+'); 
    punkt(xmax,ymin,'+');
    punkt(xmax,ymax,'+'); 
  }

  void clear(){ // loescht Bildschirmspeicher
    clearRechteck(0,0,spalten-1,zeilen-1);
  }

  void display(){ // zeigt Bildschirmspeicher an 
    for ( int z=zeilen-1 ; z>=0 ; z--){ 
      for ( int sp=0 ; sp<spalten ; sp++){ 
	    System.out.print( arr[z][sp]);
      }
      System.out.println(); 
    }
  }

  private int zeilen, spalten; 
  private char[][] arr;

  private void punkt(int x,int y,char c){
    if ( 0<=y && y<zeilen && 0<=x && x< spalten ){
      arr[y][x]=c;
    }
  }

  private void clearRechteck(int x,int y, int xmax,int ymax){
    for ( int s=x ; s<=xmax ; s++ ){
      for ( int z=y; z<=ymax ; z++ ){ 
	    arr[z][s] = ' ';
      }
    }
  }
}

// hier sollten Ihre Klassen fuer die benoetigten geometrische Objekte folgen
// und eine Testklasse zur Implementation der main-Methode