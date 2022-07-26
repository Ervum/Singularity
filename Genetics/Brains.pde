class nn{

  float xs, ys, xz, yz;

  float[] Y1 = {0., 0., 0., 0.};

  float[] Y2 = {0., 0., 0., 0.};

  float[] Y3 = {0, 0};

  float [][] W1 = {{random(-c, c), random(-c, c), random(-c, c)}, {random(-c, c), random(-c, c), random(-c, c)}, {random(-c, c), random(-c, c), random(-c, c)}, {random(-c, c), random(-c, c), random(-c, c)}};

  float [][] W2 = {{random(-c, c), random(-c, c), random(-c, c), random(-c, c)}, {random(-c, c), random(-c, c), random(-c, c), random(-c, c)}, {random(-c, c), random(-c, c), random(-c, c), random(-c, c)}, {random(-c, c), random(-c, c), random(-c, c), random(-c, c)}};

  float [][] W3 = {{random(-c, c), random(-c, c), random(-c, c), random(-c, c)}, {random(-c, c), random(-c, c), random(-c, c), random(-c, c)}};

  float [] b1 = {random(-c, c), random(-c, c), random(-c, c), random(-c, c)};

  float [] b2 = {random(-c, c), random(-c, c), random(-c, c), random(-c, c)};

  float b3[] = {random(-c, c), random(-c, c)};

  float sigmoid(float w){

    return 1/(1 + exp(-w));

  }

  float[] frontPropagate(ball other, player others){

     xs = other.x;

     ys = other.y;

     xz = others.x;

     yz = others.y;

     float[] X = {xs/800, ys/900, dist(xs, ys, xz + 50, yz + 5)/1204};

    //1

    for(int i = 0; i < 4; i++){

       Y1[i] = sigmoid((W1[i][0]*X[0] + W1[i][1]*X[1] + W1[i][2]*X[2] + b1[i]));

    }

    //2

    for(int i = 0; i < 4; i++){

       Y2[i] = sigmoid(W2[i][0]*Y1[0] + W2[i][1]*Y1[1] + W2[i][2]*Y1[2] + W2[i][3]*Y1[3] + b2[i]);

    }

    for(int i = 0; i < 2; i++){

       Y3[i] = sigmoid(W2[i][0]*Y1[0] + W2[i][1]*Y1[1] + W2[i][2]*Y1[2] + W2[i][3]*Y1[3] + b3[i]);

    }

    return Y3;

     }

}

