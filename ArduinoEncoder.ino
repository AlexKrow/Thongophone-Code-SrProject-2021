//This file is the sketch used on ALL 3 Microcontrollers for the Thongophone.
//Determines what pin to set to HIGH (solenoid to fire) based on character taken in from the RPi.
//This sketch works for both live play and midi file play.

//Author: Deaja Vital

// defining solenoid pins
const int SOL1 = 7;
const int SOL2 = 33; 
const int SOL3 = 6; 
const int SOL4 = 32; 
const int SOL5 = 5;
const int SOL6 = 31; 
const int SOL7 = 4;
const int SOL8 = 30; 
const int SOL9 = 3;
const int SOL10 = 29;
const int SOL11 = 2;
const int SOL12 = 28;

void setup() 
{ 

  pinMode (SOL1, OUTPUT); // Set Arduino board pin to output
  pinMode (SOL2, OUTPUT); // Set Arduino board pin to output
  pinMode (SOL3, OUTPUT); // Set Arduino board pin to output
  pinMode (SOL4, OUTPUT); // Set Arduino board pin to output
  pinMode (SOL5, OUTPUT); // Set Arduino board pin to output
  pinMode (SOL6, OUTPUT); // Set Arduino board pin to output
  pinMode (SOL7, OUTPUT); // Set Arduino board pin to output
  pinMode (SOL8, OUTPUT); // Set Arduino board pin to output
  pinMode (SOL9, OUTPUT); // Set Arduino board pin to output
  pinMode (SOL10, OUTPUT); // Set Arduino board pin to output
  pinMode (SOL11, OUTPUT); // Set Arduino board pin to output
  pinMode (SOL12, OUTPUT); // Set Arduino board pin to output
  
  digitalWrite (SOL1, LOW); // Set Arduino board pin to LOW
  digitalWrite (SOL2, LOW); // Set Arduino board pin to LOW
  digitalWrite (SOL3, LOW); // Set Arduino board pin to LOW
  digitalWrite (SOL4, LOW); // Set Arduino board pin to LOW
  digitalWrite (SOL5, LOW); // Set Arduino board pin to LOW
  digitalWrite (SOL6, LOW); // Set Arduino board pin to LOW
  digitalWrite (SOL7, LOW); // Set Arduino board pin to LOW
  digitalWrite (SOL8, LOW); // Set Arduino board pin to LOW
  digitalWrite (SOL9, LOW); // Set Arduino board pin to LOW
  digitalWrite (SOL10, LOW); // Set Arduino board pin to LOW
  digitalWrite (SOL11, LOW); // Set Arduino board pin to LOW
  digitalWrite (SOL12, LOW); // Set Arduino board pin to LOW

  // Setting data rate for data transmission
  Serial.begin(9600); 

} 

void loop() 
{ 

  // Checks if there is data from serial port
  if (Serial.available() > 0) 
  { 

    // Read the incoming data and store in the character data
    char data = Serial.read();

    // ------- Note on ---------
      // If A is recieved
      // Note A
      if (data == 'A')
      {
        // Turn on solenoid 1 
        digitalWrite(SOL1, HIGH);
      }
          
      // If H is recieved
      // Note #A
      else if (data == 'H')
      {
        // Turn on solenoid 2
        digitalWrite(SOL2, HIGH);
      }
      // If B is recieved
      // Note B
      else if (data == 'B')
      {
        // Turn on solenoid 3
        digitalWrite(SOL3, HIGH);
      }
          
      // If C is recieved
      // Note C
      else if (data == 'C')
      {
        // Turn on solenoid 4
        digitalWrite(SOL4, HIGH);
      }
          
      // If I is recieved
      // Note C#
      else if (data == 'I')
      {
        // Turn on solenoid 5 
        digitalWrite(SOL5, HIGH);
      }
          
      // If D is recieved
      // Note D
      else if (data == 'D')
      {
        // Turn on solenoid 6
        digitalWrite(SOL6, HIGH);
      }
          
      // If J is recieved 
      // Note D#
      else if (data == 'J')
      {
        // Turn on solenoid 7
        digitalWrite(SOL7, HIGH);
      }
          
      // If E is recieved
      // Note E
      else if (data == 'E')
      {
        // Turn on solenoid 8
        digitalWrite(SOL8, HIGH);
      }
          
      // If F is recieved
      // Note F
      else if (data == 'F')
      {
        // Turn on solenoid 9
        digitalWrite(SOL9, HIGH);
      }
          
      // If K is recieved
      // Note F#
      else if (data == 'K')
      {
        // Turn on solenoid 10
        digitalWrite(SOL10, HIGH);
      }
          
      // If G is recieved
      // Note G
      else if (data == 'G')
      {
        // Turn on solenoid 11
        digitalWrite(SOL11, HIGH);
      }
          
      // If L is recieved
      // Note G#
      else if (data == 'L')
      {
        // Turn on solenoid 12
        digitalWrite(SOL12, HIGH);
      }

    // ------- Note off ---------
      // If a is recieved
      // Note A
      else if (data == 'a')
      {
        // Turn off solenoid 1
        digitalWrite(SOL1, LOW);
      }
          
      // If h is recieved
      // Note A#
      else if (data == 'h')
      {
        // Turn off solenoid 2
        digitalWrite(SOL2, LOW);
      }
      // If b is recieved
      // Note B
      else if (data == 'b')
      {
        // Turn off solenoid 3
        digitalWrite(SOL3, LOW);
      }
          
      // If c is recieved
      // Note C
      else if (data == 'c')
      {
        // Turn off solenoid 4
        digitalWrite(SOL4, LOW);
      }
          
      // If i is recieved
      // Note C#
      else if (data == 'i')
      {
        // Turn off solenoid 5
        digitalWrite(SOL5, LOW);
      }
          
      // If d is recieved
      // Note D
      else if (data == 'd')
      {
        // Turn off solenoid 6
        digitalWrite(SOL6, LOW);
      }
          
      // If j is recieved
      // Note D#
      else if (data == 'j')
      {
        // Turn off solenoid 7
        digitalWrite(SOL7, LOW);
      }
          
      // If e is recieved
      // Note E
      else if (data == 'e')
      {
        // Turn off solenoid 8
        digitalWrite(SOL8, LOW);
      }
          
      // If f is recieved
      // Note F
      else if (data == 'f')
      {
        // Turn off solenoid 9
        digitalWrite(SOL9, LOW);
      }
          
      // If k is recieved
      // Note F#
      else if (data == 'k')
      {
        // Turn off solenoid 10
        digitalWrite(SOL10, LOW);
      }
          
      // If g is recieved
      // Note G
      else if (data == 'g')
      {
        // Turn off solenoid 11
        digitalWrite(SOL11, LOW);
      }
          
      // If l is recieved
      // Note G#
      else if (data == 'l')
      {
        // Turn off solenoid 12
        digitalWrite(SOL12, LOW);
      }

  } 

} 
 
