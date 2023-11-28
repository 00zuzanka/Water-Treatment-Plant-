
// LIBRARIES

// OLED libraries:
#include "OLED_Driver.h"
#include "GUI_Paint.h"
#include "DEV_Config.h"
#include "Debug.h"
#include "ImageData.h"

// pH libraries:
#include "DFRobot_PH.h"
#include <EEPROM.h>

// EC libraries:
#include "DFRobot_ECPRO.h"



  // PIN setup
  const int sensorPin = A0; // turbidity sensor
  const int PH_PIN = A1;     // pH sensor
  const int TE_PIN= A2;   // temperature sensor (belonging to EC)
  const int EC_PIN = A3;     // electrical conductivity sensor
  float volt;
  float ntu;
  
  // VARIABLES & CONSTANTS declaration
  
  // OLED screen printout
  UBYTE *BlackImage;
  char buffer[6]; 
  
  // pH parameters
  float voltage,phValue,temperature = 20;
  DFRobot_PH ph;
  
  // EC parameters
  DFRobot_ECPRO ec;
  DFRobot_ECPRO_PT1000 ecpt;

  uint16_t EC_Voltage, TE_Voltage;
  float Conductivity, Temp;
  
  // ARDUINO configuration (runs once on startup):

  void setup()
  {
  // Open serial connection
  Serial.begin(115200);      
    
  // CALIBRATION:
  ec.setCalibration(1.1876); // Replace the 1 with the calibrated K value if it's calibrated Serial.println("Default Calibration K=" + String(ec.getCalibration()))
  Serial.println("Default Calibration K= " + String(ec.getCalibration()));
    
  // Configure pin functionality:
  pinMode(sensorPin, INPUT); 
  pinMode(PH_PIN, INPUT);
  pinMode(TE_PIN, INPUT);
  pinMode(EC_PIN, INPUT);
  System_Init();
  Serial.print(F("OLED_Init()...\r\n"));
  OLED_0in96_Init();
  Driver_Delay_ms(500); 
  OLED_0in96_clear(); 

  // Create a new image cache
  UWORD Imagesize = ((OLED_0in96_WIDTH%8==0)? (OLED_0in96_WIDTH/8): (OLED_0in96_WIDTH/8+1)) * OLED_0in96_HEIGHT;
  if((BlackImage = (UBYTE *)malloc(Imagesize)) == NULL) { 
      Serial.print("Failed to apply for black memory...\r\n");
      return -1;
  }
  
  Serial.print("Paint_NewImage\r\n");
  Paint_NewImage(BlackImage, OLED_0in96_WIDTH, OLED_0in96_HEIGHT, 90, BLACK);  

  //1.Select Image
  Paint_SelectImage(BlackImage);
  Paint_Clear(BLACK);
  Driver_Delay_ms(500); 

  ph.begin();
  //ph.calibration(voltage,temperature);           // calibration process by Serial CMD

  }
  
  
  // ARDUINO main loop (continuous):
  
  void loop()
  {
  // Read and calculate turbidity   
  volt = 0;
  for(int i=0; i<800; i++)
  {
      volt += ((float)analogRead(sensorPin)/1023)*5;
  }
  volt = volt/800;
  volt = round_to_dp(volt,2);
  if(volt < 2.5){
    ntu = 3000;
  }else{
   
    ntu = -1120.4*square(volt)+5742.3*volt-4353.8; 
  }
  dtostrf(ntu,6,1,buffer);
  // Draw turbidity to screen
  // Drawing data to image
  Paint_DrawString_EN(10, 0, "Turbidity", &Font16, WHITE, WHITE);
  Paint_DrawString_EN(10, 17, buffer, &Font24, WHITE, WHITE);
  Paint_DrawString_EN(60, 40, "NTU", &Font24, WHITE, WHITE);

  //  Show image to screen
  OLED_0in96_display(BlackImage);
  // Driver_Delay_ms(2000);
  delay(2000);  
  Paint_Clear(BLACK);

    
  // Read and calculate conductivity and T
  EC_Voltage = (uint32_t)analogRead(EC_PIN) * 5000 / 1024;
  TE_Voltage = (uint32_t)analogRead(TE_PIN) * 5000 / 1024;

  Temp = ecpt.convVoltagetoTemperature_C((float)TE_Voltage/1000);
  Conductivity = ec.getEC_us_cm(EC_Voltage, Temp);
  
  

  dtostrf(Conductivity,6,1,buffer);

  // Draw conductivity to screen
  // Drawing data to image
  Paint_DrawString_EN(10, 0, "El.Cond.", &Font16, WHITE, WHITE);
  Paint_DrawString_EN(10, 17, buffer, &Font24, WHITE, WHITE);
  Paint_DrawString_EN(30, 40, "uSv/cm", &Font24, WHITE, WHITE);

  //  Show image to screen
  OLED_0in96_display(BlackImage);
  // Driver_Delay_ms(2000);
  delay(2000);  
  Paint_Clear(BLACK);

  dtostrf(Temp,6,1,buffer);

  // Draw temperature to screen
  // Drawing data to image
  Paint_DrawString_EN(10, 0, "Temp.", &Font16, WHITE, WHITE);
  Paint_DrawString_EN(10, 17, buffer, &Font24, WHITE, WHITE);
  Paint_DrawString_EN(40, 40, "deg C", &Font24, WHITE, WHITE);

  //  Show image to screen
  OLED_0in96_display(BlackImage);
  // Driver_Delay_ms(2000);
  delay(2000);  
  Paint_Clear(BLACK);
  
  // Read and calculate pH 
  voltage = analogRead(PH_PIN)/1024.0*5000;  // read the voltage
  phValue = ph.readPH(voltage,temperature);  // convert voltage to pH with temperature compensation

  dtostrf(phValue,6,1,buffer);

  // Draw pH to screen
  // Drawing data to image
  Paint_DrawString_EN(10, 0, "pH", &Font16, WHITE, WHITE);
  Paint_DrawString_EN(10, 17, buffer, &Font24, WHITE, WHITE);

  //  Show image to screen
  OLED_0in96_display(BlackImage);
  // Driver_Delay_ms(2000);
  delay(2000);  
  Paint_Clear(BLACK);

  // Report all values to Serial-connection
  // REPORT:
  Serial.print("**");
  Serial.print(ntu);
  Serial.print(",");
  Serial.print(Temp);
  Serial.print(",");
  Serial.print(Conductivity);
  Serial.print(",");
  Serial.println(phValue);
  delay(1000);
  }
   
  float round_to_dp( float in_value, int decimal_place )
  {
    float multiplier = powf( 10.0f, decimal_place );
    in_value = roundf( in_value * multiplier ) / multiplier;
    return in_value;
  }
