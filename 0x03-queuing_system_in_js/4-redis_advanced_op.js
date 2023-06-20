import redis from 'redis';

const client = redis.createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));

client.on("connect", function() {
  console.log("Redis client connected to the server");
});

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, k) => {
  client.hset('HolbertonSchools', key, values[k], redis.print);
});

client.hgetall('HolbertonSchools', (err, value) => {
  console.log(value);
})
