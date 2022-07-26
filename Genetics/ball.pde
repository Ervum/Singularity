class ball{

  float x = 400 + random(-20, 20);

  float y = 600 +random(-20, 20);

  //float x = 400;

  //float y = 450;

  float vx = 4*pow(-1, int(random(0, 2)));

  float vy = -3;

  int vi = 1;

  int ks = 1;

  int ssuma = 0;

  int dssuma = 1;

  void display(int i){

    //fill((i +o)*ks*255/vs, (i + o)*ks*255/vs, 120);

    fill(255);

         if(i == 0){

      fill(0,120, 150);

    }

    ellipse(x , y, 20, 20);

    //text(i,x-1, y-20);

    //fill((i +20)*ks*255/vs, (i + 20)*ks*255/vs, i*ks*255/vs);

    //fill(255);

    //text(time[i],x-1, y+25);

  }

  void move(){

   x = x + vx;

   y = y + vy;

   //x = mouseX;

   //y = mouseY;

  }

  void collide(int i){

    player p2 = p2s.get(i);

    if(p2.x >= 0){

      if(p2.x <= 800){

      //time[i] = time[i] + dt*vi;

      }

    }

    //time[i] = time[i] + dt*vi;

    if(x <= 0){

      vx = -vx;

    }

    if(x >= 800){

      vx = -vx;

    }

    if(y >= 900){

     vy = -vy;

    }

    if(y <= 0){

      vy = -vy;

      kss[i] = kss[i] + vi;

      vi = 0;

    }

  }

  void Muerte(int i){

    if(kss[i] == 1){

     for(int j = 0; j <Brains.size(); j++){ 

      ssuma = ssuma + kss[j]*dssuma;

    }

     lugar[vs - ssuma] = i;

     lugars[i] = vs - ssuma + 1;

       x = 10000;

       y = 10000;

       dssuma = 0;

    }

   }

}

