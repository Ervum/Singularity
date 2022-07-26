class poblacion{

  int Tiempos;

  int ksss = 0;

  int dsuma = 1;

  int suma = 0;

  int tiempofinal;

 void start(){

    for(int i = 0; i < Brains.size(); i++){

       ball ball = balls.get(i);

       player p2 = p2s.get(i);

    if(uwu == true){

    p2.display(i);

    ball.display(i);

    }else{

      ball owo = balls.get(padre);

      player ewe = p2s.get(padre);

      owo.display(padre);

      ewe.display(padre);

      text("learning rate: " + l, 0, 20);

      text("mut rate: " + mut, 0, 40);

    }

    mostrar();

    ball.move();

    ball.collide(i);

    p2.collide(ball, i);

    p2.IA(i);

    p2.Muerte(i);

    ball.Muerte(i);

    for(int j = 0; j <Brains.size(); j++){ 

      suma = suma + kss[j]*dsuma;

    }

    text("Muertos: " + suma, 700, 900);

    text("Vivos: " + (Brains.size() - suma), 700, 870);

    if(suma ==Brains.size()){

     dsuma = 0;

    }

    else{

    suma = 0;

    }

    for(int k = 0; k < vs; k++){

      //fill((k +o)*1*255/vs, (k + o)*1*255/vs, 120);

      fill(255);

    if(uwu == true){

       //text(k + ":  " +time[k], 0, 20 + 20*k);

       //text("Primer lugar", 50, 20 + 20*y3[0]);

    }else{

       //text(y3[0] + ":  " +time[y3[0]], 0, 20 + 20*y3[0]);

       //text("Primer lugar", 50, 20 + 20*y3[0]);

    }

    }

} 

     text("maximo: " + max(time), 700, 885);

 }

 void mejores(){

   if((suma == Brains.size())&&(ksss == 0)){

            ksss = 1;

            kssss = ksss;

                                           }

 }

 void nuevaG(){

   if(ksss == 1){

     //anterior = time;

}

 }

void reproducir(){

  if(ksss == 1){

  nn Brain = new nn();

  nn Brain2 = new nn();

    for(int i = Brains.size() - 1; i > -1;i = i - 1){

    p2s.remove(i);

    balls.remove(i);

    }

    for(int i = 0; i < Brains.size(); i++){

    p2s.add(new player(400, 20, Brains.size()));

    balls.add(new ball());

    suma = 0;

    

    time[i] = 0; 

    kss[i] = 0;

    dsuma = 1;

    }

       ksss = 0;

       kssss = ksss;

       golpes = 0;

       n = n +1;

       //padre

       ex = random(0, 1);

       for(int i = 0; i < vs; i++){

       //println(ex);

        if(ex >= 1 - pow(0.5, i) ){

        if( ex <=  1 - pow(0.5, i + 1)){

         padre = lugar[i];

        }

        }

       }

       //println(ex);

      //println(padre + "    " + lugars[padre] );

     //madre

     ex = random(0, 1);

     for(int i = 0; i < vs; i++){

        if(ex >= 1 - pow(0.5, i) ){

        if( ex <=  1 - pow(0.5, i + 1)){

         madre = lugar[i];

        }

        }

       }

       

      //Ellite

      if((a[n - 2] == max(a))){

        nn uwur = Brains.get(padre);

        Brains.remove(0);

        Brains.add(0, uwur);

      }

      

     for(int i = 1; (i < Brains.size()); i++){

      Brain =  Brains.get(padre);

      Brain2 = Brains.get(madre);

      nn WTF = Brains.get(i);

     //Reproduccion

     for(int j = 0; j < 4; j++){

       for(int q = 0; q < 3; q++){

       if(int(random(0, 5)) == 1){

        WTF.W1[j][q] = Brain2.W1[j][q];

       }else{

       WTF.W1[j][q] = Brain.W1[j][q];

       }

       }

       for(int q = 0; q < 4; q++){

       if(int(random(0, 5)) == 1){

        WTF.W2[j][q] = Brain2.W2[j][q];

       }else{

       WTF.W2[j][q] = Brain.W2[j][q];

       }

       }

       if(int(random(0, 5)) == 1){

        WTF.b1[j] = Brain2.b1[j];

       }else{

         WTF.b1[j] = Brain.b1[j];

       }

       if(int(random(0, 5)) == 1){

         WTF.b2[j] = Brain2.b2[j];

       }else{

       WTF.b2[j] = Brain.b2[j];

       }

      for(int js = 0; js < 2; js++){

       for(int q = 0; q < 2; q++){

         if(int(random(0, 5)) == 1){

         WTF.W3[js][q] = Brain.W3[js][q];

         }else{

         WTF.W3[js][q] = Brain2.W3[js][q];

         }

         if(int(random(0, 5)) == 1){        

         WTF.b3[q] = Brain.b3[q];

         }else{

         WTF.b3[q] = Brain2.b3[q];

         }

     }

      }

     Brains.remove(i);

     Brains.add(i, WTF);

  }

    }

  for(int is = Brains.size() - 1; (is > 0);is = is - 1){

      nn OMG = Brains.get(is);

         for(int j = 0; j < 4; j++){

      for(int q = 0; q < 3; q++){

       if(int(random(0, (mut*2 + 1))) == 1){

       OMG.W1[j][q] = OMG.W1[j][q] - random(-l,l);

       }else{

       OMG.W1[j][q] = OMG.W1[j][q] + random(-l, l)*0;

       }

      }

     for(int q = 0; q < 4; q++){

       if(int(random(0, (mut*2 + 1))) == 1){

        OMG.W2[j][q] = OMG.W2[j][q] - random(-l, l);

       }else{

       OMG.W2[j][q] = OMG.W2[j][q] + random(-l, l)*0;

       }

     }

       if(int(random(0, (mut*2 + 1))) == 1){

        OMG.b1[j] = OMG.b1[j] - random(-l, l);

       }else{

       OMG.b1[j] = OMG.b1[j] + random(-l, l)*0;

       }

       if(int(random(0, (mut*2 + 1))) == 1){

        OMG.b2[j] = OMG.b2[j] - random(-l, l);

       }else{

       OMG.b2[j] = OMG.b2[j] + random(-l, l)*0;

       }

     }

     for(int j = 0; j < 2; j++){

       for(int q = 0; q < 2; q++){

         if(int(random(0, (mut*2 + 1))) == 1){

       OMG.W3[j][q] = OMG.W3[j][q] - random(-l, l);

         }

         else{

           OMG.W3[j][q] = OMG.W3[j][q] + random(-l, l)*0;

         }

       }

     }

       for(int q = 0; q < 2; q++){

         if(int(random(0, (mut*2 + 1))) == 1){

         OMG.b3[q] = OMG.b3[q] - random(-l, l);

         }else{

         OMG.b3[q] = OMG.b3[q] + random(-l, l);

         }

       }

       //

     Brains.remove(is);

     Brains.add(is, OMG);

  }

}

}

}

