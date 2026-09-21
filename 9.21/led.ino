
int led;
int period;
int duty;
int time;

void setup() {
  led = 9;
  pinMode(led, OUTPUT);
  set_period(100);
  set_duty(100);
 time = 0;

}

void loop() {
 
  analogWrite(led, periodf(period,duty,time));
  time = (time + 10)%period;
  delay(10);
}

int periodf(int period, int duty, int x) {
  int a = (int) (-abs(2.55*duty/(period*0.5f)*(x-period*0.5)) + 2.55*duty);
  if (a < 0) a = 0;
  if (a > 255) a = 255;
  return a; 
  }

 void set_period(int p) {
  period = p;
  }

 void set_duty(int d) {
  duty = d;}
