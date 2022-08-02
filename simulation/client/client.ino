#include <ESP8266WiFi.h>

#define DEVNAME "DEV2"


const char* SSID = "OpenWrt";
const char* PSWD = "holyeit0000";

const int PORT = 12345;
const IPAddress ADDR = IPAddress(192, 168, 1, 163);
const int BAUDRATE = 115200;

WiFiClient client;

bool work(int duration) {
    delay(duration);
    return random(0, 2);
}

void setup() {
    Serial.begin(BAUDRATE);
    Serial.println();

    // Begin WiFi
    WiFi.begin(SSID, PSWD);
    // Connect to WiFi
    Serial.print("Connecting to ");
    Serial.print(SSID);
    // Loop until success or timeout
    int numOfAttempts = 0;
    int attemptsLimit = 10;
    while (WiFi.status() != WL_CONNECTED || numOfAttempts < attemptsLimit) {
      numOfAttempts++;
      delay(100);
      Serial.print(".");
    }
    // Connection error
    if (WiFi.status() != WL_CONNECTED) {
      Serial.println();
      Serial.print("Unable to connect to ");
      Serial.print(SSID);
      Serial.println();
      Serial.print("(Restart the device and try again)");
    }
    // Connection successful
    else {
      Serial.println();
      Serial.print("Connected! IP address: ");
      Serial.println(WiFi.localIP());
    }

    // Connect to host
    client.connect(ADDR, PORT);
    if (client) {
        if (client.connected()) {
            Serial.println("Client connected");
        } else {
            Serial.println("Connection to host failed!");
        }
    }
}

void loop() {
    int duration = 1000;
    // If client is connected send data
    while (client.connected()) {
      duration = random(1,5)*1000;
      int timestamp = millis();
      bool success = work(duration);
      bool defective = false;
      if (success) {
        defective = random(0,2);
      }
      
      String string = "timestamp:" + (String)timestamp + "&devName:" + (String)DEVNAME +"&success:" + (String)success + "&defective:" + (String)defective + "&duration:" + (String)duration;
      char char_array[string.length() + 1];
      string.toCharArray(char_array, string.length() + 1);
      client.write(char_array);
    }

    delay(500);
}
