
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); // use the same baud-rate as the python side

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hello world from Ardunio!"); // write a string
  delay(1000);

}
