  #include <Wire.h>
  #include <Adafruit_ADS1X15.h>
  #include "Adafruit_AHTX0.h"
  #include <OneWire.h>
  #include <DallasTemperature.h>
  #define ONE_WIRE_BUS 0  //D3

  OneWire oneWire(ONE_WIRE_BUS);
  DallasTemperature sensors(&oneWire);


  Adafruit_AHTX0 aht1;
  Adafruit_ADS1115 ads;  // Create an ADS1115 instance
  #define ADS_ADDRESS 0x48


  //Calibrating 
  const int MPU_addr = 0x68; // I2C address of the MPU-6050

  int16_t gyroX_raw, gyroY_raw, gyroZ_raw;
  float gyroX_dps, gyroY_dps, gyroZ_dps;

  // Calibration constants
  const float zeroOxygenVoltage = 0.0;  // Voltage in air (zero oxygen concentration)
  const float fullOxygenVoltage = 2.5;  // Voltage in calibration gas with full oxygen concentration

  void setup() {
      
      Wire.begin();
      Serial.begin(9600);
      Wire.beginTransmission(0x70);
      Wire.write(1<<7);
      Wire.endTransmission();
      ads.begin(ADS_ADDRESS);
      // Setup AHT10
      Wire.beginTransmission(0x70);
      Wire.write(1<<3);
      Wire.endTransmission();

      

      if (!aht1.begin()) {
          Serial.println("Couldn't find AHT20 sensor!");
          while (1);
      }
      
      // Setup GYRO
      Wire.beginTransmission(0x70);
      Wire.write(1<<2);
      Wire.endTransmission();
      Wire.beginTransmission(MPU_addr);
      Wire.write(0x6B); // PWR_MGMT_1 register
      Wire.write(0);    // set to zero (wakes up the MPU-6050)
      Wire.endTransmission(true);

      // Setup RodTemp
      sensors.begin();

      // Smoke sensor
      pinMode(D6,INPUT);
  }

  void loop() {
      //Identification
      Serial.println("ID: 10");
      



      Wire.beginTransmission(0x70);
      Wire.write(1<<7);
      Wire.endTransmission();
      int16_t adc0 = ads.readADC_SingleEnded(0);  // Read analog input 0
      float voltage = adc0 * 0.000125;  // Convert ADC value to voltage (assuming 4.096V range and 16-bit resolution)

      // Convert voltage to oxygen percentage using linear interpolation
      float oxygenPercentage = mapFloat(voltage, zeroOxygenVoltage, fullOxygenVoltage, 0.0, 100.0);

      Serial.print("OP: ");
      Serial.println(oxygenPercentage);

      //Temperature1
      sensors_event_t humidityEvent1, tempEvent1;
      Wire.beginTransmission(0x70);
      Wire.write(1<<5);
      Wire.endTransmission();
      // Read data from the sensor
      aht1.getEvent(&humidityEvent1, &tempEvent1);
      float temperature1 = tempEvent1.temperature;
      float humidity1 = humidityEvent1.relative_humidity;

      // Print data from the sensor
      Serial.print("T1: ");
      Serial.println(temperature1);
      Serial.print("H1: ");
      Serial.println(humidity1);
      


      //Temperature2
      sensors_event_t humidityEvent2, tempEvent2;
      Wire.beginTransmission(0x70);
      Wire.write(1<<3);
      Wire.endTransmission();
      // Read data from the sensor
      aht1.getEvent(&humidityEvent2, &tempEvent2);
      float temperature2 = tempEvent2.temperature;
      float humidity2 = humidityEvent2.relative_humidity;

      // Print data from the sensor
      Serial.print("T2: ");
      Serial.println(temperature1);
      Serial.print("H2: ");
      Serial.println(humidity1);

      //Temperature3
      sensors_event_t humidityEvent3, tempEvent3;
      Wire.beginTransmission(0x70);
      Wire.write(1<<6);
      Wire.endTransmission();
      // Read data from the sensor
      aht1.getEvent(&humidityEvent3, &tempEvent3);
      float temperature3 = tempEvent3.temperature;
      float humidity3 = humidityEvent3.relative_humidity;

      // Print data from the sensor
      Serial.print("T3: ");
      Serial.println(temperature3);
      Serial.print("H3: ");
      Serial.println(humidity3);


      // Read Gyro
      Wire.beginTransmission(0x70);
      Wire.write(1<<2);
      Wire.endTransmission();

      readGyroData();
      convertToDPS();
      printGyroData();

    // Read RodTemp
    sensors.requestTemperatures();
    float tempC = sensors.getTempCByIndex(0);

    if (tempC == -127.00) {
      Serial.println("Unable to read from sensor");
    } else {
      Serial.print("TR: ");
      Serial.println(tempC);
    }


    //Smoke
    int smoke = analogRead(D6);
    Serial.print("S: ");
    Serial.println(smoke);



    
  }

  // Function for linear interpolation
  float mapFloat(float x, float in_min, float in_max, float out_min, float out_max) {
      return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

  }
  void readGyroData() {
    Wire.beginTransmission(MPU_addr);
    Wire.write(0x43); // starting with register 0x43 (GYRO_XOUT_H)
    Wire.endTransmission(false);
    Wire.requestFrom(MPU_addr, 6, true); // request 6 bytes of data
    
    gyroX_raw = Wire.read() << 8 | Wire.read(); // combine high and low byte
    gyroY_raw = Wire.read() << 8 | Wire.read(); // combine high and low byte
    gyroZ_raw = Wire.read() << 8 | Wire.read(); // combine high and low byte
  }

  void convertToDPS() {
    // Sensitivity for ±250 dps range is 131 LSB/dps
    gyroX_dps = gyroX_raw / 131.0;
    gyroY_dps = gyroY_raw / 131.0;
    gyroZ_dps = gyroZ_raw / 131.0;
  }

  void printGyroData() {
    Serial.print("GX: ");
    Serial.println(gyroX_dps);
    Serial.print("GY: ");
    Serial.println(gyroY_dps);
    Serial.print("GZ: ");
    Serial.println(gyroZ_dps);
  }
