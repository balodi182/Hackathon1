void setup() {
  Serial.begin(9600);
  Serial.println("Setup Done");
  pinMode(D4,OUTPUT);
}
String values[7];


void loop() {
  if (Serial.available()) {
    String receivedString = Serial.readStringUntil('\n'); // Read until newline character
    
    // Print the received string for verification
    
    
    // Parsing the received string
    if (receivedString=="Give ID"){
      Serial.println("ID: 12");}
    
    int pos = 0;
    int index = 0;
    while ((pos = receivedString.indexOf(',')) != -1) { // Break the string at each comma
      values[index] = receivedString.substring(0, pos); // Extract substring
      receivedString = receivedString.substring(pos + 1); // Remove processed part from the string
      index++;
    }
    // Last part of the string (without comma)
    values[index] = receivedString;
    int Step,Direction,M1,M2,M3,Humidity,Buzzer;

    // Print the parsed values for verification
    for (int i = 0; i < 7; i++) {
      
      
      String val = values[i];
      if (val.startsWith("Step: ")) {
        Step = val.substring(6).toInt(); // Extract step value
        

      } else if (val.startsWith("Direction: ")) {
        Direction = val.substring(11).toInt(); // Extract direction value
        
      }
      else if (val.startsWith("M1: ")) {
        M1 = val.substring(4).toInt(); // Extract direction value
        
      }
      else if (val.startsWith("M2: ")) {
        M2 = val.substring(4).toInt(); // Extract direction value
        
      }
      else if (val.startsWith("M3: ")) {
        M3 = val.substring(4).toInt(); // Extract direction value
        
      }
      else if (val.startsWith("Humidity: ")) {
        Humidity = val.substring(10).toInt(); // Extract direction value
        
      }
      else if (val.startsWith("Buzzer: ")) {
        Buzzer = val.substring(8).toInt(); // Extract direction value
        
      }
    if (Direction==-1){
      digitalWrite(D4,HIGH);

    }
    else if (Direction==1){
      digitalWrite(D4,LOW);
    }
    }
  }
  
}
