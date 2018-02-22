/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
 //paste look-up table here from References in ES432 folder

#define LED_R 6
#define LED_G 5
#define LED_B 3
#define R_IN A0
#define G_IN A1
#define B_IN A2

int redVal, bluVal, grnVal;
// the setup routine runs once when you press reset:

// Gamma correction for biology
const uint8_t PROGMEM gamma8[] = {
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
    1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
    2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
    5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
   10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
   17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
   25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
   37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
   51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
   69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
   90, 92, 93, 95, 96, 98, 99,101,102,104,105,107,109,110,112,114,
  115,117,119,120,122,124,126,127,129,131,133,135,137,138,140,142,
  144,146,148,150,152,154,156,158,160,162,164,167,169,171,173,175,
  177,180,182,184,186,189,191,193,196,198,200,203,205,208,210,213,
  215,218,220,223,225,228,231,233,236,239,241,244,247,249,252,255 };

void setup() {                
  Serial.begin(9600); //Open Serial Port
}

// the loop routine runs over and over again forever:
void loop() {
  /* Read values from the potentiometers */
  redVal = analogRead(R_IN)/4;   //Divide by 4 in order
  grnVal = analogRead(G_IN)/4;
  bluVal = analogRead(B_IN)/4;
  
  /* Print RGB Values to serial port */
  // Format is: R,G,B
  if(Serial.available>0){
    char c = Serial.read();
    if(c=='p'){
      Serial.print(redVal);
      Serial.print(",");
      Serial.print(grnVal);
      Serial.print(",");
      Serial.println(bluVal);
    }  
  }
  /* Gamma-correct the read values */
  redVal = pgm_read_byte(&gamma8[redVal]);
  grnVal = pgm_read_byte(&gamma8[grnVal]);
  bluVal = pgm_read_byte(&gamma8[bluVal]);
  
  /* Change LED inputs to read values from potentiometers */
  analogWrite(LED_R, redVal);   // turn the LED on (HIGH is the voltage level)               // wait for a second
  analogWrite(LED_G, grnVal);
  analogWrite(LED_B, bluVal);
}
