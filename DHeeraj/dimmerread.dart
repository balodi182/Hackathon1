int Dimmer = 4000; // Initialize Dimmer variable

void setup() {
  Serial.begin(9600); // Start serial communication with the built-in serial port
  delay(2000); // Wait for serial port to stabilize
  pinMode(D4,OUTPUT);
}

void loop() {
  

  if (Serial.available()) { // Check if data is available on the software serial port
    String data = Serial.readStringUntil('\n'); // Read the incoming data
    if (data=="Give ID"){
      Serial.println("ID: 11");}

    else if (data.startsWith("Dimmer: ")) { 
      Dimmer = data.substring(8).toInt(); // Extract the value after "Dimmer: " and convert it to integer
      
    }
    if (Dimmer==4000){
      digitalWrite(D4,HIGH);
      delay(500);
      digitalWrite(D4,LOW);
      delay(500);
    }
  }
}
