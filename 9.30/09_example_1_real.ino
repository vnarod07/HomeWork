
// Arduino pin assignment
#define PIN_LED 9
#define PIN_TRIG 11
#define PIN_ECHO 12
  
// configurable parameters
#define SND_VEL 346.0     // sound velocity at 24 celsius degree (unit: m/sec)
#define INTERVAL 25       // sampling interval (unit: msec)
#define PULSE_DURATION 10 // ultra-sound Pulse Duration (unit: usec)
#define _DIST_MIN 100     // minimum distance to be measured (unit: mm)
#define _DIST_MAX 300     // maximum distance to be measured (unit: mm)

#define TIMEOUT ((INTERVAL / 2) * 1000.0) // maximum echo waiting time (unit: usec)
#define SCALE (0.001 * 0.5 * SND_VEL)     // coefficent to convert duration to distance
          
#define N 30

// global variables
unsigned long last_sampling_time;   // unit: msec
float dist_prev = _DIST_MAX;        // Distance last-measured
float dist_ema;
float dist_median;                  // EMA distance
float alpha;
boolean start;
int n;
float dist[N];
float stack[N];

void setup() {
  // initialize GPIO pins
  alpha = 0.5f;
  start = 0;
  n = 1;

  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);

  digitalWrite(PIN_TRIG, LOW);

  // initialize serial port
  Serial.begin(57600);

  dist_ema = 0.5f * (_DIST_MIN + _DIST_MAX);
}

void loop() {
  float dist_raw, dist_filtered;

  // wait until next sampling time.
  // millis() returns the number of milliseconds since the program started.
  // will overflow after 50 days.
  if (millis() < last_sampling_time + INTERVAL)
    return;

  // get a distance reading from the USS
  dist_raw = USS_measure(PIN_TRIG, PIN_ECHO);

  dist_ema = alpha * dist_raw + (1.0f - alpha) * dist_ema;

  dist[n - 1] = dist_raw;

  if (n == N) {
    float arr[N];

    for (int i = 0; i < N; i++) {
      arr[i] = dist[i];
    }

    for (int i = 0; i < N - 1; i++) {
      for (int j = 0; j < N - 1 - i; j++) {
        if (arr[j] > arr[j + 1]) {
          float temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }

    if (N % 2 == 0) {
      dist_median = 0.5f * (arr[N / 2 - 1] + arr[N / 2]);
    } else {
      dist_median = arr[N / 2];
    }

    n = 1;
  } else {
    n++;
  }

  // output the distance to the serial port
  Serial.print("Min:");
  Serial.print(_DIST_MIN);

  Serial.print(",raw:");
  Serial.print(min(dist_raw, _DIST_MAX + 100));

  Serial.print(",ema:");
  Serial.print(min(dist_ema, _DIST_MAX + 100));

  Serial.print(",Max:");
  Serial.print(_DIST_MAX);

  Serial.print(",Median: ");
  Serial.print(dist_median);

  Serial.println("");

  // do something here
  if ((dist_raw < _DIST_MIN) || (dist_raw > _DIST_MAX))
    digitalWrite(PIN_LED, 1); // LED OFF
  else
    digitalWrite(PIN_LED, 0); // LED ON

  // update last sampling time
  last_sampling_time += INTERVAL;
}

// get a distance reading from USS. return value is in millimeter.
float USS_measure(int TRIG, int ECHO) {
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(PULSE_DURATION);
  digitalWrite(TRIG, LOW);

  return pulseIn(ECHO, HIGH, TIMEOUT) * SCALE; // unit: mm
}
