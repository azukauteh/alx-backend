#!/usr/bin/node
/**
 * Connect to redis server via redis client
 */
import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client
  .multi() // Use multi() method to start a transaction
  .hset('HolbertonSchools', 'Portland', 50) // Chain individual commands
  .hset('HolbertonSchools', 'Seattle', 80)
  .hset('HolbertonSchools', 'New York', 20)
  .hset('HolbertonSchools', 'Bogota', 20)
  .hset('HolbertonSchools', 'Cali', 40)
  .hset('HolbertonSchools', 'Paris', 2)
  .exec((err, replies) => { // Execute the transaction
    if (err) {
      console.error('Error executing transaction:', err.toString());
      return;
    }
    console.log('Transaction executed successfully:', replies);
  });

client.hgetall('HolbertonSchools', (err, hashset) => {
  if (err) {
    console.error('Error retrieving hash:', err.toString());
    return;
  }
  console.log('Hash stored in Redis:', hashset);
});
