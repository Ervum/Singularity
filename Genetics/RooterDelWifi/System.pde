float v = 10;

int vs = 500;

float[][] k = new float[vs][2];

int[] kss = new int[vs];

int[] time = new int[vs];

int dt = 1;

int o = 3;

int contador;

int[] a = {0};

int[] lugar = new int[vs];

int[] lugars = new int[vs];

int n = 1;

int golpes = 0;;

float c = 1;

float l = 0.1;

int mut = 20;

int kssss;

boolean uwu = true;

poblacion pob; 

ArrayList<nn> Brains = new ArrayList<nn>(vs);

ArrayList<player> p2s = new ArrayList<player>(vs);

ArrayList<ball> balls = new ArrayList<ball>(vs);

historial historial = new historial();

int padre, madre;

float ex = 0;

void setup(){

  stroke(0);

  size(800, 900, P2D);

  background(0);

    for(int i = 0; i < vs; i++){

    Brains.add(new nn());

    p2s.add(new player(400, 20, i));

    balls.add(new ball());

    pob = new poblacion();

  }

}

void draw(){

background(0);

pob.start();

pob.mejores();

if(kssss == 1){

  a = historial.actualizar(max(time));

}

text(max(a), 400, 450);

//pob.nuevaG();

pob.reproducir(); 

text("Generacion" + ":   " +n, 400, 900); 

text("golpes" + ":  " +golpes, 400, 890); 

      //text("salida1: " +k[0][0], 20, 20);

      //text("salida2: "+ k[0][1], 20, 40);

     // text("entrada1: " + owo.x/800, 20, 60);

      //text("entrada2: " + owo.y/900, 20, 80);

      //text("entrada3: " + dist(owo.x, owo.y, ewe.x + 50, ewe.y + 5)/1204, 20, 100);

}

void mostrar(){

  if(keyPressed){

    if(key == 'a'){

      uwu = true;

      //l = l + 0.1;

      //mut = mut + 1;

      //key = 'b';

    }

    if(key == 's'){

      uwu = false;

      //l = l - 0.1;

      //mut = mut - 1;

      

    }

    if(key == 'm'){

    mut  = mut + 1; 

    key = 'b';

    }

    if(key == 'n'){

    mut  = mut - 1; 

    key = 'b';

    }

    if(key == 'l'){

    l  = l + 0.1; 

    key = 'b';

    }

    if(key == 'k'){

    l  = l - 0.1; 

    key = 'b';

    }

  }

}

