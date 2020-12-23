int pin_Out_S0 = 8;
int pin_Out_S1 = 9;
int pin_Out_S2 = 10;
int pin_Out_S3 = 11;
int pin_In_Mux1 = A0;
int Mux1_State[17] = {0};

int pin_In_Mux2 = A1;
int Mux2_State[17] = {0};


void setup() {
  pinMode(pin_Out_S0, OUTPUT);
  pinMode(pin_Out_S1, OUTPUT);
  pinMode(pin_Out_S2, OUTPUT);
  pinMode(pin_Out_S3, OUTPUT);

  //pinMode(pin_In_Mux1, INPUT);
  Serial.begin(9600);
}

void loop() {
  updateMux();
  for(int i = 0; i < 17; i ++) {
    if(i == 16) {
      int pin_In_Mux1 = A0;
      int pin_In_Mux2 = A1;
      Serial.println();

      
    } else {

      //Serial.print(Mux1_State[i]);
      Serial.print((Mux1_State[i])  * 0.5 , 0);
      Serial.print(";");
      Serial.print(round(Mux2_State[i]) * 0.9, 0);
      Serial.print(";");
    }
  }
}

void updateMux () {
  for (int i = 0; i < 16; i++){
    digitalWrite(pin_Out_S0, HIGH && (i & B00000001));
    digitalWrite(pin_Out_S1, HIGH && (i & B00000010));
    digitalWrite(pin_Out_S2, HIGH && (i & B00000100));
    digitalWrite(pin_Out_S3, HIGH && (i & B00001000));

    Mux1_State[i] = analogRead(pin_In_Mux1);
    Mux2_State[i] = analogRead(pin_In_Mux2);
  }
}
