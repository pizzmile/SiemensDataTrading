#include <ESP8266WiFi.h>

// #define DEVNAME "MILLING"
// #define DEVNAME "PELLETING"
#define DEVNAME "MVLV"


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
    int duration = 60 * 1000;
    // If client is connected send data
    while (client.connected()) {
      /*
      // Milling
      double activePower = random(-873923, 1405200) / 100;
      double reactivePower = random(-939362, 24413100) / 100;
      double apparentPower = random(0, 2529700) / 100;
      double current = random(6674, 151430) / 100;
      double voltage = random(16149, 23615) / 100;
      // Pelletizer
      float activePower = random(-2539150, 29593700) / 100;
      float reactivePower = random(-6185630, 4163200) / 100;
      float apparentPower = random(3658, 43539000) / 100;
      float current = random(4343, 258723) / 100;
      float voltage = random(2562, 24198) / 100;
      */
      
      // MVLV
      float activePower = random(-17227600, 95268800) / 100;
      float reactivePower = random(-46979700, 101334000) / 100;
      float apparentPower = random(20058, 110231000) / 100;
      float current = random(29585, 16951) / 100;
      float voltage = random(55098, 774857) / 100;
      
      
      
      String string = "devName:" + (String)DEVNAME + "&current:" + current + "&voltage:" + voltage + "&activePower:" + activePower + "&reactivePower:" + reactivePower + "&apparentPower:" + apparentPower;
      char char_array[string.length() + 1];
      string.toCharArray(char_array, string.length() + 1);
      client.write(char_array);
      delay(duration);
    }

    delay(500);
}
